from flask import Flask, render_template, request, redirect, url_for
import os
import uuid
from transcription_client import TranscriptionClient
from queue_module import Queue
import time

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["RESULT_FOLDER"] = "results"
app.config["STATUS_FOLDER"] = "status"

job_status = {}


class Runner:
    def __init__(self, name):
        self.name = name
        self.busy = False

    def run_task(self, task):
        self.busy = True
        _, _, result_id, _ = task
        print(f"{self.name} is running task: {result_id}")
        time.sleep(2)
        print(f"{self.name} completed task: {result_id}")
        self.busy = False

    def is_busy(self):
        return self.busy


class TranscriptionRunner(Runner):
    def __init__(self, name, transcription_client):
        super().__init__(name)
        self.transcription_client = transcription_client

    def run_task(self, task):
        super().run_task(task)
        audio_path, model, result_id, language = task
        response = self.transcription_client.transcribe_and_get_response(
            audio_path, model, result_id, lang=language
        )

        with open(response, "r") as f:
            response_content = f.read()

        result_file_path = os.path.join(app.config["RESULT_FOLDER"], f"{result_id}.srt")
        with open(result_file_path, "w") as result_file:
            result_file.write(response_content)

        job_status[result_id] = {"status": "completed"}


transcription_client = TranscriptionClient(status_path=app.config["STATUS_FOLDER"])
runner1 = TranscriptionRunner("Runner 1", transcription_client)
runner2 = TranscriptionRunner("Runner 2", transcription_client)
transcription_queue = Queue(runners=[runner1, runner2])


def transcribe_in_background(audio_path, model, result_id, language):
    response = transcription_client.transcribe_and_get_response(
        audio_path, model, result_id, lang=language
    )

    with open(response, "r") as f:
        response_content = f.read()

    result_file_path = os.path.join(app.config["RESULT_FOLDER"], f"{result_id}.srt")
    with open(result_file_path, "w") as result_file:
        result_file.write(response_content)

    job_status[result_id] = {"status": "completed"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio_file" not in request.files:
        return redirect(request.url)

    audio_file = request.files["audio_file"]
    if audio_file.filename == "":
        return redirect(request.url)

    if audio_file:
        audio_path = os.path.join(app.config["UPLOAD_FOLDER"], audio_file.filename)
        audio_file.save(audio_path)

        model = request.form.get("model", "base")
        language = request.form.get("language")
        result_id = str(uuid.uuid4())
        transcription_queue.add_task((audio_path, model, result_id, language))
        return redirect(url_for("show_status", result_id=result_id))

    return redirect(request.url)


@app.route("/set_status/<job_id>")
def set_status(job_id):
    job_status[job_id] = request.json.get("status")
    return ""


@app.route("/status/<result_id>")
def show_status(result_id):
    return render_template("status.html", result_id=result_id)


@app.route("/get_status/<job_id>")
def get_status(job_id):
    try:
        status_path = os.path.join(app.config["STATUS_FOLDER"], f"{job_id}.txt")
        with open(status_path) as f:
            status = f.read()
    except FileNotFoundError:
        return {"status": "In queue"}

    return (
        {"status": "completed"} if status.startswith(str(100)) else {"status": status}
    )


@app.route("/result/<result_id>")
def show_result(result_id):
    result_file_path = os.path.join(app.config["RESULT_FOLDER"], f"{result_id}.srt")
    try:
        with open(result_file_path, "r") as result_file:
            subtitles_content = result_file.read()
            return render_template("result.html", subtitles_content=subtitles_content)
    except FileNotFoundError:
        return "Result not found."


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
