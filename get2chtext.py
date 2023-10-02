import requests
from bs4 import BeautifulSoup
import sys
import re
from bs4 import BeautifulSoup

def split_reply_text(element_text):
    id_pattern = re.compile(r"(\d+).+?", re.MULTILINE)
    reply_pattern = re.compile(r">>(\d+)", re.MULTILINE)

    header_match = id_pattern.search(element_text)
    reply_matches = reply_pattern.finditer(element_text)
    prev_end = 0
    elements = []
    tmp="";
    for i,match in enumerate(reply_matches):
        start, end = match.span()
        if i==0:
            tmp=element_text[prev_end:start]
        else:
            elements.append(tmp+element_text[prev_end:start])
        prev_end = start

    elements.append(tmp+element_text[prev_end:])
    return elements

def reorder_elements_based_on_reply(text_elements):
    ordered_elements = []
    reply_dict = {}
    id_pattern = re.compile(r"(\d+).+?", re.MULTILINE)
    reply_pattern = re.compile(r">>(\d+)", re.MULTILINE)

    for element_text in text_elements:
        #element_text = element.get_text()
        splitted_texts = split_reply_text(element_text)

        for text in splitted_texts:
            id_match = id_pattern.search(text)
            reply_match = reply_pattern.search(text)
            element_id = int(id_match.group(1)) if id_match else None
            reply_to_id = int(reply_match.group(1)) if reply_match else None

            if reply_to_id:
                if reply_to_id not in reply_dict:
                    reply_dict[reply_to_id] = [text]
                else:
                    reply_dict[reply_to_id].append(text)
            else:
                ordered_elements.append(text)

    result = []
    for element_text in ordered_elements:
        id_match = id_pattern.search(element_text)
        element_id = int(id_match.group(1)) if id_match else None
        result.append(element_text)
        if element_id in reply_dict:
            result.extend(reply_dict[element_id])

    return result







def save_text_from_url(url, output_file,output_file2):
    # URLからHTMLを取得
    response = requests.get(url)
    # HTMLを解析してテキストを抽出
    soup = BeautifulSoup(response.content, "html.parser")
    #with open("proj1/a.txt", "w", encoding="utf-8") as f:
    #    
    #    f.write(soup.text)
    #    f.write("\n")
    soup.text.replace(" ","")
    #text_elements = soup.find_all(lambda tag: tag.has_attr("class") and "res_body" in " ".join(tag["class"]))#alfalfaモザイク
    #text_elements = soup.find_all(lambda tag: tag.has_attr("class") and "post" in " ".join(tag["class"]))
    #text_elements = soup.find_all(lambda tag: tag.has_attr("class") and "post" in " ".join(tag["class"]))
    
    # dtタグとddタグのテキストを取得
    
    text_elements = soup.find_all(lambda tag: tag.has_attr("class") and "thread" in " ".join(tag["class"]))
    print(len(text_elements))
    print(text_elements[0].get_text())
    text_elements=text_elements[0].get_text().replace(" ","").split("\n")
    
    formatted_data = []

    for text in text_elements:
        date_match = re.search(r'\d{4}/\d{2}/\d{2}\([月火水木金土日]\)', text)
        time_id_match = re.search(r'\d{2}:\d{2}:\d{2}\.\d{2}ID:.{9}', text)
        
        if date_match and time_id_match:
            date_end = date_match.end()
            time_id_end = time_id_match.end()
            
            new_text = text[:date_end] + '\n' + text[date_end:time_id_end] + '\n' + text[time_id_end:]
            formatted_data.append(new_text)
        else:
            formatted_data.append(text)
    print(formatted_data)
    text_elements = reorder_elements_based_on_reply(formatted_data)
    with open(output_file, "w", encoding="utf-8") as f:
        for element in text_elements:
            text=element.replace(" ","\n")
            while text.find("\n\n")!=-1:
                text=text.replace("\n\n","\n")
            f.write(text[:len(text)])
            f.write("|\n")
    with open(output_file2, "w", encoding="utf-8") as f:
        for element in text_elements:  # 並べ替えられた要素を使用してください
            text=element.replace(" ","\n")
            while text.find("\n\n")!=-1:
                text=text.replace("\n\n","\n")
            pattern = r">>\d+(\n)?"
            text = re.sub(pattern, "", text)
            lines = text.split("\n")
            filtered_lines = lines[2:]  # 上の2行を省く
            text = "\n".join(filtered_lines)
            f.write(text[:len(text)])
            f.write("|\n")
    print(f"テキストが {output_file} に保存されました。")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py URL output_file")
    else:
        url = sys.argv[1]
        dir_path=sys.argv[2]
        if len(sys.argv)>4:
            output_file = dir_path+"/"+sys.argv[3]
            output_file2 = dir_path+"/"+sys.argv[4]
        else:
            output_file=dir_path+"/input.txt"
            output_file2=dir_path+"/kana.txt"
            
        save_text_from_url(url, output_file,output_file2)
