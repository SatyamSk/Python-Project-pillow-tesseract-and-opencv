#!/usr/bin/env python
# coding: utf-8

# In[2]:


import PIL
from PIL import Image,ImageFont,ImageDraw,ImageChops,ImageFilter,ImageEnhance
from IPython.display import display


file = PIL.Image.open("Photo.png")
image = file.convert('RGB')
print(image)
intensity = [0.1, 0.5, 0.9]
r, g, b = image.split()
image = []
def red():
    for j in intensity:
        channel = 0
        global r, g, b
        r = r.point(lambda i: i * j )
        im = Image.merge('RGB',(r, g, b))
        text_color = im.getpixel((0, 70))
        font = ImageFont.truetype("arial.ttf",35)
        draw = ImageDraw.Draw(im)
        draw.rectangle((0,410,800,450),fill ='black')
        strin = 'channel '+str(channel)+'  intensity '+str(j)
        draw.text((20,409),strin,fill = text_color,font = font)
        r = r.point(lambda i: i/j)
        image.append(im)
        if j == 0.9:
            green()
def green():
    global r, g, b
    channel = 1

    for j in intensity:
        g = g.point(lambda i: i * j )
        im = Image.merge('RGB',(r, g, b))
        text_color = im.getpixel((0, 70))
        font = ImageFont.truetype("arial.ttf",35)
        draw = ImageDraw.Draw(im)
        draw.rectangle((0,410,800,450),fill ='black')
        strin = 'channel '+str(channel)+'  intensity '+str(j)
        draw.text((20,409),strin,fill = text_color,font = font)
        g = g.point(lambda i: i/j)
        image.append(im)
        if j == 0.9:
            blue()
def blue():
    global r, g, b
    channel = 2

    for j in intensity:
        b = b.point(lambda i: i * j )
        im = Image.merge('RGB',(r, g, b))
        text_color = im.getpixel((0, 70))
        font = ImageFont.truetype("arial.ttf",35)
        draw = ImageDraw.Draw(im)
        draw.rectangle((0,410,800,450),fill ='black')
        strin = 'channel '+str(channel)+'  intensity '+str(j)
        draw.text((20,409),strin,fill = text_color,font = font)
        b = b.point(lambda i: i/j)
        image.append(im)
red()
first_image = image[0]
contact_sheet=PIL.Image.new(first_image.mode, (3*first_image.width,3*first_image.height))
x=0
y=0

for img in image:
    contact_sheet.paste(img,(x,y))
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.save('assignment_result',format = 'jpeg')
display(contact_sheet)


# In[ ]:




