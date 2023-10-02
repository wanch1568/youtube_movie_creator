import sys
from moviepy.editor import *
from pydub import AudioSegment

def load_text_segments(text_file_path, separator="|"):
    with open(text_file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return text.split(separator)

def create_video(bg_image_path, bgm_path, voice_path, text_file_path, output_path):
    fps = 24
    bg_image = ImageClip(bg_image_path).set_fps(fps)

    voice = AudioFileClip(voice_path)
    voice_duration = voice.duration

    bgm = AudioFileClip(bgm_path)
    bgm_duration = voice_duration + 4

    bgm = bgm.volumex(0.5)
    bgm = bgm.subclip(0, bgm_duration)
    bgm = bgm.fx(afx.audio_loop, duration=bgm_duration)

    final_audio = CompositeAudioClip([bgm, voice.set_start(2)])

    text_segments = load_text_segments(text_file_path)
    text_timings = [voice_duration * i / len(text_segments) for i in range(len(text_segments))]

    text_clips = []
    for i, text in enumerate(text_segments):
        text_clip = TextClip(text.strip(), fontsize=30, color="white", size=bg_image.size).set_start(text_timings[i]).set_duration(text_timings[i + 1] - text_timings[i] if i + 1 < len(text_segments) else bgm_duration - text_timings[i])
        text_clips.append(text_clip)

    final_video = CompositeVideoClip([bg_image] + text_clips).set_duration(bgm_duration).set_audio(final_audio)
    final_video.write_videofile(output_path, fps=fps)

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python create_video.py <bg_image_path> <bgm_path> <voice_path> <text_file_path> <output_path>")
        sys.exit(1)

    bg_image_path = sys.argv[1]
    bgm_path = sys.argv[2]
    voice_path = sys.argv[3]
    text_file_path = sys.argv[4]
    output_path = sys.argv[5]

    create_video(bg_image_path, bgm_path, voice_path, text_file_path, output_path)
