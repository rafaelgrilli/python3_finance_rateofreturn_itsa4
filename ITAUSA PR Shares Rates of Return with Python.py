#!/usr/bin/env python
# coding: utf-8

# # With this simple Python code, I will estimate Itausa's simple returns. The first thing that I have done is downloading historical data for Itausa (ticker ITSA4, Sao Paulo Stock Exchange), and creating a repository for the downloaded data. I use the Anaconda Navigator, which is a pretty complete package for analysing financial or any orther type of data. The code will be written on next lines, hope it can be repplied by anyone willing to measure returns of any stock or any other matter. 

# # first step: call the modules used for this computation: numpy, pandas, and the data we have downloaded from yahoofinance. 

# In[17]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
ITSA4 = pd.read_csv('ITSA4.csv', index_col='Date')


# In[20]:


ITSA4.info()


# In[21]:


ITSA4.head()


# In[22]:


ITSA4.tail()


# # estimating the Simple Rate of Return

# In[23]:


ITSA4['simple_return'] = (ITSA4['Adj Close'] / ITSA4['Adj Close'].shift(1)) - 1
print (ITSA4['simple_return'])


# In[24]:


ITSA4['simple_return'].plot(figsize=(10,7))
plt.show()


# # on the next two cells, we estimate the simple average returns for ITSA4, as well as the annualized returns for the stock, respectively. We apply 250 trading days as assumption. 

# In[25]:


avg_returns_a = ITSA4['simple_return'].mean() * 250
avg_returns_a


# In[26]:


print (str(round(avg_returns_a, 5) * 100) + '% ')


# # on the next cells, we estimate the Log returns for ITSA4, daily and annualized. 

# In[27]:


ITSA4['log_returns'] = np.log(ITSA4['Adj Close'] / ITSA4['Adj Close'].shift(1))
print (ITSA4['log_returns'])


# In[28]:


ITSA4['log_returns'].plot(figsize=(8,5))
plt.show()


# In[33]:


log_returns_a = ITSA4['log_returns'].mean() * 250
log_returns_a


# In[34]:


print (str(round(log_returns_a, 5) * 100) + ' %')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




