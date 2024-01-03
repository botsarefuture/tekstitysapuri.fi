from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import uuid  # for generating unique IDs
from TranscriptionClient import TranscriptionClient
import threading

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULT_FOLDER'] = 'results'
app.config['STATUS_FOLDER'] = 'status'

# Configure the TranscriptionClient with your server address
transcription_client = TranscriptionClient(status_path=app.config['STATUS_FOLDER'])

job_status = {}

def transcribe_in_background(audio_path, model, result_id):
    # Transcribe the audio and get the response
    response = transcription_client.transcribe_and_get_response(audio_path, model, result_id)

    with open(response, "r") as f:
        response_content = f.read()

    # Save the result in a file with the unique ID
    result_file_path = os.path.join(app.config['RESULT_FOLDER'], f"{result_id}.srt")
    with open(result_file_path, 'w') as result_file:
        result_file.write(response_content)

    # Update the job status to completed
    job_status[result_id] = {"status": "completed"}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio_file' not in request.files:
        return redirect(request.url)

    audio_file = request.files['audio_file']

    if audio_file.filename == '':
        return redirect(request.url)

    if audio_file:
        audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
        audio_file.save(audio_path)

        model = request.form.get('model', 'base')

        result_id = str(uuid.uuid4())

        # Start transcription in a separate thread
        transcription_thread = threading.Thread(
            target=transcribe_in_background,
            args=(audio_path, model, result_id)
        )
        transcription_thread.start()

        # Redirect to the status page while continuing the transcription in the background
        return redirect(url_for('show_status', result_id=result_id))

    return redirect(request.url)

@app.route("/set_status/<job_id>")
def set_status(job_id):
    job_status[job_id] = request.json.get("status")
    return ""

@app.route('/status/<result_id>')
def show_status(result_id):
    return render_template('status.html', result_id=result_id)


@app.route("/get_status/<job_id>")
def get_status(job_id):
    try:
        status_path = os.path.join(app.config['STATUS_FOLDER'], f"{job_id}.txt")
        with open(status_path) as f:
            status = f.read()
    except FileNotFoundError:
        return {"status": "In queque"}

    if status.startswith(str(100)):
        return {"status": "completed"}
    
    else:
        return {"status": status}
    
@app.route('/result/<result_id>')
def show_result(result_id):
    # Read the result from the file with the given ID
    result_file_path = os.path.join(app.config['RESULT_FOLDER'], f"{result_id}.srt")
    try:
        with open(result_file_path, 'r') as result_file:
            subtitles_content = result_file.read()
            return render_template('result.html', subtitles_content=subtitles_content)
    except FileNotFoundError:
        return "Result not found."

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
