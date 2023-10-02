from PIL import Image, ImageDraw, ImageFont
import random
import sys

from PIL import Image, ImageDraw, ImageFont
import string




def create_transparent_text_image(text, font_path, font_size, output_path, text_color=(255,0,0), outline_color=(255,255,255)):
    # フォントの設定
    font = ImageFont.truetype(font_path, font_size)

    # テキストを行ごとに分割
    lines = text.split('\n')
    # 各行のテキストサイズを取得し、最大の幅と全体の高さを計算
    max_width = 0
    total_height = 0
    line_sizes = []
    for line in lines:
        text_bbox = font.getbbox(line)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        max_width = max(max_width, text_width)
        total_height += text_height
        line_sizes.append((text_width, text_height))

    # 透明な画像を作成
    image = Image.new("RGBA", (max_width + 10, total_height + 10 + 5 * (len(lines) - 1)), (0, 0, 0, 0))

    # 描画オブジェクトを作成
    draw = ImageDraw.Draw(image)

    # 各行のテキストを描画
    y_offset = 5
    for i, line in enumerate(lines):
        text_width, text_height = line_sizes[i]

        # テキストの縁を描画
        for x_offset in range(-1, 2):
            for y in range(-1, 2):
                draw.text((5 + x_offset, y_offset + y), line, font=font, fill=outline_color)

        # テキストを描画
        draw.text((5, y_offset), line, font=font, fill=text_color)

        # 次の行へのオフセットを更新
        y_offset += text_height + 5

    # 画像を保存
    image.save(output_path)



def wrap_text(text, font, max_pixel_width):
    lines = []

    for line in text.split("\n"):
        current_line = ""
        for char in line:
            new_line = current_line + char
            text_bbox = font.getbbox(new_line)
            text_width = text_bbox[2] - text_bbox[0]
            if text_width > max_pixel_width:
                lines.append(current_line)
                current_line = char
            else:
                current_line = new_line
        lines.append(current_line)

    return "\n".join(lines)





def add_text_to_image(image_path, text, output_path, font_path=None, font_size=30, text_color=(255, 255, 255), line_length=23):
    # テキストを折り返す
    texts=text.split("|\n")
    cnt=0
    for tx in texts:
        image_path = random.choice(images)
        #if cnt!=1:
        if tx[0]=='-':
            tx=tx[1:]
            text_color=(0,0,255)
        else:
            text_color=(0,0,0)
        if cnt!=-1:
            font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default().font
            max_pixel_width = 1100

            wrapped_text = wrap_text(tx, font, max_pixel_width)
        # 画像を読み込む
        #if cnt>1:
        if cnt>-1:
            cnt+=1
            image = Image.open(image_path)

            # 描画オブジェクトを作成
            draw = ImageDraw.Draw(image)

            # フォントの設定
            if font_path:
                font = ImageFont.truetype(font_path, font_size)
            else:
                font = ImageFont.load_default().font

            # テキストサイズを取得
            text_bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

            # 画像サイズを取得
            image_width, image_height = image.size

            # 画像を拡張
            new_image = image.resize((text_width+50,text_height+20), Image.LANCZOS)

            # 描画オブジェクトを作成
            draw = ImageDraw.Draw(new_image)

            # テキストの位置を計算
            position = (30, 10)

            # テキストを描画
            draw.multiline_text(position, wrapped_text, fill=text_color, font=font)

            # 変更された画像を保存
            new_image.save(output_path+"/"+alp[(cnt//10)]+num[cnt%10]+"frame.png")
        else:
           create_transparent_text_image(tx, font_path, font_size, output_path+"/"+alp[(cnt//10)]+num[cnt%10]+"frame.png")
           cnt+=1
def add_title_to_image(image_path, text, output_path, font_path=None, font_size=30, text_color=(255, 255, 255), line_length=23):
    # テキストを折り返す
    texts=text.split("|\n")
    cnt=0
    for tx in texts:
        image_path = random.choice(images)
        #if cnt!=1:
        print(tx)
        if tx[0]=='-':
            print("blue")
            text_color=(0,0,255)
        else:
            text_color=(255,255,255)
        if cnt!=1:
            font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default().font
            max_pixel_width = 1100

            wrapped_text = wrap_text(tx, font, max_pixel_width)
        # 画像を読み込む
        #if cnt>1:
        if cnt>1:
            cnt+=1
            image = Image.open(image_path)

            # 描画オブジェクトを作成
            draw = ImageDraw.Draw(image)

            # フォントの設定
            if font_path:
                font = ImageFont.truetype(font_path, font_size)
            else:
                font = ImageFont.load_default().font

            # テキストサイズを取得
            text_bbox = draw.multiline_textbbox((0, 0), wrapped_text, font=font)
            text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

            # 画像サイズを取得
            image_width, image_height = image.size

            # 画像を拡張
            new_image = image.resize((text_width+50,text_height+20), Image.LANCZOS)

            # 描画オブジェクトを作成
            draw = ImageDraw.Draw(new_image)

            # テキストの位置を計算
            position = (30, 10)

            # テキストを描画
            
            draw.multiline_text(position, wrapped_text, fill=text_color, font=font)

            # 変更された画像を保存
            new_image.save(output_path+"/title"+alp[(cnt//10)]+num[cnt%10]+".png")
        else:
           create_transparent_text_image(tx, font_path, font_size, output_path+"/title"+alp[(cnt//10)]+num[cnt%10]+".png")
           cnt+=1
if __name__ == "__main__":
    alp = list(string.ascii_lowercase)
    num=["0","1","2","3","4","5","6","7","8","9"]
    dir_path=sys.argv[1]
    images=["frames/black.png","frames/orange.png","frames/yellow.png","frames/light_blue.png","frames/blue.png","frames/pink.png","frames/red.png","frames/green.png"]
    image_path = random.choice(images)  # 入力画像のパス
    if len(sys.argv) > 2:
        text_file_path = dir_path + "/" + sys.argv[2]
    else:
        text_file_path =dir_path+"/input.txt"  # テキストファイルのパス
    with open(text_file_path, "r", encoding="utf-8") as file:
        text = file.read()  # テキストファイルからテキストを読み込む
    output_path = dir_path  # 出力画像のパス
    font_path = "./azukifont121/azuki.ttf"  # フォントファイルのパス (Noneの場合はデフォルトフォントが使用されます)
    font_size = 30  # フォントサイズ
    text_color = (0, 0, 0)  # テキストの色 (R, G, B)
    if text_file_path==dir_path+"/input.txt":
        add_text_to_image(image_path, text, output_path, font_path, font_size, text_color)
    else:
        add_title_to_image(image_path, text, output_path, font_path, font_size, text_color)
