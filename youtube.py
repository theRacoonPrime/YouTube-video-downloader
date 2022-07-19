from pytube import YouTube
import os

link = "https://www.youtube.com/watch?v=QITxerVv76Q"
direction = 'Users/andrey/Downloads'


def downloadYouTube(video_link, direction):

    yt = YouTube(video_link)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(direction):
        os.makedirs(direction)
    yt.download(direction)


downloadYouTube(link, direction)