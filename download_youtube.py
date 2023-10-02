from pytube import YouTube

def download_youtube_video(url, output_directory):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()
    video.download(output_directory)

url = "https://youtu.be/CIa_gxllYj8"
output_directory = "."

download_youtube_video(url, output_directory)
