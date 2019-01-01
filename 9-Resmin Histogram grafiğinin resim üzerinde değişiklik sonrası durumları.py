
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# In[2]:


def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c= v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    d=((a**2)*w[0] + (b**2)*w[1] +(c**2)*w[2])**.5
    return d


# In[3]:


def convert_rgb_to_gray_level(img):
    m=img.shape[0]
    n=img.shape[1]
    img_2=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            img_2[i,j]=get_distance(img[i,j,:])
    return img_2


# In[4]:


def convert_gray_level_to_BW(img):
    m=img.shape[0]
    n=img.shape[1]
    img_bw=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if img[i,j] > 120:
                img_bw[i,j]=1
            else:
                img_bw[i,j]=0
    return img_bw


# In[9]:


def my_H(image):
    H={}
    for i in range (image.shape[0]):
        for j in range (image.shape[1]):
            if(image[i,j,0] in H.keys()):
                H[image[i,j,0]]=H[image[i,j,0]]+1
            else:
                H[image[i,j,0]]=1
            if(image[i,j,1] in H.keys()):
                H[image[i,j,1]]=H[image[i,j,1]]+1
            else:
                H[image[i,j,1]]=1
            if(image[i,j,2] in H.keys()):
                H[image[i,j,2]]=H[image[i,j,2]]+1
            else:
                H[image[i,j,2]]=1
    plt.bar(list(H.keys()),list( H.values()), color='BLUE')
    plt.show()


# In[12]:


def my_H2(image):
    H={}
    for i in range (image.shape[0]):
        for j in range (image.shape[1]):
            if(image[i,j] in H.keys()):
                H[image[i,j]]=H[image[i,j]]+1
            else:
                H[image[i,j]]=1
           
    plt.bar(list(H.keys()),list( H.values()), color='BLUE')
    plt.show()


# In[24]:


img5 =mpimg.imread("siyah.jpg")
plt.imshow(img5)


# In[21]:


my_H(img5)


# In[25]:


img6 =mpimg.imread("siyah2.jpg")
plt.imshow(img6)


# In[23]:


my_H(img6)


# In[26]:


img7 =mpimg.imread("siyah3.jpg")
plt.imshow(img7)


# In[27]:


my_H(img7)


# In[28]:


img8 =mpimg.imread("siyah4.jpg")
plt.imshow(img8)


# In[29]:


my_H(img8)

