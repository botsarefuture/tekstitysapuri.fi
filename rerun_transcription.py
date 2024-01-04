import torch
import numpy as np
from typing import Union, Tuple

import time

import whisper


def transcribe_with_rerun(
    initial_model: "Whisper",
    audio: Union[str, np.ndarray, torch.Tensor],
    rerun_module_threshold: float = 0.5,
    rerun_module: str = "medium",
    **decode_options,
):
    rerun_needed = False

    initial_model_c = whisper.load_model(initial_model)
    # Initial detection using the provided model
    initial_result = initial_model_c.transcribe(audio, **decode_options)

    for index, segment in enumerate(initial_result["segments"]):
        # Extract tokens and confidence scores from the initial result
        confidence = segment.get("temperature", [])

        if rerun_needed != True:
            rerun_needed = confidence > rerun_module_threshold

    # If the segment requires rerun, rerun only that segment
    if rerun_needed and not initial_model == rerun_module:
        print("rerun")
        # Create a new model instance with the better module
        rerun_model_c = whisper.load_model(rerun_module)  # Replace with your actual class and module selection logic

        # Rerun detection for the specific segment
        rerun_result = rerun_model_c.transcribe(audio, **decode_options) # make this able to only rerun the segment

        # Update the initial result with the rerun results for the specific segment
        initial_result["segments"] = rerun_result["segments"]

    return initial_result
