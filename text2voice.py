from google.cloud import texttospeech
import os

# Google CloudのAPIキーのパスを設定
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./ivory-partition-383306-3a9b4c5caf3e.json"

def text_to_speech(text_file, output_file):
    # クライアントを作成
    client = texttospeech.TextToSpeechClient()

    # テキストファイルを読み込む
    with open(text_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # 入力テキストを設定
    input_text = texttospeech.SynthesisInput(text=text)

    # 音声設定を選択（日本語、女性の声）
    voice = texttospeech.VoiceSelectionParams(
        language_code="ja-JP",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # 音声ファイルのタイプを指定
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # テキストを音声に変換
    response = client.synthesize_speech(
        input=input_text,
        voice=voice,
        audio_config=audio_config
    )

    # 音声ファイルを保存
    with open(output_file, "wb") as out:
        out.write(response.audio_content)

    print(f"音声ファイルが {output_file} に保存されました。")

# 入力テキストファイルと出力音声ファイルを指定
text_file = "out2.txt"
output_file = "output_speech1.mp3"

# 関数を実行
text_to_speech(text_file, output_file)
