# Speech-to-text Recognition
This python library use [Wav2Vec2](https://huggingface.co/docs/transformers/model_doc/wav2vec2) as speech to text recognition model

### variable and return type
**variable**\
`model_path:` path that collect speech to text model.
`preprocess_path:` path that collect speech to text preprocessor.

**return type**\
`get_text_from_speech:` List[str]
### How to use
```python
from speech_to_text.usecase.engine import SpeechToTextEngine
engine = SpeechToTextEngine(model_path="PATH TO MODEL", preprocess_path="PATH TO PREPROCESS")

engine.get_text_from_speech(wave_tensor)

#return value
["GOING ALONG SLUSHY COUNTRY ROADS AND SPEAKING TO DAMP AUDIENCES IN DRAUGHTY SCHOOL ROOMS DAY AFTER DAY FOR A FORTNIGHT HE'LL HAVE TO PUT IN AN APPEARANCE AT SOME PLACE OF WORSHIP ON SUNDAY MORNING AND HE CAN COME TO US IMMEDIATELY AFTERWARDS"]
```
