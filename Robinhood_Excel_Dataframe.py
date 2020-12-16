#!/usr/bin/env python
# coding: utf-8

# In[4]:


pip install robin_stocks


# In[5]:


import robin_stocks 
import pandas as pd
import matplotlib.pyplot as plt

robin_stocks.login("dhruvspatel","Sureshdpatel1234")

my_stocks = robin_stocks.build_holdings()


# In[6]:


stock_list = pd.DataFrame(my_stocks)
stock_list = stock_list.T
stock_list['ticker'] = stock_list.index
stock_list = stock_list.reset_index(drop=True)
stock_list['quantity'] = stock_list['quantity'].astype(float)
stock_list['average_buy_price'] = stock_list['average_buy_price'].astype(float)


# In[7]:


stock_list


# In[8]:


stock_list["total_stock_price"] = stock_list["quantity"]*stock_list["average_buy_price"]


# In[9]:


stock_list


# In[10]:


stock_list.loc['Total Money Invested'] = pd.Series(stock_list['total_stock_price'].sum(), index = ['total_stock_price'])


# In[11]:


data = pd.DataFrame(dct)  


# In[12]:


stock_list


# In[13]:


stock_list.drop(['id','type'], axis=1)


# In[14]:


stock_list.to_excel("StockList.xlsx")


# In[ ]:




