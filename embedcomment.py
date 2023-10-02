from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip
import os
import glob
import sys
import random

def load_image_paths(directory):
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.tiff')
    image_paths = []
    for ext in image_extensions:
        image_paths.extend(glob.glob(os.path.join(directory, f'*{ext}')))
    return image_paths

def load_start_times(text_file):
    with open(text_file, 'r') as file:
        start_times = file.read().split('|')
    return [float(time.strip()) for time in start_times if time.strip()]


def create_images_info(directory, text_file):
    image_paths = load_image_paths(directory)
    people_imgs = load_image_paths("illust/2chmin")
    start_times = load_start_times(text_file)
    images_info = []
    people_info = []

    for i, img_path in enumerate(image_paths):
        if i < len(start_times) - 1:
            start_time = start_times[i]
            end_time = start_times[i + 1]
            images_info.append([img_path, start_time, end_time])
        elif i==len(start_times)-1:
            start_time = start_times[i]
            end_time = start_times[i]+2
            images_info.append([img_path, start_time, end_time])

        if i < len(start_times) - 1:
            start_time = start_times[i]
            end_time = start_times[i + 1]
            people_info.append([random.choice(people_imgs), start_time, end_time])

    return images_info, people_info

def arrange_images_vertically(image_clips, start_times, people_images_info):
    y_position = 50
    idx = 0
    while idx < len(start_times) - 1:
        current_start_time = start_times[idx]
        same_start_times = [idx]

        # 同じstart_timesの値を持つimg_clipsのインデックスを見つける
        for next_idx in range(idx + 1, len(start_times)):
            if start_times[next_idx] == current_start_time:
                same_start_times.append(next_idx)
            else:
                break

        # 同じstart_timesの値を持つimg_clipsの縦幅の合計を計算
        total_height = sum([image_clips[i].h for i in same_start_times])

        # 合計縦幅が600pxを下回るまで、img_clipsから要素を削除
        while total_height > 550:
            del image_clips[same_start_times[0]]
            del start_times[same_start_times[0]]
            same_start_times.pop(0)
            same_start_times = [i - 1 for i in same_start_times]
            total_height = sum([image_clips[i].h for i in same_start_times])

        idx = same_start_times[-1] + 1
    for idx, img_clip in enumerate(image_clips):
        if idx > 0 and start_times[idx] != start_times[idx - 1]:
            y_position = 50
        img_clip = img_clip.set_position((100, y_position))
        y_position += img_clip.size[1] + 20
        image_clips[idx] = img_clip

    for p_idx, p_img_clip in enumerate(people_images_info):
        p_img_clip = p_img_clip.set_position((900, 300))
        p_img_clip=p_img_clip.resize(1.3)
        people_images_info[p_idx] = p_img_clip

    return image_clips, people_images_info

def insert_images_in_video(video_path, images_info, duration, people_images_info):
    video = VideoFileClip(video_path)
    video = video.subclip(0, duration+5)
    image_clips = []
    people_image_clips = []
    start_times = []
    for p_img_info in people_images_info:
        p_img_path, p_start_time, p_end_time = p_img_info
        p_img_clip = ImageClip(p_img_path).set_start(p_start_time).set_end(p_end_time)
        people_image_clips.append(p_img_clip)
    for img_info in images_info:
        img_path, start_time, end_time = img_info
        img_clip = ImageClip(img_path).set_start(start_time).set_end(end_time)
        image_clips.append(img_clip)
        start_times.append(start_time)

    arranged_people_clips,arranged_image_clips = arrange_images_vertically(image_clips, start_times, people_image_clips)
    composite = CompositeVideoClip([video] + arranged_image_clips + arranged_people_clips)
    output_video_path = directory+"/output_video.mp4"
    composite.write_videofile(output_video_path)

if __name__ == "__main__":
    video_path = "movie_raw.mp4"
    directory = sys.argv[1]  # 画像ファイルが含まれるディレクトリ
    text_file = sys.argv[1]+"/start_time.txt"  # 開始時間が記載されたテキストファイル
    duration=float(sys.argv[2])
    images_info,people_images_info = create_images_info(directory, text_file)
    images = []
    last = []
    for i, img_info in enumerate(images_info):
        if i > 5:
            images.pop(0)
        images.append(img_info)
        for img in images:
            img_copy = img.copy()
            img_copy[1] = images[-1][1]
            if i != (len(images_info) - 1):
                img_copy[2] = images_info[i + 1][1]
            else:
                img_copy[2] = img_copy[1]+5
            last.append(img_copy)
    insert_images_in_video(video_path, last,duration,people_images_info)