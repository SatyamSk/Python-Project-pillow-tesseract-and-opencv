#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math
import zipfile
from PIL import Image, ImageOps, ImageDraw
import pytesseract
import cv2 as cv
import numpy as np

bundle = {}
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('readonly/haarcascade_eye.xml')

with zipfile.ZipFile('readonly/images.zip', 'r') as img_zip:
    for entry in img_zip.infolist():
        with img_zip.open(entry) as file:
            img = Image.open(file).convert('RGB')
            bundle[entry.filename] = {'pil_img':img}

for name in bundle.keys():
    text = pytesseract.image_to_string(bundle[name]['pil_img'])
    bundle[name]['text'] = text

for name in bundle.keys():
    open_cv_image = np.array(bundle[name]['pil_img']) 
    gray_img = cv.cvtColor(open_cv_image, cv.COLOR_BGR2GRAY)
    faces_bounding_boxes = face_cascade.detectMultiScale(gray_img, 1.3, 5)
    bundle[name]['faces'] = []
    for x,y,w,h in faces_bounding_boxes:
        faces = bundle[name]['pil_img'].crop((x,y,x+w,y+h))
        bundle[name]['faces'].append(faces)

for name in bundle.keys():
    for faces in bundle[name]['faces']:
        faces.thumbnail((100,100),Image.ANTIALIAS)
        
def find_face(string):
    for name in bundle:
        if (string in bundle[name]['text']):
            if(len(bundle[name]['faces']) != 0):
                print("Result found in file {}".format(name))
                h = math.ceil(len(bundle[name]['faces'])/5)
                contact_sheet=Image.new('RGB',(500, 100*h))
                x = 0
                y = 0
                for img in bundle[name]['faces']:
                    contact_sheet.paste(img, (x, y))
                    if x + 100 == contact_sheet.width:
                        x = 0
                        y += 100
                    else:
                        x += 100
                        
                display(contact_sheet)
            else:
                print("Result found in file {} \nBut there were no faces in that file\n\n".format(name))
    return


# In[9]:


find_face('Christopher')


# In[12]:


find_face('Mark')


# In[13]:


find_face('pizza')


# In[ ]:




