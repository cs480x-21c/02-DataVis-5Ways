#!/usr/bin/env python
# coding: utf-8

# In[30]:


#!python -m pip install --upgrade pip
#!pip3 install plotly
import pandas as pd
import plotly.express as px

data = pd.read_csv("https://raw.githubusercontent.com/FISH-HAT/02-DataVis-5Ways/main/cars-sample.csv")

fig = px.scatter(data, x="Weight", y="MPG", size="Weight", color="Manufacturer",
                 color_discrete_sequence=['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000'],
                size_max=20, hover_name="Car")

fig.show()


# In[ ]:




