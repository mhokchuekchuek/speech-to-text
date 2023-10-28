from typing import List

import torch

from speech_to_text.service.recognizer import RecognizerService


class SpeechToTextEngine:
    def __init__(self, model_path: str, preprocess_path: str):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.recognizer = RecognizerService(
            model_path=model_path, preprocess_path=preprocess_path, device=device
        )

    def get_text_from_speech(
        self, wave_tensor: torch.Tensor, simple_rate: int
    ) -> List[str]:
        return self.recognizer.recognize(
            wave_tensor=wave_tensor, simple_rate=simple_rate
        )
