#!/usr/bin/env python
# coding: utf-8

# In[2]:


import PIL
from PIL import Image, ImageChops
import pytesseract

text_image = Image.open("C:\Projects\Inorbit.jpg")
display(text_image)
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR/tesseract.exe'

text_image=text_image.resize((600,400))
text_image = text_image.crop((360,25,445,55))

text_image=text_image.resize((text_image.width*5, text_image.height*5))
display(text_image)
text_image = text_image.convert('L')
def binary_image(text_image, threshold):
    for i in range(text_image.width):
        for j in range(text_image.height):
            if text_image.getpixel((i,j))<threshold:
                text_image.putpixel((i,j),0)
            else:
                text_image.putpixel((i,j),255)
    return text_image
text = pytesseract.image_to_string(binary_image(text_image,100))

display(text_image)
print (text)


# In[ ]:





# In[ ]:




