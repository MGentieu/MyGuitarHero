import pandas as pd
import librosa
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Charger le fichier audio
audio_path = 'votre_audio.wav'
y, sr = librosa.load(audio_path)

# Définir les fréquences spécifiques que vous souhaitez analyser (par exemple, 1000 Hz à 5000 Hz)
frequencies_to_analyze = [220.0, 233.1, 246.9, 261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370.0, 392.0, 415.3, 440.0]
frequencies_to_analyze = np.linspace(1000, 5000, num=100)  # Plage de fréquences entre 1000 et 5000 Hz

# Calculer le spectrogramme Constant-Q
C = librosa.cqt(y, sr=sr, fmin=frequencies_to_analyze[0], n_bins=len(frequencies_to_analyze))

# Afficher le spectrogramme dans la plage de fréquences définie
plt.figure(figsize=(10, 6))
librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max), y_axis='cqt_hz', x_axis='time', sr=sr)
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogramme Constant-Q (plage de fréquences définie)')
plt.show()

# Exporter les données sous forme de CSV pour analyse
time_steps = np.arange(C.shape[1])
freq_steps = frequencies_to_analyze

# Créer un DataFrame avec les données
spectrogram_df = pd.DataFrame(C, index=freq_steps, columns=time_steps)

# Sauvegarder les données en CSV
spectrogram_df.to_csv('spectrogram_data.csv')
"""
def load_dataset(input_file):
    try:
        df = pd.read_csv(input_file)

        df.describe()
        print(df.columns)

        return df  
    

    except Exception as e:
        print(f"Erreur : {e}")
        return None


load_dataset("C:/Users/33695/Music/test.csv")
"""