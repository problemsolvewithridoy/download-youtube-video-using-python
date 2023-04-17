from pytube import YouTube

url = input("please enter your youtube video link: ")
yt = YouTube(url)

video = yt.streams.filter(progressive= True, file_extension= "mp4").order_by("resolution").desc().first()
video.download()
print("Congratulations, your download is completed")