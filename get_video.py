from pytubefix import YouTube

video_url = 'https://www.youtube.com/shorts/1nIGWHLMsFA'

yt = YouTube(video_url)

stream = yt.streams.filter(adaptive=True).filter(mime_type='video/webm').first().download(filename='video.mp4')

print("Download completed!")
