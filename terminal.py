from tkinter import Tk as tk
from pytube import YouTube

filePath = input("What should the files path be?\n")
link = input('What is the URL of your video?\n')

try:
    yt = YouTube(link)
except:
    print('Connection error')
    exit()

dVideo = yt.streams.filter(progressive = True, file_extension = 'mp4').first()

# try:
dVideo.download(output_path = filePath, filename = yt.title)
# except:
#     print('Download error')

print('Done')

#https://www.youtube.com/watch?v=hsOaJ5gHhu8