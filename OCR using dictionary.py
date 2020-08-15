#!/usr/bin/env python
# coding: utf-8

# In[3]:


import PIL
from PIL import Image, ImageChops
import pytesseract
import string

im = Image.open("C:\Projects\Inorbit.jpg")
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'
text_image = im.convert('L')
text_image=text_image.resize((600,400))
text_image = text_image.crop((360,25,445,55))
text_image=text_image.resize((text_image.width*5, text_image.height*5))

def binary_image(text_image, threshold):
    for i in range(text_image.width):
        for j in range(text_image.height):
            if text_image.getpixel((i,j))<threshold:
                text_image.putpixel((i,j),0)
            else:
                text_image.putpixel((i,j),255)
    return text_image
eng_dict=[]
with open ("C:\Projects/dictionary.txt", "r") as f:
    data=f.read()
    eng_dict=data.split("\n")

for i in range(95,105):
    strng=pytesseract.image_to_string(binary_image(text_image,i))
    strng=strng.lower()
    comparison=''
    for character in strng:
        if character in string.ascii_lowercase:
            comparison=comparison+character
    if comparison in eng_dict:

        print(comparison)
display(text_image)



# In[ ]:




