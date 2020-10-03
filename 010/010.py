from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def randChar():
    return chr(random.randint(65, 90))

def randColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def randColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width, height = 240, 60
image = Image.new("RGB", (width, height), (255, 255, 255))
#创建font对象
font = ImageFont.truetype("font.ttf", 40)
#创建draw对象
draw = ImageDraw.Draw(image)

#填充每一个像素  
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=randColor())
#输出文字
for t in range(4):
    draw.text((60*t+20, 10), randChar(), font = font, fill = randColor2())

#模糊处理
image = image.filter(ImageFilter.BLUR)
#保存图片
image.save("code.jpg", "jpeg")
#展示图片
image.show("code.jpg")
