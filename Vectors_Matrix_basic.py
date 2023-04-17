#!/usr/bin/env python
# coding: utf-8

# In[1]:


from typing import List
from collections import Counter,defaultdict
import random
import math


# In[2]:


Vector=List[float]


# In[3]:


def add(v,w):
    assert len(v)==len(w)
    return[v_i+w_i for v_i,w_i in zip(v,w)]


# In[4]:


def sub(v,w):
    assert len(v)==len(w)
    return[v_i-w_i for v_i,w_i in zip(v,w)]


# In[5]:


def vector_sum(vectors):
    assert vectors
    num_elements=len(vectors[0])
    assert all(len(v)==num_elements for v in vectors)
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


# In[6]:


def scalar(c,v):
    return [c*v_i for v_i in v]


# In[8]:


def vector_mean(vectors):
    n=len(vectors)
    return scalar(1/n,vector_sum(vectors))


# In[10]:


def dot(v,w):
    assert len(v)==len(w)
    return sum(v_i*w_i for v_i,w_i in zip(v,w))


# In[11]:


# Sum of squares
def sum_of_sqaures(v):
    return dot(v,v)


# In[12]:


#magnitude of the vecotor
def mag(v):
    math.sqrt(sum_of_sqaures(v))


# In[13]:


#distance between two vectors
def dis(v,w):
    return math.sqrt(sum_of_sqaures(v,w))


# In[14]:


def shape(A):
    num_rows=len(A)
    num_cols=len(A[0]) if A else 0
    return num_rows,num_cols


# In[16]:


def make_matrix(num_rows,num_cols,entry_fn):
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]


# In[20]:


def identity_matrix(n):
    return make_matrix(n,n,lambda i,j: 1 if i==j else 0)


# In[ ]:




