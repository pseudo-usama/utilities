import os
import tempfile
import youtube_dl


SONGS = (
    {
        'name': 'Hum Pagal Nahin Hai',
        'file': 'Hum Pagal Nahin Hai.mp3',
        'link': 'https://www.youtube.com/watch?v=___hMJ3toxM',
        'languages': ['hindi'],
        'movie': 'Humshakals',
        'tags': ['comedy', 'hindi', 'bollywood'],
    },
)



def download_song(link, path):
    ops = {
        'format': 'best',
        'outtmpl': path + r'//%(uploader)s%(title)s.%(ext)s'
    }
    ytdl = youtube_dl.YoutubeDL(ops)
    info = ytdl.extract_info(link, download=True)

    file_name = ytdl.prepare_filename(info)
    return file_name

def video_to_mp3(file_name, out_file_name):
    os.system(f'ffmpeg -i "{file_name}" "{out_file_name}"')


def songs():
    temp_dir = tempfile.mkdtemp()
    
    for song in SONGS:
        file_name = download_song(song['link'], temp_dir)
        video_to_mp3(file_name, f'{temp_dir}//{song["file"]}')
