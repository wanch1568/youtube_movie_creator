from moviepy.editor import VideoFileClip, ImageClip, CompositeVideoClip

def arrange_images_vertically(image_clips):
    y_position = 100
    for idx, img_clip in enumerate(image_clips):
        img_clip = img_clip.set_position((100, y_position))
        y_position += img_clip.size[1] + 20
        image_clips[idx] = img_clip
    return image_clips

def insert_images_in_video(video_path, images_info):
    video = VideoFileClip(video_path)
    video=video.subclip(0,video.duration/3)
    image_clips = []

    for img_info in images_info:
        img_path, start_time, end_time = img_info
        img_clip = ImageClip(img_path).set_start(start_time).set_end(end_time)
        image_clips.append(img_clip)

    arranged_image_clips = arrange_images_vertically(image_clips)
    composite = CompositeVideoClip([video] + arranged_image_clips)
    output_video_path = "output_video.mp4"
    composite.write_videofile(output_video_path)

video_path = "movie_raw.mp4"
images_info = [
    ["11frame.png", 1,20],
    ["12frame.png", 3, 20],
    ["13frame.png", 5, 20],
    ["14frame.png", 7, 20],
    ["15frame.png", 9, 20],
    ["16frame.png", 11, 20],
    # ... 他の画像
]
images=[]
last=[]
for i,img_info in enumerate(images_info):
    if i>3:
        images.pop(0)
    images.append(img_info)
    if i!=(len(images_info)-1):
        for img in images:
            img[1]=img[-1][1]
            img[2]=images_info[i+1][1]
            last.append(img)
print(last)
insert_images_in_video(video_path, last)
