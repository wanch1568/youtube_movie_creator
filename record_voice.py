import sounddevice as sd
import numpy as np
import wave
import sys
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import soundcard as sc


def detect_audio_starts(audio_file, min_silence_len=700, silence_thresh=-40):
    audio = AudioSegment.from_file(audio_file, format="wav")
    nonsilent_ranges = detect_nonsilent(audio, min_silence_len, silence_thresh)
    
    start_times = []
    for start, end in nonsilent_ranges:
        start_times.append(start)
    
    return start_times
def record_audio(duration, dir_path, sample_rate=44100):
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    
    sd.wait()

    with wave.open(dir_path+"/voice.wav", 'wb') as file:
        file.setnchannels(2)
        file.setsampwidth(2)
        file.setframerate(sample_rate)
        file.writeframes(recording.tobytes())
    
    start_times = detect_audio_starts(dir_path+"/voice.wav")
    with open(dir_path+"/start_time.txt", "w") as f:
        start_times_in_seconds = [str(start_time / 1000) for start_time in start_times]
        f.write("|".join(start_times_in_seconds))

def record_internal_audio(duration, dir_path, sample_rate=44100):
    # Get the default speaker
    speaker = sc.default_speaker()
    device_index=1
    # Get the default microphone
    microphone = sc.default_microphone()
    print(microphone)
    # Record the internal audio
    with speaker.recorder(samplerate=sample_rate) as recorder, microphone.player(samplerate=sample_rate) as player:
        for _ in range(int(duration * sample_rate // 1024)):
            data = recorder.record(1024)
            player.play(data)

            with wave.open(dir_path + "/voice.wav", "wb") as file:
                file.setnchannels(2)
                file.setsampwidth(2)
                file.setframerate(sample_rate)
                file.writeframes(data.tobytes())
    start_times = detect_audio_starts(dir_path+"/voice.wav")
    with open(dir_path+"/start_time.txt", "w") as f:
        start_times_in_seconds = [str(start_time / 1000) for start_time in start_times]
        f.write("|".join(start_times_in_seconds))
duration=float(sys.argv[1])
dir_path=sys.argv[2]
record_audio(duration,dir_path)