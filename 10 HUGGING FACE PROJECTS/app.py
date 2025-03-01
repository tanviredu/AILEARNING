import warnings
import gradio as gr
import librosa
import torch
import numpy as np
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

warnings.filterwarnings("ignore")

# Load model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def transcribe_audio(audio_path):
    try:
        # Load and preprocess audio
        audio, sampling_rate = librosa.load(audio_path, sr=16000)
        input_values = processor(audio, return_tensors="pt", sampling_rate=16000).input_values
        
        # Perform speech-to-text
        with torch.no_grad():
            logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.batch_decode(predicted_ids)[0]
        
        return transcription
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio Interface
demo = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Speech-to-Text Transcription",
    description="Upload an audio file (wav, mp3, mp4, etc.) and get its transcription."
)

demo.launch()
