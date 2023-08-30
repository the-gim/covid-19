#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('file.csv')


# In[3]:


data


# In[4]:


data.count()


# In[6]:


data.isnull().sum()


# In[8]:


import seaborn as sns


# In[9]:


import matplotlib.pyplot as plt


# In[11]:


sns.heatmap(data.isnull())
plt.show()


# In[12]:


data.head(2)


# In[14]:


#data.groupby('Region').sum().head(20)


# In[18]:


#data.groupby('Region')['Confirmed'].sum().sort_values(ascending = False).head()


# In[20]:


#data.groupby('Region')['Confirmed', 'Recovered'].sum()


# In[21]:


data.head(2)


# In[25]:


data = data[~(data.Confirmed < 10)] #to remove the records satisfying condition


# In[26]:


data


# In[27]:


data.head(2)


# In[28]:


data.groupby('Region').Confirmed.sum().sort_values(ascending = False).head(20)


# In[29]:


data.head(2)


# In[31]:


data.groupby('Region').Deaths.sum().sort_values(ascending = True).head(20)


# In[32]:


data.head(2)


# In[34]:


data[data.Region == 'India']


# In[35]:


data[data.Region == 'Yemen']


# In[36]:


data[data.Region == 'US']


# In[37]:


data.head(2)


# In[38]:


data.sort_values( by = ['Recovered'] , ascending = False)


# In[ ]:




