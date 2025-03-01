import warnings
warnings.filterwarnings("ignore")
import transformers
import librosa
import torch
import numpy as np
from transformers import pipeline
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")
audio,sampling_rate = librosa.load('./BreakingBad.mp4',sr=16000)
input_values = tokenizer(audio, return_tensors="pt").input_values
non_normalizedd_logits = model(input_values).logits
predicted_ids = torch.argmax(non_normalizedd_logits, dim=-1)
transcription = tokenizer.decode(predicted_ids[0])
print(transcription)