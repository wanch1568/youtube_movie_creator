import pykakasi
import sys

def convert_kanji_to_hiragana(input_file, output_file):
    # pykakasiの設定
    kakasi = pykakasi.kakasi()

    # 入力ファイルを読み込み、漢字をひらがなに変換
    with open(input_file, "r", encoding="utf-8") as f:
        input_text = '|'.join(f.read().splitlines())
        print(input_text)
        converted_text = kakasi.convert(input_text)
        converted_text = "".join([entry['hira'] for entry in converted_text])

    # 変換されたテキストを出力ファイルに保存
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(converted_text)

    print(f"変換が完了し、 {output_file} に保存されました。")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_kanji_to_hiragana(input_file, output_file)
