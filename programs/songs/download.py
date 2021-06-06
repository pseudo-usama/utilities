import os

from tinydb import TinyDB
import youtube_dl


INDEXED_DIR = 'f:/songs'
TEMP_DIR = 'f:/songs/temp'


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


def download_songs_from_tuple(songs):
    db = TinyDB('db.json')

    for song in songs:
        video_file_name = download_song(song['link'], TEMP_DIR)
        audio_file_name = f'{TEMP_DIR}/{song["file"]}'
        video_to_mp3(video_file_name, audio_file_name)

        os.rename(audio_file_name, f'{INDEXED_DIR}/{song["file"]}')
        os.remove(video_file_name)

        db.insert(song)


def download_songs_from_db():
    # TODO: Have to implement this
    pass


# Sample tamplate
SONGS = (
    {
        'name': 'name',
        'file': 'file.mp3',
        'link': 'link',
        'languages': ['language'],
        'artists': ['singer name'],
        'movie': {
            'name': 'movie name',
            'industry': 'hollywood',
            'cast': ['actors']
        },
        'tags': ['some tag'],
    }
)


download_songs_from_tuple(SONGS)
