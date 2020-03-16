#!/usr/bin/env python
# coding: utf-8

# #### IMDB, Rotten Tomatoes, Fandango Or Metacritic?

# Customize your graphs more by reproducing almost completely the FiveThirtyEight style. You can take a look at this tutorial if you want to do that.
# Improve your project from a stylistical point of view by following the guidelines discussed in this style guide.
# Use the two samples to compare ratings of different movie ratings aggregators and recommend what's the best website to check for a movie rating. There are many approaches you can take here — you can take some inspiration from this article.
# Collect recent movie ratings data and formulate your own research questions. You can take a look at this blog post to learn how to scrape movie ratings for IMDB and Metacritic.

# In[1]:


import pandas as pd
pd.options.display.max_columns = 100  # Avoid having displayed truncated output

previous = pd.read_csv('fandango_score_comparison.csv')
after = pd.read_csv('movie_ratings_16_17.csv')

previous.head(3)


# ####  Comparing Ratings of different movie ratings
# There are lot of websites for movies that come up with their own movie ratings.The most popular websites are 1) IMDB, 2) 3)Fandango, 4)otten Tomatoes, and 5) Metacritic.

# In[2]:


previous.columns


# In[3]:


after.columns


# In[4]:


Ratings_2015=previous.copy()


# In[5]:


Ratings_2015['Year'] = Ratings_2015['FILM'].str[-5:-1]


# In[32]:


Ratings_2016=after.copy()


# In[7]:


Ratings_2015['Year'].value_counts()


# In[8]:


Ratings_2015 = Ratings_2015[Ratings_2015['Year']=='2015'].copy()
Ratings_2015['Year'].value_counts()


# In[33]:


Ratings_2016['year'].value_counts()


# In[18]:


Ratings_2015.head(20)
Ratings_2015.shape


# In[29]:


Ratings_2015.head(5)


# In[35]:


Ratings_2016.head()


# In[13]:


colors = [[0,0,0], [230/255,159/255,0], [86/255,180/255,233/255], [0,158/255,115/255],
          [213/255,94/255,0], [0,114/255,178/255]]


# In[28]:


import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from numpy import arange
get_ipython().run_line_magic('matplotlib', 'inline')

# Generate a figure with 4 axes (2 rows by 2 columns)
fig = plt.figure(figsize = (15,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

# Remove grids for all axes
for ax in fig.axes:
    ax.grid(False)

## IMDB
#bins range is.5
ax1.hist(Ratings_2015.IMDB,bins = 20, range = (0,10), align = 'left')
ax1.axvline(3, color = 'black', alpha = 0.4)
ax1.axvline(7, color = 'black', alpha = 0.4)
ax1.set_ylim(0, 40)
ax1.text(5,30, 'The Average\n Area', fontsize = 17, weight = 'bold', ha = 'center')
ax1.set_yticks([0,10,20,30,40])
ax1.set_xticks([0,3,7,10])
ax1.set_yticklabels(labels =['0   ','10   ','20   ','30   ','40 movies'])   
ax1.text(5,-7.2, 'IMDB\n (0-10)', fontsize = 14, weight = 'bold', ha = 'center')
#ax1.text(-0.86,39.2, 'movies', fontsize = 11) 

# Fandango
ax2.hist(Ratings_2015.Fandango_Stars, bins=10, range=(0,5), align='left')
ax2.axvline(1.5, color='black',alpha=0.4)
ax2.axvline(3.5, color='black',alpha=0.4)
ax2.set_ylim(0,60)
ax2.set_yticks([0,15,30,45,60])
ax2.set_xticks([0,1.5,3.5,5])
ax2.text(2.5,-11, 'Fandango\n (0-5 stars)', weight='bold', fontsize=14, ha='center')
ax2.set_yticklabels(labels =['0   ','15   ','30   ','45   ','60 movies'])  

# Metacritic
ax3.hist(Ratings_2015.Metacritic,bins=20, range=(0,100),align='left')
#bin range = 5 (equivalent to 0.5 if normalized to 0-10)
ax3.axvline(30, color='black', alpha=0.4)
ax3.axvline(70, color='black', alpha=0.4)
ax3.set_ylim(0,20)
ax3.set_yticks([0,5,10,15,20])
ax3.set_xticks([0,30,70,100])
ax3.text(50,-3,'Metascore\n (0-100)', fontsize = 14, weight = 'bold', ha = 'center')

# RT
ax4.hist(Ratings_2015.RottenTomatoes, bins = 20, range = (0,100), align = 'left') # bin range = 5 
ax4.axvline(30, color = 'black', alpha = 0.4)
ax4.axvline(70, color = 'black', alpha = 0.4)
ax4.set_ylim(0,20)
ax4.set_yticks([0,5,10,15,20])
ax4.set_xticks([0,30,70,100])
ax4.text(50,-3.65, 'Tomatometer\n (0-100%)', fontsize = 14, weight = 'bold', ha = 'center')


# From the above , The Metascore's histogram resembles a normal distribution. it has a thick cluster in the average area area,the bar on the each of the other two areas, which decrease in height towards extremes, less gradually.All these clearly indicate that most of the metascores have an average value, The bulk of the distribution is in the average area as well, but there is an obvious skew towards the highest average values. The high ratings area looks similar to what would be expected to be seen for a normal distribution in that part of the histogram. However, the striking feature is that the area representing low movie ratings is completely empty, 

# In[41]:


fan_ds=previous.copy()
fan_ds.head()


# In[ ]:


fan_ds['Year'.value_count()


# In[38]:


### Fandango
fan_vals = Ratings_2016['fandango'].value_counts(normalize =True).sort_index()*100

