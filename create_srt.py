from datetime import timedelta
import os
import whisper

def transcribe_audio(path):
    model = whisper.load_model("base") 
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio=path)
    segments = transcribe['segments']

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"

        
        with open('srtFilename1.srt', 'a', encoding='utf-8') as srtFile:
            srtFile.write(segment)
transcribe_audio('test.wav')