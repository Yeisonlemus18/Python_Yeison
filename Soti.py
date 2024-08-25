import os
import yt_dlp
from pydub import AudioSegment

def descargar_y_convertir(url, carpeta_destino):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
            'noplaylist': True,  # Para descargar solo un video, no una lista de reproducción
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            archivo_video = ydl.prepare_filename(info_dict)
            archivo_mp3 = os.path.splitext(archivo_video)[0] + '.mp3'

            # Convertir el archivo descargado a MP3
            audio = AudioSegment.from_file(archivo_video)
            audio.export(archivo_mp3, format='mp3')

            # Eliminar el archivo de video descargado
            os.remove(archivo_video)

            print(f"Descargado y convertido: {archivo_mp3}")
    except Exception as e:
        print(f"Error al procesar {url}: {e}")

def main():
    # URL de la lista de reproducción
#Salsa    playlist_url = 'https://www.youtube.com/playlist?list=PLhxNyMmTLzoxuruCiW1gcYfLKVpY8OkQs'
#Bachata    playlist_url = 'https://www.youtube.com/playlist?list=PLhxNyMmTLzoy905p5FBUjUMl7E1FcnHCS'
#Merengue    
    playlist_url = 'https://www.youtube.com/playlist?list=PLhxNyMmTLzozdrrfH7dvmn4ImI4gaJwLN'
#Ranchera_Popular    playlist_url = 'https://www.youtube.com/playlist?list=PLhxNyMmTLzozwUbjuX3Nff0TXmujRVzCI'
#Salsa_Bailable    playlist_url = 'https://www.youtube.com/playlist?list=PLhxNyMmTLzoydTd8FrFoH-K2OP-V_BWt2'
#Rock    playlist_url = 'https://www.youtube.com/playlist?list=PLhxNyMmTLzoy1CPBxjjIYVxz_WX7oPfLE'
#Rock_Latino    playlist_url = 'https://www.youtube.com/playlist?list=PLhxNyMmTLzoxNaacoZ5Rr8hOWtDOWFmIl'

    
    # Carpeta donde se guardarán los MP3
    carpeta_destino = 'C:/Users/yeiso/Desktop/Carpetas/Proyectos/Python_Yeison/Merengue'
    os.makedirs(carpeta_destino, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'extract_flat': True,
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)
        video_urls = [entry['url'] for entry in playlist_info['entries']]

    for url in video_urls:
        descargar_y_convertir(url, carpeta_destino)

if __name__ == '__main__':
    main()

