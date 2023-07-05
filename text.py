from PIL import Image
from moviepy.editor import *


pic = Image.new('RGB', (100, 100), 'green')
pic.save('my_image.png')
image = ['my_image.png', ]
clip = [ImageClip(m).set_duration(3) for m in image]
concatenated = concatenate_videoclips(clip, method='compose')
concatenated.write_videofile('my_video.mp4', fps=30)


txt = 'бегущая строка'

w = 100
h = 50

clip = VideoFileClip("my_video.mp4")

txt_clip = TextClip(
    txt, color="white", fontsize=25, font="arial.ttf"
).set_duration(3)

txt_clip = txt_clip.set_pos(lambda t: (int(-w*t+100),
                                       int(5.4 * h / 6)))

video = CompositeVideoClip([clip, txt_clip])

video.write_videofile('my_video.mp4')