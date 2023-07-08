import cv2
from PIL import Image, ImageFont, ImageDraw

def video_maker(text):
    frame = (100, 100)
    output = cv2.VideoWriter('./static/run/output_video.avi', cv2.VideoWriter_fourcc(*'DIVX'), 30, frame)
    width = 0
    font = ImageFont.truetype('./static/run/arial.ttf', 40)
    for i in text:
        width += font.getlength(i)
    x = 100
    for i in range(0, 90):
        image = Image.new('RGB', (100, 100), (100, 50, 13))
        draw = ImageDraw.Draw(image)
        draw.text((x, 50), text, font=font)
        image.save('static/run/my_image.png')
        image = cv2.imread("./static/run/my_image.png")
        output.write(image)
        x -= (100+width)/90
    output.release()

