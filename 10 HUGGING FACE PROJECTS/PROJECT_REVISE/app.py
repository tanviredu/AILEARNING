import warnings
import torch 
import gradio as gr 
import librosa
from transformers import Wav2Vec2ForCTC,Wav2Vec2Processor

warnings.filterwarnings("ignore")

processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model     = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def transcribe_audio(audio_path):
    try:
        audio,sampling_rate = librosa.load(audio_path,sr=16000)
        input_values        = processor(audio,return_tensors='pt',sampling_rate=16000).input_values
        
        with torch.no_grad():
            logits = model(input_values).logits
        
        predicted_ids  = torch.argmax(logits,dim=-1)
        transcriptions = processor.batch_decode(predicted_ids)[0]
        return transcriptions
    except Exception as e:
        return str(e)
    
demo = gr.Interface(
    fn = transcribe_audio,
    inputs = gr.Audio(type="filepath"),
    outputs= "text",
    title="Subtititle Generator",
    description="This tool transcribes audio files into text."
)

demo.launch()
        