#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import ydata_profiling as pp

# Read in the data
adult_df = pd.read_csv('adult.csv')
adult_df.info()
adult_df.head()

# Generate the profile report
profile = pp.ProfileReport(adult_df, title='PProfiling Report')

# Display the report
profile.to_notebook_iframe()

#Identify the missing values
adult_df.isna()


# In[6]:


# Generate the profile report
profile = pp.ProfileReport(adult_df, title='PProfiling Report')


# In[7]:


# Display the report
profile.to_notebook_iframe()


# In[8]:


adult_df.isna()


# In[15]:


'##Title'


# In[ ]:




