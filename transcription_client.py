import threading
import time  # Added time for sleep function
import logging
from audio_transcription import transcribe_audio
import json

# Set the logging level for the entire application
logging.basicConfig(level=logging.INFO)

# Get the logger for the current module
logger = logging.getLogger(__name__)

# Enable DEBUG level only for this file
logger.setLevel(logging.DEBUG)


class Job:
    def __init__(self, file_path, job_id, status="in progress"):
        self.file_path = file_path
        self.job_id = job_id
        self.status = status

    def __json__(self):
        return json.dumps(
            {"file_path": self.file_path, "job_id": self.job_id, "status": self.status}
        )


class TranscriptionClient:
    def __init__(self, status_path=None):
        self.status_path = status_path

    def transcribe_and_get_response(
        self, audio_path, model="base", job_id=None, lang="fi"
    ):
        # Start a new thread for audio transcription
        transcribe_thread = threading.Thread(
            target=self.transcribe_locally,
            args=(audio_path, model, job_id, self.status_path, lang),
        )
        transcribe_thread.start()

        # Monitor progress in the main thread
        while transcribe_thread.is_alive():
            logger.debug(f"JOB {job_id}: is still alive.")
            time.sleep(1)

        logger.info(f"JOB {job_id}: finished or died.")

        # Wait for the transcription thread to finish and return the response
        transcribe_thread.join()
        logger.info(f"JOB {job_id}: Done.")
        logger.debug(f"JOB {job_id}: Result path: results/{job_id}.srt")
        return f"results/{job_id}.srt"

    def transcribe_locally(
        self, audio_path, model="base", job_id=None, status_path=None, lang=None
    ):
        # Use the whisper script to transcribe audio locally
        transcribe_audio(audio_path, model, job_id, status_path=status_path, lang=lang)


if __name__ == "__main__":
    # Example usage:
    client = TranscriptionClient()
    response = client.transcribe_and_get_response(
        "tallenne.m4a", model="base", job_id="123"
    )
    print(response)
