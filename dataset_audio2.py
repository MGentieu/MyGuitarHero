import numpy as np
import librosa
import pandas as pd
from scipy.fft import rfft, rfftfreq


# Charger le fichier audio
audio_path = "C:/Users/33695/Music/plug_in_baby_guitar_only.wav"
y, sr = librosa.load(audio_path, sr=5000) # sr = Feq = 5000 Hz

# Fréquences définies à analyser : les notes de A3 à A4
freqs = [220.0, 233.1, 246.9, 261.6, 277.2, 293.7, 311.1, 329.6, 349.2, 370.0, 392.0, 415.3, 440.0]
frequencies_to_analyze = np.array(freqs)

segment_duration = 0.1103  #BPM à 136, donc temps pour une double-croche
segment_samples = int(segment_duration * sr)

# Découper le signal en segments de 0.11029 seconde
segments = [
    y[i:i+segment_samples] for i in range(0, len(y), segment_samples)
    if len(y[i:i+segment_samples]) == segment_samples
]

# Analyse des amplitudes pour les fréquences définies avec la FFT
data = []
for i, segment in enumerate(segments):
   
    fft_amplitudes = np.abs(rfft(segment))
    fft_frequencies = rfftfreq(len(segment), d=1/sr)

    segment_data = {"Segment": i}
    for f in frequencies_to_analyze:
  
        idx = (np.abs(fft_frequencies - f)).argmin()
        segment_data[f] = fft_amplitudes[idx]
    
    data.append(segment_data)

# On convertit ensuite en DataFrame pandas pour analyse
df = pd.DataFrame(data)

#On trouve la max pour chaque colonne, et on met le reste à 0
for index, row in df.iterrows():
    max_freq = row[1:].idxmax() 
    df.loc[index, row.index[1:]] = 0 
    df.loc[index, max_freq] = row[max_freq]  


segment_to_note = {}

#On parcoure le dataframe, et on enlève tous les attributs à 0 afin de n'avoir que deux colonnes : le segment et la note détectée.
for index, row in df.iterrows():
    
    max_amplitude = row[1:].max()
    if max_amplitude > 0: 
        detected_note = row[1:].idxmax()  
        detected_note = float(detected_note)
        segment_to_note[float(row['Segment'])] = detected_note
     

def segment_to_time(segment, segment_duration=0.1):
    return segment * segment_duration
    
segment_to_time_dict = dict(map(lambda item: (segment_to_time(item[0]), item[1]), segment_to_note.items()))

#On change les segments en temps réel.

df_time_note = pd.DataFrame(list(segment_to_time_dict.items()), columns=['Time (s)', 'Detected Note'])

#On change les fréquences en notes

frequency_to_note_mapping = {
    220.0: 'A3',
    233.1: 'A#3',
    246.9: 'B3',
    261.6: 'C4',
    277.2: 'C#4',
    293.7: 'D4',
    311.1: 'D#4',
    329.6: 'E4',
    349.2: 'F4',
    370.0: 'F#4',
    392.0: 'G4',
    415.3: 'G#4',
    440.0: 'A4'
}


df_time_note['Detected Note'] = df_time_note['Detected Note'].map(frequency_to_note_mapping)

#On enregistre maintenant notre dataframe final dans un fichier CSV.

df_time_note.to_csv('segments_with_times_and_notes.csv', index=False,sep=';')

#df = pd.read_csv('frequencies_to_analyze_amplitudes_per_segment.csv')

#print(df.shape)  # Affiche le nombre de lignes et de colonnes
#print(df.info())  # Affiche des informations sur les colonnes et leurs types
#print(df.head())  # Affiche les 5 premières lignes
#print(df)


print("Analyse terminée. Les données ont été exportées dans frequencies_to_analyze_amplitudes_per_segment.csv.")
