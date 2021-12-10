from pytube import YouTube

filePath = input("What should the files path be?\n")
link = input('What is the URL of your video?\n')

try:
    yt = YouTube(link)
except:
    print('Connection error')
    exit()

mp4files = yt.filer('mp4')

yt.set_filename(yt.title)

dVideo = yt.get(mp4files[-1].extension, mp4files[-1].resolution)

try:
    dVideo.download(filePath)
except:
    print('Error')

print('Done')