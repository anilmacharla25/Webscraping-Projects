import deepspeech
import librosa
import numpy as np
import soundfile as sf

# Step 3: Load the DeepSpeech model
model_path = r"C:\Users\prave\Downloads\deepspeech-0.9.3-models.pbmm"
model = deepspeech.Model(model_path)

# Step 4: Load the audio file
# audio_path = r"C:\Users\prave\Downloads\OSR_us_000_0010_8k.wav"
audio_path =r"C:\Users\prave\Downloads\OSR_us_000_0010_8k.wav"
# Load the audio file using soundfile
audio_data, sample_rate = sf.read(audio_path)
print(audio_data,sample_rate)

# Resample audio to 16kHz if necessary using librosa
target_sample_rate = 16000
if sample_rate != target_sample_rate:
    audio_data = librosa.resample(audio_data.T,orig_sr=sample_rate-50, target_sr=16000).T
    sample_rate = target_sample_rate

# Convert audio data to int16 format
audio_data = (audio_data * 32767).astype(np.int16)

# Step 5: Perform speech-to-text inference
text = model.stt(audio_data)
print("Transcription:", text)
