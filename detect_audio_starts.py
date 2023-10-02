from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import sys

def detect_audio_starts(audio_file, min_silence_len=700, silence_thresh=-40):
    audio = AudioSegment.from_file(audio_file, format="wav")
    nonsilent_ranges = detect_nonsilent(audio, min_silence_len, silence_thresh)
    
    start_times = []
    for start, end in nonsilent_ranges:
        start_times.append(start)
    
    return start_times

audio_file = sys.argv[1]+"/voice.wav"
start_times = detect_audio_starts(audio_file)
with open("timestamps.txt", "w") as f:
    start_times_in_seconds = [str(start_time / 1000) for start_time in start_times]
    f.write("|".join(start_times_in_seconds)+"|")