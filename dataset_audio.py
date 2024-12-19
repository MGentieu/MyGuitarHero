import librosa
import numpy as np
import pandas as pd

# Charger le fichier audio
audio_path = "C:/Users/33695/Music/plug_in_baby_guitar_only.wav"
y, sr = librosa.load(audio_path)

# Fréquences définies
frequencies_to_analyze = np.array([220.0, 233.1, 246.9, 261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370.0, 392.0, 415.3, 440.0])

# Créer un spectrogramme Constant-Q basé sur les fréquences spécifiées
C = librosa.cqt(
    y,
    sr=sr,
    fmin=frequencies_to_analyze[0],   # Fréquence minimale (la plus basse)
    n_bins=len(frequencies_to_analyze),  # Nombre de fréquences analysées
    bins_per_octave=len(frequencies_to_analyze)  # Un bin par fréquence
)

# Convertir les amplitudes brutes en décibels
C_db = librosa.amplitude_to_db(np.abs(C), ref=np.max)

# Extraire les amplitudes par échantillon (frame)
frames = librosa.frames_to_time(np.arange(C_db.shape[1]), sr=sr)
samples_per_frame = int(len(y) / len(frames))  # Nombre approximatif d'échantillons par frame

# Créer un DataFrame avec les amplitudes (frame par frame)
spectrogram_df = pd.DataFrame(
    data=C_db, 
    index=frequencies_to_analyze,  # Les fréquences
    columns=[f"Frame {i}" for i in range(C_db.shape[1])]  # Une colonne par frame
)
#print(spectrogram_df.columns)
spectrogram_df.describe()
spectrogram_df.head(100)
# Exporter en CSV
#spectrogram_df.to_csv('spectrogram_amplitudes_per_frame.csv', index_label="Frequency (Hz)")
