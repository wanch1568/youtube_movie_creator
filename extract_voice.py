import os
from moviepy.editor import *
from google.cloud import speech_v1p1beta1 as speech
import io

def trim_video(input_video, start_time, end_time, output_video):
    video = VideoFileClip(input_video)
    trimmed_video = video.subclip(start_time, end_time)
    trimmed_video.write_videofile(output_video)

def transcribe_audio_to_text_file(audio_path, text_file, credentials):
    client = speech.SpeechClient.from_service_account_file(credentials)

    with io.open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="ja-JP",
    )

    response = client.recognize(config=config, audio=audio)

    with open(text_file, "w") as f:
        for result in response.results:
            f.write(result.alternatives[0].transcript + "\n")

def extract_audio_from_video(input_video, output_audio):
    video = VideoFileClip(input_video)
    video.audio.write_audiofile(output_audio)

input_video = "movie1.mp4"
start_time = 0  # 開始時間（秒）
end_time = 30  # 終了時間（秒）
output_video = "trimmed_video.mp4"
output_audio = "trimmed_audio.wav"
text_file = "transcript.txt"
credentials = "path/to/your_google_application_credentials.json"

trim_video(input_video, start_time, end_time, output_video)
extract_audio_from_video(output_video, output_audio)
transcribe_audio_to_text_file(output_audio, text_file, credentials)

print(f"Trimmed video saved as: {output_video}")
print(f"Transcript saved as: {text_file}")
