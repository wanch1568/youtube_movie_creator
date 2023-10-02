from PIL import Image, ImageDraw, ImageFont
import numpy as np

def create_graded_text_image(text, colors, font_path, font_size, output_file):
    font = ImageFont.truetype(font_path, font_size)
    char_sizes = [font.getmask(c).getbbox()[2] for c in text]
    size = (sum(char_sizes), max(font.getmask(c).getbbox()[3] for c in text))
    img = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    x_offset = 0
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        draw.text((x_offset, 0), char, font=font, fill=color)
        x_offset += char_sizes[i]

    img.save(output_file, "PNG")

if __name__ == "__main__":
    text = "サンプルテキスト"
    colors = [(255, 0, 0), (255, 255, 255), (255, 0, 0), (0, 0, 255), (255, 255, 255), (0, 0, 255)]
    font_path = "honoka/Honoka_Shin_Mincho_L.otf"
    font_size = 40
    output_file = "output.png"

    create_graded_text_image(text, colors, font_path, font_size, output_file)
