from moviepy.editor import VideoFileClip, concatenate_videoclips

# 連結する動画のリスト
input_videos = ['mov.mp4']

# 連結後の動画のファイル名
output_video = 'connected.mp4'
# 動画ファイルを読み込み、VideoFileClipオブジェクトのリストを作成
video_clips = [VideoFileClip(video) for video in input_videos]

# 動画を連結
final_clip = concatenate_videoclips(video_clips)

# 連結された動画をファイルに書き出し
final_clip.write_videofile(output_video)

# リソースを解放
for clip in video_clips:
    clip.close()
final_clip.close()
