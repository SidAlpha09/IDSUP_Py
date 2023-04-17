#!/usr/bin/env python
# coding: utf-8

# In[1]:


# list is to be entered
def mean(xs):
    return sum(xs)/len(xs)


# In[4]:


def media(xs):
    sorted_xs=sorted(xs)
    if len(xs)%2==0:#even condition
        ev_mid=len(xs)//2
        return (sorted_xs[even-1]+sorted_xs[even])/2
    
    else:
        return sorted_xs[len(xs)//2]


# In[5]:


def quantile(xs,p):# p can be 0.25,0.75,.50(median)
    p_index=int(p*len(xs))
    return sorted(xs)[p_index]


# In[6]:


#Mode--retrun the element having the highest frequency
def mode(x):
    counts=Counter(x)
    max_count=max(counts.values())
    return [x_i for x_i,count in counts.items()
           if count==max_count]


# In[8]:


#range
def data_range(xs):
    return max(xs)-min(xs)


# In[9]:


# Varaince
# Sum of squares
def sum_of_sqaures(v):
    return dot(v,v)

def de_mean(xs):
    x_bar=mean(xs)
    return [x-x_bar for x in xs]

def vairance(xs):
    n=len(xs)
    deviation=de_mean(xs)
    return sum_of_sqaures(deviation)/(n-1)


# In[10]:


# Standard deviation ===sqrt(varinace)
def standard_deviation(xs):
    return math.sqrt(variance(xs))


# In[11]:


# interQuartile--difference between the 75th and 25th percentile values
def interQuartile(xs):
    return quantile(xs,0.75)-quantile(xs,0.25)


# In[12]:


# Covariance and corelation
def dot(v,w):
    assert len(v)==len(w)
    return sum(v_i*w_i for v_i,w_i in zip(v,w))

def covariance(xs,ys):
    assert len(xs)==len(ys)
    return dot(de_mean(xs),de_mean(ys))/(len(xs)-1)


# In[13]:


# Correlation
def correlation(xs,ys):
    stddev_x=standard_deviation(xs)
    stddev_y=standard_deviation(ys)
    if stddev_x>0 and stddev_y>0:
        return covariance(xs,ys)/(stddev_x*stddev_y)
    else:
        return 0


# In[ ]:




