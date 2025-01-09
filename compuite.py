#!/usr/bin/env python
# coding: utf-8

# In[1]:


def mean_value(given_list):
    total = sum(given_list)
    average_value = total/len(given_list)
    return average_value


# In[3]:


L = [1,2,3,4,5,6,7,8,9,10]
mean_value(L)


# In[5]:


def avg_value(*n):
    l = len(n)
    average = sum(n)/l
    return average
    


# In[7]:


avg_value(10,20,60,100,900)


# In[11]:


def median_value(*n):
    num_list = list(n)
    num_list.sort()
    l = len(num_list)
    if l%2 ==0:
        median = (num_list[int(l/2)] + num_list[int((l/2))-1])/2
    else:
        median = num_list[int(l/2)]
    return median
                


# In[13]:


median_value(1,2,3,4,5,6,7,8,9,10)


# In[ ]:





# In[ ]:




