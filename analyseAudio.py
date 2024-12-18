import librosa
import librosa.display
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfilt
import numpy as np

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    sos = butter(order, [lowcut, highcut], btype='band', fs=fs, output='sos')
    return sosfilt(sos, data)

def extract_main_notes(signal, sr, hop_length=512, threshold=0.2, min_time_gap=0.2):
    # STFT et spectrogramme
    stft = librosa.stft(signal, hop_length=hop_length)
    magnitude = np.abs(stft)
    frequencies = librosa.fft_frequencies(sr=sr)
    times = librosa.frames_to_time(range(magnitude.shape[1]), sr=sr, hop_length=hop_length)

    main_notes = []
    last_time = -min_time_gap  # Initialiser pour permettre la première note

    for t in range(magnitude.shape[1]):
        spectrum = magnitude[:, t]
        if np.max(spectrum) < threshold * np.max(magnitude):
            continue  # Ignorer si l'énergie est trop faible

        # Trouver la fréquence avec l'amplitude maximale
        peak_index = np.argmax(spectrum)
        freq = frequencies[peak_index]
        note = librosa.hz_to_note(freq).replace('♯', '#').replace('♭', 'b')

        # Ignorer si trop proche de la dernière note détectée
        if times[t] - last_time >= min_time_gap:
            main_notes.append((times[t], freq, note))
            last_time = times[t]

    return main_notes

# Chargement du fichier audio
y, sr = librosa.load("C:/Users/33695/Music/psycho_guitar.wav", sr=5000)

# Application du filtre passe-bande
filtered_signal = bandpass_filter(y, lowcut=160, highcut=1200, fs=sr)

# Affichage du spectrogramme
D = librosa.amplitude_to_db(np.abs(librosa.stft(filtered_signal)), ref=np.max)
plt.figure(figsize=(10, 5))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', hop_length=512)
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()

# Extraction des notes principales
notes = extract_main_notes(filtered_signal, sr, hop_length=512, threshold=0.3, min_time_gap=0.2)

# Affichage des résultats
print("Notes principales détectées :")
for time, freq, note in notes:
    print(f"Temps : {time:.2f} s, Fréquence : {freq:.2f} Hz, Note : {note}")


"""
peaks, _ = find_peaks(filtered_signal, height=0.2, prominence=1, distance = 1000)  # Ajuste la hauteur des pics
times = librosa.frames_to_time(peaks, sr=sr)

print(len(peaks))
print("Temps des notes :", times)
"""

"""
plt.figure(figsize=(10, 5))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()
"""
