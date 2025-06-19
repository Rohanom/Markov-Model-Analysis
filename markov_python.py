#!/usr/bin/env python
# coding: utf-8

# In[19]:


import yfinance as yf
import pandas as pd
import numpy as np


# In[20]:


ticker = "SPY"
data = yf.download(ticker, start="2010-01-01", end="2022-04-22")


# In[21]:


data


# In[22]:


data["daily_return"] = data["Adj Close"].pct_change()
data["state"] = np.where(data["daily_return"] >= 0, "up", "down")


# In[23]:


data


# In[24]:


up_counts = len(data[data["state"] == "up"])
down_counts = len(data[data["state"] == "down"])
up_to_up = len(data[(data["state"] == "up") & (data["state"].shift(-1) == "up") ]) / len(data.query('state=="up"'))
down_to_up = len(data[(data["state"] == "up") & (data["state"].shift(-1) == "down")]) / len(data.query('state=="up"'))
up_to_down = len(data[(data["state"] == "down") & (data["state"].shift(-1) == "up")]) / len(data.query('state=="down"'))
down_to_down = len(data[(data["state"] == "down") & (data["state"].shift(-1) == "down")]) / len(data.query('state=="down"'))
transition_matrix = pd.DataFrame({
    "up": [up_to_up, up_to_down],
    "down": [down_to_up, down_to_down]
}, index=["up", "down"])

print(transition_matrix)


# In[26]:


len(data[(data["state"] == "up") & (data["state"].shift(-1) == "down") & (data["state"].shift(-2) == "down") & (data["state"].shift(-3) == "down") & (data["state"].shift(-4) == "down") & (data["state"].shift(-5) == "down")]) / len(data[(data["state"].shift(1) == "down") & (data["state"].shift(2) == "down") & (data["state"].shift(3) == "down") & (data["state"].shift(4) == "down") & (data["state"].shift(5) == "down")])


# In[ ]:




