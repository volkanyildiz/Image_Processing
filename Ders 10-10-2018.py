
# coding: utf-8

# In[1]:


def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c= v[0],v[1],v[2]
    w1,w2,w3=w[0],w[1],w[2]
    d=((a**2)*w[0] + (b**2)*w[1] +(c**2)*w[2])**.5
   # d=((a*w1)**2+(b*w2)**2+(c*w3)**2)**.5
    return d
#w1,w2,w3 ağırlık
#v vektor


# In[2]:


my_RGB=[10,20,30]
gray_level= get_distance(my_RGB)
print(gray_level)


# In[3]:


def convert_rgb_to_gray_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2=np.zeros((m,n))  #aşlangıçta im_2 nin oyutları verilmediğinden hata vermemesi için yazıldı
    for i in range(m):
        for j in range(n):
            im_2[i,j]=get_distance(im_1[i,j,:])
    return im_2


# In[4]:


def convert_gray_level_to_BW(image_gray_level):
    m=image_gray_level.shape[0]
    n=image_gray_level.shape[1]
    im_bw=np.zeros((m,n))  #aşlangıçta im_2 nin oyutları verilmediğinden hata vermemesi için yazıldı
    for i in range(m):
        for j in range(n):
            if image_gray_level[i,j] > 120:
                im_bw[i,j]=1
            else:
                im_bw[i,j]=0
            #im_bw[i,j]=get_distance(image_gray_level[i,j])
    return im_bw


# In[5]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
im_1 =mpimg.imread("turtle.jpg")
#plt.imshow(img)
get_ipython().run_line_magic('matplotlib', 'inline')
#plt.imshow(img)

im_2=convert_rgb_to_gray_level(im_1)
im_3=convert_gray_level_to_BW(im_2)

plt.imshow(im_1)
plt.subplot(1,3,1),plt.imshow(im_1)
plt.subplot(1,3,2),plt.imshow(im_2,cmap='gray')
plt.subplot(1,3,3),plt.imshow(im_3,cmap='gray')

