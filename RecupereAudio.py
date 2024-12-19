import os
from pydub import AudioSegment
import subprocess

def youtube_to_wav(youtube_url, output_folder, title):
    try:
        os.makedirs(output_folder, exist_ok=True)
        output_file = os.path.join(output_folder, title)

        print(f"Téléchargement de l'audio depuis : {youtube_url}")
        subprocess.run(
            ["yt-dlp", "-f", "bestaudio", "-o", output_file, youtube_url],
            check=True
        )
        
        wav_file = os.path.splitext(output_file)[0] + ".wav"
        print("Conversion en WAV...")
        audio = AudioSegment.from_file(output_file)
        audio.export(wav_file, format="wav")
        os.remove(output_file)

        print(f"Conversion terminée. Fichier WAV enregistré dans : {wav_file}")
        return wav_file
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du téléchargement avec yt-dlp : {e}")
    except Exception as e:
        print(f"Erreur : {e}")
        return None

# Exemple d'utilisation
youtube_url = "https://www.youtube.com/watch?v=fox_5DQ8Hz8"
output_folder = "C:/Users/33695/Music" # à personnaliser.
youtube_url_2="https://www.youtube.com/watch?v=8D0ybTfYmCE"
youtube_url_3="https://www.youtube.com/watch?v=uajxUDu12kw"
yt_url4="https://www.youtube.com/watch?v=iC8oP4Z_xPw"
yt_url5="https://www.youtube.com/watch?v=zdtxioCmtMc"
yt_url6="https://www.youtube.com/watch?v=h66dI0q_9As"
yt_url7="https://www.youtube.com/watch?v=KYkm5_fDthc"
#youtube_to_wav(youtube_url, output_folder, "rush_E.mp4")
youtube_to_wav(youtube_url_2, output_folder, "bliss.mp4")
youtube_to_wav(youtube_url_3, output_folder, "plug_in_baby.mp4")
youtube_to_wav(yt_url4, output_folder, "love_rock_n_roll.mp4")
youtube_to_wav(yt_url5, output_folder, "psycho.mp4")
youtube_to_wav(yt_url6, output_folder, "take_me_out.mp4")
youtube_to_wav(yt_url7, output_folder, "plug_in_baby_guitar_only.mp4")


