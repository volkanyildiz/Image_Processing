
# coding: utf-8

# In[33]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math


# In[34]:


def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3 = w[0],w[1],w[2]
    return math.sqrt((a**2)*w1 + (b**2)*w2 + (c**2)*w3)


# In[35]:


def turn_rgb_to_gray_level(image_rgb):
    m,n=image_rgb.shape[0],image_rgb.shape[1]
    image_gray_level = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            image_gray_level[i,j]=get_distance(image_rgb[i,j,:])
    return image_gray_level


# In[36]:


def apply_mask_avg(part_of_image):
    return np.average(part_of_image)

def apply_mask_med(part_of_image):
    return np.median(part_of_image)


# In[37]:


im_1=plt.imread("turtle.jpg")
im_2=turn_rgb_to_gray_level(im_1)
im_3=np.zeros((m,n))
im_4=np.zeros((m,n))


# In[38]:


m,n=im_1.shape[0],im_1.shape[1]


# In[39]:


plt.imshow(im_1)
plt.show()
plt.imshow(im_2,cmap='gray')
plt.show()


# In[40]:


#filter
for i in range(m):
    for j in range(n):
        if(i==0 or j==0 or i==m or j==n):
            continue
        else:
            poi=im_2[i-1:i+2,j-1:j+2]
            im_3[i,j]=apply_mask_avg(poi)


# In[41]:


plt.imshow(im_3,cmap='gray') #MEAN FILTER'li resmi bastırıyorum
plt.show()


# In[42]:


for i in range(m):
    for j in range(n):
        if(i==0 or j==0 or i==m or j==n):
            continue
        else:
            poi=im_2[i-1:i+2,j-1:j+2]
            im_4[i,j]=apply_mask_med(poi)


# In[43]:


plt.imshow(im_4,cmap='gray')
plt.show()

