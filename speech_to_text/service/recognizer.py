from typing import List

import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


class RecognizerService:
    def __init__(self, model_path: str, preprocess_path: str, device: str):
        self.device = device
        self.model = self._load_model(model_path=model_path)
        self.preprocess = self._load_preprocess(preprocess_path=preprocess_path)

    def _load_model(self, model_path: str):
        return Wav2Vec2ForCTC.from_pretrained(model_path)

    def _load_preprocess(self, preprocess_path: str):
        return Wav2Vec2Processor.from_pretrained(preprocess_path)

    def _preprocess(self, wave_tensor: torch.Tensor, simple_rate: int) -> torch.Tensor:
        return self.preprocess(
            wave_tensor,
            sampling_rate=simple_rate,
            return_tensors="pt",
            padding="longest",
        ).input_values

    def _inference(self, wave_tensor: torch.Tensor) -> torch.Tensor:
        with torch.no_grad():
            return self.model(wave_tensor.squeeze(dim=0).to(self.device))

    def _postprocess(self, wave_tensor: torch.Tensor) -> List[str]:
        logits = wave_tensor.logits
        prediction_ids = torch.argmax(logits, dim=-1)
        return self.preprocess.batch_decode(prediction_ids)

    def recognize(self, wave_tensor: torch.Tensor, simple_rate: int) -> torch.Tensor:
        preprocessed_tensor = self._preprocess(wave_tensor, simple_rate)
        inferenced_tensor = self._inference(preprocessed_tensor)
        return self._postprocess(inferenced_tensor)
