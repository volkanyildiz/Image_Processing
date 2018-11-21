
# coding: utf-8

# In[91]:


import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import iqr
from scipy.stats import skew


# In[92]:


img = plt.imread("turtle.jpg")
plt.imshow(img)
img.setflags(write=1) # resim sadece read-only özelliğine sahipti üzerinde değişiklik yapabilmek için değiştirdim
img.flags


# In[93]:


def inverse1(x):
    return 255-x


# In[94]:


def inverse(image):
    image[:,:,0]=inverse1(image[:,:,0])
    image[:,:,1]=inverse1(image[:,:,1])
    image[:,:,2]=inverse1(image[:,:,2])


# In[95]:


def mean(image):
    print("Kirmizi ortalamasi : ",np.mean(image[:,:,0]))
    print("Yesil ortalamasi : ",np.mean(image[:,:,1]))
    print("Mavi ortalamasi : ",np.mean(image[:,:,2]))


# In[96]:


def median(image):
    print("Kirmizi median : ",np.median(image[:,:,0]))
    print("Yesil median : ",np.median(image[:,:,1]))
    print("Mavi median : ",np.median(image[:,:,2]))


# In[97]:


def mode(image):
    print("Kirmizi mode: ",stats.mode(image[:,:,0]))
    print("Yesil mode : ",stats.mode(image[:,:,1]))
    print("Mavi mode: ",stats.mode(image[:,:,2]))


# In[98]:


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


# In[99]:


def ceyreklik(image):
    print("Kirmizi Q1 degeri = ",np.percentile(image[:,:,0],25))
    print("Kirmizi Q2 degeri = ",np.percentile(image[:,:,0],50))
    print("Kirmizi Q3 degeri = ",np.percentile(image[:,:,0],75))
    print("Yesil Q1 degeri = ",np.percentile(image[:,:,1],25))
    print("Yesil Q2 degeri = ",np.percentile(image[:,:,1],50))
    print("Yesil Q3 degeri = ",np.percentile(image[:,:,1],75))
    print("Mavi Q1 degeri = ",np.percentile(image[:,:,2],25))
    print("Mavi Q2 degeri = ",np.percentile(image[:,:,2],50))
    print("Mavi Q3 degeri = ",np.percentile(image[:,:,2],75))
    print("Kirmizi iqr degeri = ",iqr(image[:,:,0]))
    print("Yesil iqr degeri = ",iqr(image[:,:,1]))
    print("Mavi iqr degeri = ",iqr(image[:,:,2]))


# In[100]:


def standard(image):
    print("Kirmizi skewness degeri = ",skew(image[:,:,0]))
    print("Yesil skewness degeri = ",skew(image[:,:,1]))
    print("Mavi skewness degeri = ",skew(image[:,:,2]))


# In[101]:


def aralik(image):
    print("Kirmizi range araligi = ",image[:,:,0].max()-image[:,:,0].min())
    print("Yesil range araligi = ",image[:,:,0].max()-image[:,:,1].min())
    print("Mavi range araligi = ",image[:,:,0].max()-image[:,:,2].min())


# In[102]:


inverse(img)
plt.imshow(img)


# In[103]:


mean(img)
median(img)
ceyreklik(img)


# In[104]:


my_H(img)


# In[105]:


inverse(img)
plt.imshow(img)


# In[90]:


my_H(img)

