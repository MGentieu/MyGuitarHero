import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt, find_peaks
import numpy as np

y, sr = librosa.load("../A-440.wav", sr=10000)
#print(sr)
#D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)

"""
plt.figure(figsize=(10, 5))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()
"""



def bandpass_filter(data, lowcut, highcut, fs, order=4):
    sos = butter(order, [lowcut, highcut], btype='band', fs=fs, output='sos')
    return sosfilt(sos, data)

filtered_signal = bandpass_filter(y, lowcut=80, highcut=1200, fs=sr)

D = librosa.amplitude_to_db(librosa.stft(filtered_signal), ref=np.max)
plt.figure(figsize=(10, 5))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()

"""
peaks, _ = find_peaks(filtered_signal, height=0.2, prominence=1, distance = 1000)  # Ajuste la hauteur des pics
times = librosa.frames_to_time(peaks, sr=sr)

print(len(peaks))
print("Temps des notes :", times)
"""