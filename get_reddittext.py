import requests
from bs4 import BeautifulSoup
import sys

def save_text_from_url(url, output_file):
    # URLからHTMLを取得
    response = requests.get(url)
    # HTMLを解析してテキストを抽出
    soup = BeautifulSoup(response.content, "html.parser")
    #with open("proj1/a.txt", "w", encoding="utf-8") as f:
    #    
    #    f.write(soup.text)
    #    f.write("\n")
    print(soup.text)
    text_elements =soup.find_all("p")

    # テキストをファイルに保存
    with open(output_file, "w", encoding="utf-8") as f:
        for element in text_elements:
            f.write(element.get_text())
            f.write("\n")

    print(f"テキストが {output_file} に保存されました。")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py URL output_file")
    else:
        url = sys.argv[1]
        output_file = sys.argv[2]
        save_text_from_url(url, output_file)
