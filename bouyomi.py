import socket
import struct
import argparse
import random
import time

class Bouyomi:
    DEFAULT_BOUYOMI_HOST = "localhost"
    DEFAULT_BOUYOMI_PORT = 50001

    def __init__(self, host=DEFAULT_BOUYOMI_HOST, port=DEFAULT_BOUYOMI_PORT):
        self.host = host
        self.port = port

    def clear(self):
        self.command(self.host, self.port, 64)

    def pause(self):
        self.command(self.host, self.port, 16)

    def resume(self):
        self.command(self.host, self.port, 32)

    def skip(self):
        self.command(self.host, self.port, 48)

    def talk(self, message, volume=-1, speed=-1, tone=-1, voice=0):
        if message[0]=='-':
            print("イッチ")
            voice=2
            message=message[1:]
        self.talk_cmd(self.host, self.port, volume, speed, tone, voice, message)

    def command(self, host, port, command):
        data = struct.pack("<H", command)
        self.send(host, port, data)

    def send(self, host, port, data):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect((host, port))
                sock.sendall(data)
        except ConnectionRefusedError:
            print("接続できませんでした")

    def talk_cmd(self, host, port, volume, speed, tone, voice, message):
        message_data = message.encode("utf-8")
        length = len(message_data)
        data = struct.pack("<HHHHHHI", 1, speed, tone, volume, voice, 0, length)
        data += message_data
        self.send(host, port, data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Bouyomi command-line interface")
    parser.add_argument("message", help="Text to be spoken by Bouyomi-chan")
    parser.add_argument("-v", "--volume", type=int, default=100, help="Volume (0-100, default=-1)")
    parser.add_argument("-s", "--speed", type=int, default=120, help="Speed (50-300, default=-1)")
    parser.add_argument("-t", "--tone", type=int, default=100, help="Tone (50-200, default=-1)")
    parser.add_argument("-c", "--voice", type=int, default=random.choice([1, 2, 3, 4 ,5, 7]), help="Voice (1-8, default=0)")

    args = parser.parse_args()

    bouyomi = Bouyomi()

    # 読み上げ開始時のタイムスタンプを取得
    start_time = time.time()

    bouyomi.talk(args.message, volume=args.volume, speed=args.speed, tone=args.tone, voice=args.voice)
    # タイムスタンプをテキストファイルに書き込む
    with open("timestamps.txt", "a") as f:
        f.write(f"{start_time}\n")