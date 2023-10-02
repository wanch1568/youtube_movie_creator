from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip, concatenate_audioclips
import sys
def create_video_with_audio(video_file, narration_file, output_file):
    # 動画を読み込む
    video_clip = VideoFileClip(video_file)

    # BGMとナレーション音声を読み込む
    #bgm_audio = AudioFileClip(bgm_file)
    narration_audio = AudioFileClip(narration_file)

    # BGM音声を動画の長さに合わせてループさせる
    #bgm_loops = video_clip.duration // bgm_audio.duration + 1
    #bgm_audio = concatenate_audioclips([bgm_audio] * int(bgm_loops))
    #bgm_audio = bgm_audio.subclip(0, video_clip.duration)

    #bgm_audio = bgm_audio.volumex(bgm_volume)
    narration_audio = narration_audio.volumex(narration_volume)
    # BGMとナレーション音声を合成
    #final_audio = CompositeAudioClip([bgm_audio, narration_audio])

    # 動画に合成音声をセット
    #video_clip = video_clip.set_audio(final_audio)
    video_clip = video_clip.set_audio(narration_audio)

    # 結果をファイルに書き込む
    video_clip.write_videofile(output_file)

    # リソースを解放
    video_clip.close()
    #bgm_audio.close()
    narration_audio.close()


# 入力ファイルと出力ファイルを指定
dir_path=sys.argv[1]
video_file = dir_path+"/output_video.mp4"
#bgm_file = sys.argv[2]
narration_file = dir_path+"/voice.wav"
output_file = dir_path+"/complete_video.mp4"

#bgm_volume = 0.8
narration_volume = 2.0
# 関数を実行
create_video_with_audio(video_file, narration_file, output_file)
