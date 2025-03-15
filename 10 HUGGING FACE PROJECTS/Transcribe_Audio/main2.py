<<<<<<< HEAD:10 HUGGING FACE PROJECTS/Transcribe_Audio/main.py
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
=======
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

import gradio as gr
import torch
import cv2
import numpy as np
import whisper
from transformers import MarianMTModel, MarianTokenizer
import moviepy.editor as mp

def transcribe_and_translate_video(video_path):
    # Load Whisper ASR Model
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    english_text = result["text"]
    
    # Load English-to-Bangla translation model
    model_name = "Helsinki-NLP/opus-mt-en-bn"
    translator = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    
    # Translate to Bangla
    translated = tokenizer(english_text, return_tensors="pt", padding=True, truncation=True)
    translated_ids = translator.generate(**translated)
    bangla_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)
    
    # Overlay subtitles on video
    clip = mp.VideoFileClip(video_path)
    txt_clip = mp.TextClip(bangla_text, fontsize=24, color='white')
    txt_clip = txt_clip.set_position(('center', 'bottom')).set_duration(clip.duration)
    video_with_subs = mp.CompositeVideoClip([clip, txt_clip])
    output_path = "output_with_subtitles.mp4"
    video_with_subs.write_videofile(output_path, codec="libx264")
    
    return output_path

# Gradio UI
demo = gr.Interface(fn=transcribe_and_translate_video, inputs=gr.Video(type="filepath"), outputs=gr.Video())

demo.launch()
>>>>>>> d35ad20e088c8763951ba5799dd811a4aa4e6d77:10 HUGGING FACE PROJECTS/main.py
