#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


img = cv2.imread('C:/Users/Asus/Desktop/colour detection/house.jpg')


# In[5]:


plt.figure(figsize=(20,8))
plt.imshow(img)


# In[6]:


grid_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[7]:


plt.figure(figsize=(20,8))
plt.imshow(grid_RGB)


# In[8]:


grid_HSV = cv2.cvtColor(grid_RGB, cv2.COLOR_RGB2HSV)


# In[9]:


lower = np.array([0, 150, 50])
upper = np.array([10, 255, 255])


# In[10]:


mask = cv2.inRange(grid_HSV, lower, upper)


# In[11]:


plt.figure(figsize=(20,8))
plt.imshow(mask)


# In[12]:


res = cv2.bitwise_and(grid_RGB, grid_RGB, mask=mask)


# In[13]:


plt.figure(figsize=(20,8))
plt.imshow(res)


# In[ ]:





# In[ ]:




