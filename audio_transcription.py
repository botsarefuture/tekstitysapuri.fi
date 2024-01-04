# Import necessary libraries and modules
import argparse
from datetime import timedelta
import whisper
from rerun_transcription import transcribe_with_rerun

# Function to format time in HH:MM:SS,mmm format
def format_time(seconds):
    # Convert seconds to timedelta
    time_delta = timedelta(seconds=seconds)

    # Extract hours, minutes, seconds, and milliseconds
    hours, remainder = divmod(time_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = time_delta.microseconds // 1000

    # Format the time
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

    return formatted_time

# Function to transcribe audio and save as SRT file
def transcribe_audio(input_audio, model, job_id, status_path, lang):
    # Check if the specified model is supported by whisper
    if model not in whisper.available_models():
        raise Exception(f"Model is not available. \nTry one of these models:\n{whisper.available_models()}")

    # Load the audio file using whisper library
    audio = whisper.load_audio(input_audio)
    
    # Transcribe the audio using the loaded model
    result = transcribe_with_rerun(model, audio, word_timestamps=True, verbose=True, job_id=job_id, status_path=status_path, language=lang)
    
    # Save the transcript to an SRT file
    with open(f"results/{job_id}.srt", 'w') as srt_file:
        for segment in result['segments']:
            # Format start and end times
            start_time = format_time(segment["start"])
            end_time = format_time(segment['end'])
            
            # Process and write each segment to the SRT file
            srt_file.write(f"{segment['id']+1}\n{start_time} --> {end_time}\n{(segment['text'].strip()).replace('  ', ' ')}\n\n")

if __name__ == "__main__":
    # Command-line argument parser
    parser = argparse.ArgumentParser(description="Transcribe audio to SRT using whisper")
    
    # Define command-line arguments
    parser.add_argument("input_audio", help="Path to the input audio file")
    parser.add_argument("output_srt", help="Path to the output SRT file")
    parser.add_argument("model", help="Name of the whisper ASR model", choices=whisper.available_models())

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the transcribe_audio function with provided arguments
    transcribe_audio(args.input_audio, args.output_srt, args.model)
