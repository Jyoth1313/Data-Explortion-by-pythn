#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[13]:


data = pd.read_csv(r"C:\Users\nanakjyoth\Downloads\Weather.csv")


# In[5]:


data


# In[6]:


data.head()


# In[7]:


data.shape


# In[8]:


data.index


# In[9]:


data.columns


# In[10]:


data.dtypes


# In[16]:


data['Weather'].unique()


# In[17]:


data.nunique()


# In[18]:


data.count()


# In[20]:


data['Weather'].value_counts()


# In[21]:


data.info()


# In[ ]:


#now exploration


# In[22]:


data.head(2)


# In[23]:


data.nunique()


# In[24]:


data['Wind Speed_km/h'].nunique()


# In[25]:


data['Wind Speed_km/h'].unique()


# In[27]:


data.head(3)


# In[28]:


data.Weather.value_counts()


# In[31]:


#data.head(2)
data[data.Weather=='Clear']


# In[33]:


data.groupby('Weather').get_group('Clear')


# In[35]:


data [data['Wind Speed_km/h']==4]


# In[39]:


data.isnull().sum()


# In[40]:


data.notnull().sum()


# In[43]:


data.rename(columns = {'Weather' :'weather cnd' }, inplace = True)


# In[44]:


data.head(1)


# In[45]:


data.Visibility_km.mean()


# In[46]:


data.Press_kPa.std()


# In[47]:


data['Rel Hum_%'].var()


# In[49]:


data['weather cnd'].value_counts()


# In[52]:


#filtering
data[data['weather cnd'] == 'Snow']


# In[54]:


#str.contain

data[data['weather cnd'].str.contains('Snow')].tail(20)


# In[57]:


#wind above 24

data[(data['Wind Speed_km/h']>24)&(data['Visibility_km'] ==25)] 


# In[60]:


#mean for ech column in wthr cnd
#data.head(1)

data.groupby('weather cnd').mean()


# In[62]:


#mx and Min vlue for wthr cnd
data.groupby('weather cnd').min()
data.groupby('weather cnd').max()



# In[65]:


#wthr cnd is fog

data[data['weather cnd'] == 'Fog']


# In[70]:


#wthr clr or visblty > 40
data[(data['weather cnd'] == 'Clear') | (data['Visibility_km']>40)]
#data.head(1)
         


# In[ ]:


#all instance clear and rltive humidty >50
#and vblity >40


# In[72]:


data.head(1)


# In[76]:


data[(data['weather cnd'] == 'Clear') &(data['Rel Hum_%']> 50) |(data['Visibility_km']> 40)]



# In[ ]:





# In[ ]:




