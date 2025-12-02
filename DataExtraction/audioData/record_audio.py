import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
duration = 5  # seconds

print("Recording audio for 5 seconds")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()

write("audio.wav", fs, audio)
print("Audio saved as audio.wav")
