import subprocess
import sys
import time

dir_path = sys.argv[1]
duration = sys.argv[2]
#bgm_path = sys.argv[3]
start_from_video_creation = len(sys.argv) >= 4 and sys.argv[3] == '1'

if not start_from_video_creation:
    print("Creating images")
    create_img_process = subprocess.Popen(["python", "create_comment_image.py", dir_path])
    create_img_process.wait()

    # run_bouyomi.py と record_voice.py の両方のプロセスを開始
    print("start_recording")
    record_voice_process = subprocess.Popen(["python", "record_voice.py", duration, dir_path])
    time.sleep(1)
    print("Start bouyomityan")
    run_bouyomi_process = subprocess.Popen(["python", "run_bouyomi.py", dir_path])

    # 両方のプロセスが終了するのを待つ
    print("Recording....")
    run_bouyomi_process.wait()
    record_voice_process.wait()

print("Creating video")
create_movie = subprocess.Popen(["python", "embedcomment.py", dir_path, duration])
create_movie.wait()
create_complete_movie_process = subprocess.Popen(["python", "combine_material.py", dir_path])
create_complete_movie_process.wait()
