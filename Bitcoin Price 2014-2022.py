#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data = pd.read_csv('bitcoindata.csv')
print (data.shape)
data.info()


# In[5]:


data.head()


# In[6]:


data['Date'] = pd.to_datetime(data['Date'])


# In[7]:


data['Year'] = data['Date'].dt.strftime('%Y')
data['Month'] = data['Date'].dt.strftime('%m')
data['Day'] = data['Date'].dt.strftime('%d')


# In[8]:


a = ['Open', 'Close', 'Low', 'High', 'Year', 'Month']
b = data[a].groupby(['Year', 'Month']).sum()
b


# In[9]:


b.plot(figsize=(20, 10), grid=True, marker='*')
plt.show()


# In[10]:


b.plot(kind='bar', figsize=(18, 9))
plt.show()


# In[11]:


b.plot(kind='area', figsize=(18, 9))
plt.show()


# In[ ]:




