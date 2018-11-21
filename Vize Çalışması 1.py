
# coding: utf-8

# In[1]:


liste = [0,1,2,3,4,5,6,7,8,9]

for i in range(len(liste)):
    print(liste[i])


# In[2]:


print(liste)


# In[3]:


import random


# In[4]:


s= random.randint(5,10)
print(s)


# In[5]:


s


# In[6]:


for i in range(10):
    print(i)


# In[12]:


liste2=[]
for i in range(10):
    liste2.append(random.randint(0,10))
print (liste2)


# In[13]:


import numpy as np


# In[20]:


x=4
liste2=np.arange(x)
liste3=liste2+7
print(liste2)
print(liste3)


# In[17]:


s= np.arange(20)
s


# In[23]:


import matplotlib.pyplot as plt


# In[24]:


img= plt.imread("turtle.jpg")
plt.imshow(img)


# plt.show()

# In[26]:


plt.imshow(img)
plt.show()


# In[27]:


print(img.shape)


# In[36]:


def fonksiyon1(img):
    print("Resmin boyutu = ",img.ndim) 
    print("Resmin Shape değeri = ",img.shape)
    print("Kırmızı için min değer = ",img[:,:,0].min()) # : -> tümü
    print("Kırmızı için max değer = ",img[:,:,0].max()) # 0 kırmızı, 1 yeşil , 2 mavi
    print("Yeşil için min değer = ",img[:,:,1].min())
    print("Yeşil için max değer = ",img[:,:,1].max())
    print("Mavi için min değer = ",img[:,:,2].min())
    print("Mavi için max değer = ",img[:,:,2].max())


# In[37]:


fonksiyon1(img)


# In[4]:


s= random.randint(5,6)
print(s)


# In[5]:


s= random.randint(5,6)
print(s)


# In[6]:


s= random.randint(5,6)
print(s)

