import sys
import random
import subprocess
from time import sleep, time

if len(sys.argv) < 2:
    print("Please provide the input text file name as an argument.")
    sys.exit(1)

dir_path = sys.argv[1]

with open(dir_path+"/kana.txt", "r", encoding="utf-8") as f:
    content = f.read()
    chunks = content.split("|")

timestamps = []

start_time = time()

# タイムスタンプのファイルをクリアする
with open("timestamps.txt", "w") as f:
    f.write("")

for chunk in chunks:
    voice = random.choice([1, 2, 5, 7])
    subprocess.run(["python", "bouyomi.py", chunk, "-c", str(voice)])
    sleep(1)
