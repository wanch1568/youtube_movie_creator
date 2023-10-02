import re
import sys

def extract_text_between_tags(text, start_tag='<p>', end_tag='</p>'):
    pattern = re.compile(f'{start_tag}(.*?){end_tag}', re.DOTALL)
    matches = pattern.findall(text)
    return matches

def write_list_to_file(output_file_path, text_list):
    with open(output_file_path, "w", encoding="utf-8") as file:
        for item in text_list:
            file.write(item)

if __name__ == "__main__":
    input_text_file_path = sys.argv[1]+"/"+sys.argv[2]
    with open(input_text_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    extracted_texts = extract_text_between_tags(text)

    output_file_path = sys.argv[1]+"/"+sys.argv[3]
    write_list_to_file(output_file_path, extracted_texts)
