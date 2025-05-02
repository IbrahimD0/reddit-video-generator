from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy import *
import textwrap
# Path to your audio and SRT files
audio_file = 'test.wav'
srt_file = 'srtFilename1.srt'
background_file = 'video.mp4'
# Load the audio file
audio = AudioFileClip(audio_file)
audio = audio.subclipped(0,(min(59, audio.duration))) 

video = VideoFileClip(background_file)
video = video.cropped(width=1080, height=1920, x_center=video.w / 2)
video = video.subclipped(0,(min(59, audio.duration)))




# Load subtitles from the SRT file
generator = lambda txt: TextClip(
    font = "Roboto\Roboto-Italic-VariableFont_wdth,wght.ttf",
    text = textwrap.fill(txt, width=50),
    font_size = 64,
    color= 'white',
    stroke_color="black",
    stroke_width=8,
    method = 'caption',
    text_align = 'center',
    size = (800, None)
)
subtitles = SubtitlesClip(srt_file, make_textclip=generator)
subtitles = subtitles.with_duration(audio.duration)

# Ensure subtitles are positioned slightly above the bottom of the vertical frame
video_with_subtitles = CompositeVideoClip([
    video,
    subtitles.with_position(('center','center'))
])

# Set the audio of the video to match the audio file
video_with_subtitles = video_with_subtitles.with_audio(audio)

# Output the final video file
video_with_subtitles.write_videofile('output_video.mp4')