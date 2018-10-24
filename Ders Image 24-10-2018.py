
# coding: utf-8

# In[12]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math


# In[13]:


img_1=plt.imread("TC.jpg")


# In[14]:


plt.imshow(img_1)
plt.show()


# In[15]:


def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c=v[0],v[1],v[2]
    w1,w2,w3 = w[0],w[1],w[2]
    return math.sqrt((a**2)*w1 + (b**2)*w2 + (c**2)*w3)


# In[16]:


def convert_rgb_to_gray_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2=np.zeros((m,n))  #aşlangıçta im_2 nin oyutları verilmediğinden hata vermemesi için yazıldı
    for i in range(m):
        for j in range(n):
            im_2[i,j]=get_distance(im_1[i,j,:])
    return im_2


# In[17]:


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


# In[18]:



            


# In[27]:


def piksel_compare_1(piksel):
    if(img_1[i-1:i+1,j-1:j+1]):
        return True
    else:
        return False


# In[28]:


def piksel_compare_2(piksel):
    if(img_1[i-1:i+1,j-1:j+1]):
        return False
    else:
        return True


# In[29]:


def fonksiyon(img_1):
    m,n=img_1.shape[0],img_1.shape[1]
    e,internal=0,0
    for i in range(1,m-1):
        for j in range(1,n-1):
            if(piksel_compare_1(img_1[i,j])):
                e=e+1
            if(piksel_compare_2(img_1[i,j])):
                internal+=1
    return (e-internal)/4


# In[35]:


img_1=plt.imread("TC.jpg")
get_ipython().run_line_magic('matplotlib', 'inline')
img_2=convert_rgb_to_gray_level(img_1)
img_3=convert_gray_level_to_BW(img_2)


plt.imshow(img_3,cmap='gray')
plt.show()


# In[43]:


my_block=img_3[10:12,50:52]
my_block= my_block.reshape(1,4)
my_block.shape


# In[51]:


def fonksiyon(img_1):
    m,n=img_1.shape[0],img_1.shape[1]
    e,internal=0,0
    for i in range(1,m-1):
        for j in range(1,n-1):
            p=img_1[i:i+2,j:j+2]
            siyah=0
            beyaz=0
            for a in range(2):
                for b in range(2):
                    if p[a][b]==1:
                        beyaz=beyaz+1
                    else:
                        siyah=siyah+1
            if(siyah>beyaz and beyaz>0):
                internal=internal+1
            elif(beyaz>siyah and siyah>0):
                e=e+1
                
    print("external ",e)
    print("internal",internal)
    print("object",(e-internal)/4)


# In[52]:


fonksiyon(img_3)

