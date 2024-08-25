import os
import yt_dlp
from pydub import AudioSegment

def archivo_existe(nombre_archivo, carpeta_destino):
    """Verifica si el archivo MP3 ya existe en la carpeta de destino."""
    return os.path.isfile(os.path.join(carpeta_destino, nombre_archivo))

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
            nombre_archivo_mp3 = os.path.splitext(os.path.basename(archivo_video))[0] + '.mp3'
            archivo_mp3 = os.path.join(carpeta_destino, nombre_archivo_mp3)

            if archivo_existe(nombre_archivo_mp3, carpeta_destino):
                print(f"El archivo {nombre_archivo_mp3} ya existe. Saltando descarga.")
                return

            # Convertir el archivo descargado a MP3
            audio = AudioSegment.from_file(archivo_video)
            audio.export(archivo_mp3, format='mp3')

            # Eliminar el archivo de video descargado
            os.remove(archivo_video)

            print(f"Descargado y convertido: {archivo_mp3}")
    except Exception as e:
        print(f"Error al procesar {url}: {e}")

def main():
    # URL del video
    video_url = 'https://www.youtube.com/watch?v=LII8Nfu1sOE'
    
    # Carpeta donde se guardarán los MP3
    carpeta_destino = 'C:/Users/yeiso/Desktop/Carpetas/Proyectos/Python_Yeison/Solas'
    os.makedirs(carpeta_destino, exist_ok=True)

    descargar_y_convertir(video_url, carpeta_destino)

if __name__ == '__main__':
    main()