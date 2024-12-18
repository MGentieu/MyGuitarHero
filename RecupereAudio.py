"""

from pytube import YouTube
from pydub import AudioSegment
import os




def youtube_to_wav(youtube_url, output_folder):
    try:
        # Télécharger la vidéo YouTube
        yt = YouTube(youtube_url)
        video_stream = yt.streams.filter(only_audio=True).first()
        
        print(f"Téléchargement de {yt.title}...")
        downloaded_file = video_stream.download(output_folder)
        print(f"Fichier téléchargé : {downloaded_file}")
        
        # Convertir le fichier audio en WAV
        base, ext = os.path.splitext(downloaded_file)
        wav_file = base + ".wav"
        
        print("Conversion en WAV...")
        audio = AudioSegment.from_file(downloaded_file)
        audio.export(wav_file, format="wav")
        
        # Supprimer le fichier temporaire (optionnel)
        os.remove(downloaded_file)
        
        print(f"Conversion terminée. Fichier WAV enregistré dans : {wav_file}")
        return wav_file
    except Exception as e:
        print(f"Erreur : {e}")

# Exemple d'utilisation
if __name__ == "__RecupereAudio__":
    youtube_url = "https://www.youtube.com/watch?v=fox_5DQ8Hz8"
    output_folder = "downloads"
    os.makedirs(output_folder, exist_ok=True)
    youtube_to_wav(youtube_url, output_folder)
"""

from pydub import AudioSegment
from pydub.utils import which

#AudioSegment.converter = which("C:/ffmpeg/bin/ffmpeg.exe")

import os

print(os.environ["PATH"])