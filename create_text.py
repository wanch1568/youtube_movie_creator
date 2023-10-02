from PIL import Image, ImageDraw, ImageFont
import sys
def create_transparent_text_image(text, font_path, font_size, output_path,text_color, outline_color,  vertical_scale=1.5):
    # フォントの設定
    font = ImageFont.truetype(font_path, font_size)

    # テキストサイズを取得
    text_bbox = font.getbbox(text)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # 透明な画像を作成
    image = Image.new("RGBA", (text_width + 10, int(text_height * vertical_scale) + 10), (0, 0, 0, 0))

    # 描画オブジェクトを作成
    draw = ImageDraw.Draw(image)

    # テキストの縁を描画
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            draw.text((5 + x_offset, 5 + y_offset), text, font=font, fill=outline_color)

    # テキストを描画
    draw.text((5, 5), text, font=font, fill=text_color)

    # 画像を保存
    image.save(output_path)
if __name__ == "__main__": 
    # 入力画像のパス
    text = sys.argv[1]  # テキストファイルからテキストを読み込む
    output_path = sys.argv[2]  # 出力画像のパス
    font_path = "./azukifont121/azuki.ttf"  # フォントファイルのパス (Noneの場合はデフォルトフォントが使用されます)
    font_size = 40  # フォントサイズ
    text_color = (int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))   # テキストの色 (R, G, B)
    outline_color=(int(sys.argv[6]),int(sys.argv[7]),int(sys.argv[8]))
    create_transparent_text_image(text, font_path, font_size, output_path, text_color, outline_color)