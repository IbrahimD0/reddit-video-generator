from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save
import os
import srt
import datetime
from create_text import fetch_reddit_post

load_dotenv()

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

title, body = fetch_reddit_post()
story = title + " " + body

response = client.generate(
    voice="UgBBYS2sOqTuMpoF3BR0",
    text=story,
    model="eleven_multilingual_v2"
)

audio_file_path = "test.wav"
save(response, audio_file_path)


