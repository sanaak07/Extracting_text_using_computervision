#!/usr/bin/env python
# coding: utf-8

# # The (Py)Tesseract Library

# In[1]:


#Import required libraries
from PIL import Image

image  = Image.open('1.png')
display(image)


# In[2]:


#import pytesseract
import pytesseract
dir(pytesseract)


# In[3]:


help(pytesseract.image_to_string)


# In[4]:


#resize image
help(Image.Image.resize)


# In[5]:


import inspect
src = inspect.getsource(pytesseract.image_to_string)
print(src)


# In[6]:


#we can use this function in jupyter too
get_ipython().run_line_magic('pinfo2', 'pytesseract.image_to_string')


# In[7]:


#running pytesseract on this image
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string(image)
print(text)


# # Using more tesseract

# In[8]:


#Using a different image with same text with added noise in the picture
from PIL import Image
img=Image.open('2.png')
display(img)


# In[9]:


#Let's see if OCR works on noisy image
import pytesseract
text = pytesseract.image_to_string(Image.open('2.png'))
print(text)


# In[10]:


#Working more on the image
import PIL
basewidth = 600
img = Image.open('2.png')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize),PIL.Image.ANTIALIAS)
img.save('resized2.png')
display(img)
text = pytesseract.image_to_string(Image.open('resized2.png'))
print(text)


# In[11]:


#Improvment for resizing the image
img = Image.open('2.png')
iimg = img.convert('L')
#save the image
img.save('greyscale_2.png')
text = pytesseract.image_to_string(Image.open('greyscale_2.png'))
print(text)


# In[12]:


#Open noisy image and convert it using binarisation
img = Image.open('2.png').convert('1')
#Save the image
img.save('black_white_2.png')
display(img)


# In[13]:


#Defining a function called binarize that takes an image and a threshold value
def binarize(imgae_to_transform,threshold):
    output_image = image_to_transform.convert('L')
    
    for x in range(output_image.width):
        for y in range(output_image.height):
            if output_image.getpixel((x,y))<threshold:
                output_imgae.putpixel((x,y),0)
            else:
                output_image.putpixel((x,y),225)
    return output_image

    
    for thresh in range(0,257,64):
        print('Trying with threshold' + str(thresh))
        display(binarize(Image.open('2.png'),thresh))
        print(pytesseract.image_to_string(binarize(Image.open('2.png'),thresh)))


# In[ ]:




