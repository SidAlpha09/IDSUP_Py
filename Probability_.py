#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Normal destribution PDF
import math
import random
SQRT=math.sqrt(2*math.pi)
def NDF_PDF(x,mu,sigma):
    return (math.exp((-(x-mu)**2)/(2*(sigma**2)))/(SQRT*sigma))


# In[2]:


#Normal distribution CDF
def NDF_CDF(x,mu,sigma):
    return (1+math.erf((x-mu)/math.sqrt(2)/sigma))/2


# In[3]:


#Bernoulli Trial
def ber_tri(p):
    return 1 if random.random() < p else 0

def binomial(n,p):
    return sum(ber_tri(p) for _ in range(n))


# In[ ]:




