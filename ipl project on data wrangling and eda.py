#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# loading the required libraries
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[7]:


# loading the ipl matches dataset
ipl=pd.read_csv('F:/python/DATASETS/matches.csv')


# In[8]:


# having a glance at the first five records of the dataset
ipl.head()


# In[9]:


# looking at the number of rows and columns in the dataset
ipl.shape


# In[10]:


# Getting the frequency of most man of the match awards
ipl['player_of_match'].value_counts()


# In[11]:


# Getting the top 10 players with most man of the match awards
ipl['player_of_match'].value_counts()[0:10]


# In[13]:


list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[14]:


# making a bar-plot for the top 5 players with most man of the match awards
plt.figure(figsize=(8,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color='g')
plt.show()


# In[15]:


# Getting the frequency of result column
ipl['result'].value_counts()


# In[16]:


# finding out the number of toss wins w.r.t each team 
ipl['toss_winner'].value_counts()


# In[17]:


# Extracting the records where a team won batting first
batting_first=ipl[ipl['win_by_runs']!=0]


# In[18]:


# Looking at the head 
batting_first.head()


# In[25]:


# Making a histogram
plt.figure(figsize=(5,6))
plt.hist(batting_first['win_by_runs'])
plt.title("Distribution of Runs")
plt.xlabel("Runs")
plt.show()


# In[26]:


# finding out the number of wins w.r.t each team after batting first
batting_first['winner'].value_counts()


# In[28]:


# Making a bar-plot for top 3 teams with most wins after batting first
plt.figure(figsize=(6,6))
plt.bar(list(batting_first['winner'].value_counts()[0:3].keys()),list(batting_first['winner'].value_counts()[0:3]),color=["blue","yellow","orange"])
plt.show()


# In[32]:


# Making a pie chart
plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[4]:


import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns


# In[7]:


ipl=pd.read_csv('F:/python/DATASETS/matches.csv')


# In[8]:


# Extracting those records where a team has won after batting second
batting_second=ipl[ipl['win_by_wickets']!=0]


# In[9]:


# looking at the head
batting_second.head()


# In[14]:


# Making a histogram for frequency of wins w.r.t number of wickets
plt.figure(figsize=(7,7))
plt.hist(batting_second['win_by_wickets'],bins=30)
plt.show()


# In[15]:


# finding out the frequency of number of wins w.r.t each time after batting second
batting_second['winner'].value_counts()


# In[16]:


# Making a bar plot for top-3 teams with most wins after batting second
plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=["purple","blue","red"])
plt.show()


# In[17]:


# Making a pie chart for distribution of most wins after batting second
plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[19]:


# looking at the number of matches played each season
ipl['Season'].value_counts()


# In[20]:


# looking at the number of matches played in each city
ipl['city'].value_counts()


# In[2]:


import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[4]:


ipl=pd.read_csv('F:/python/DATASETS/matches.csv')


# In[5]:


# finding out how many times a team has won the match after winning the toss
np.sum(ipl['toss_winner']==ipl['winner'])


# In[6]:


325/636


# In[8]:


deliveries=pd.read_csv('F:/python/DATASETS/deliveries.csv')


# In[9]:


deliveries.head()


# In[10]:


deliveries['match_id'].unique()


# In[11]:


match_1=deliveries[deliveries['match_id']==1]


# In[12]:


match_1.head()


# In[14]:


match_1.shape


# In[15]:


srh=match_1[match_1['inning']==1]


# In[16]:


srh['batsman_runs'].value_counts()


# In[17]:


srh['dismissal_kind'].value_counts()


# In[18]:


rcb=match_1[match_1['inning']==2]


# In[19]:


rcb['batsman_runs'].value_counts()


# In[20]:


rcb['dismissal_kind'].value_counts()


# In[ ]:





# In[ ]:





# In[ ]:




