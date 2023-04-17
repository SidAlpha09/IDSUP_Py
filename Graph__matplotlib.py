#!/usr/bin/env python
# coding: utf-8

# In[32]:


import matplotlib.pyplot as plt
from collections import Counter,defaultdict
import random
import math


# In[3]:


# Line chart
years=[1950,1960,1970,1980,1990,2000,2010]
gdp=[300.2,543.2,1075.9,2862.5,5979.6,10289.7,300.8]
font={'color':'red','size':20}
plt.plot(years,gdp,color='green',linestyle='solid')

plt.title('Nominal GDP')
plt.ylabel('Billions of $')
plt.xlabel('years')
plt.show()


# In[4]:


#Bar Chart
movies=["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi",
"West Side Story"]
num_of_oscars=[5, 11, 3, 8, 10]
plt.bar(range(len(movies)),num_of_oscars)
plt.title('Movies and their oscars')
plt.ylabel('No.of Oscars')
plt.xticks(range(len(movies)),movies)
plt.show()


# In[8]:


# Histogram
grades=[83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
plt.hist(grades,histtype ='bar')
plt.xticks([10 * i for i in range(11)])
plt.show()


# In[12]:


variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
total_error=[x + y for x, y in zip(variance, bias_squared)]
xs = [i for i, _ in enumerate(variance)]
plt.plot(xs, variance, 'g-', label='variance')
'''green
solid line '''
plt.plot(xs, bias_squared, 'r-.', label='biasˆ2')
'''red
dot-dashed line '''
plt.plot(xs, total_error, 'b:', label='total error')
'''
blue dotted line '''
'''Because we have assigned labels to each series, we can
get a legend for free (loc=9 means "top center")'''
plt.legend(loc=9)#location 9 means center
plt.xlabel('Model complexity')
plt.title('The bias-variance tradeoff')
plt.show()


# In[23]:


# Scatter plot
friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
plt.scatter(friends, minutes)
for label, friend_count, minute_count in zip(labels,friends, minutes):
    plt.annotate(label,
    xy=(friend_count, minute_count),
    xytext=(5, -5),
    textcoords='offset points')
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()


# In[20]:


# Assingment 1 Question 14
test1=[99,90,85,97,80]
test2=[100,85,60,90,70]
plt.scatter(test1,test2)
plt.axis('equal')
#divides the x axis in equal parts
plt.show()


# In[22]:


s="aabbbasdfasdsdfasdfsfggigkheighkhweijkjwlejrj"
d=list(s)
dic=Counter(d)
y=[i for i in dic.keys()]
x=[i for i in dic.values() ]
# print(dic)
print(x)
print(y)
plt.xlabel("Alphabets",font)
plt.ylabel("# Occurances",font)
plt.bar(range(len(y)),x)
plt.xticks(range(len(x)), y)
plt.show()


# In[25]:


# Assingment 1 Question 11
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
max = [17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18]
min = [-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58]
plt.bar(months,max,width=0.5,label="Max",color = "Red")
plt.bar(months,min,width=0.5,label="Min",color = "Blue")
plt.legend()
plt.show()


# In[30]:


male_age = [53,51,71,31,33,39,52,27,54,30,64,26,21,54,52,20,59,32]
female_age = [53,65,68,21,75,46,24,63,61,24,49,41,39,40,25,54,42,
32,48,23,23]
plt.hist(male_age)
plt.show()
plt.hist(female_age,color='red')
plt.show()


# In[34]:


# Assingment 1 Question 9
x=[i for i in range(-10,10)]
y1=[i*math.sin(i) for i in x]
y2=[(i**2)*math.sin(i) for i in x]
y3=[(i**3)*math.sin(i) for i in x]
y4=[(i**4)*math.sin(i) for i in x]
plt.plot(x,y1,label='x sinx')
plt.plot(x,y2,label='x sin^2x')
plt.plot(x,y3,label='x sin^3x')
plt.plot(x,y4,label='x sin^4x')
plt.legend()
plt.show()


# In[52]:


# Generate a list of 100 random integers between 1 and 100 and plot histogram
# for the same
l=[random.randint(1,100) for _ in range(100)]
plt.hist(l)
plt.show()#for every consecutive run the graph will be different


# In[57]:


# Normal Probability Distribution Function
SQRT=math.sqrt(2*math.pi)
def NDF(x,mu,sigma):
    return (math.exp(-(x-mu)**2/2/sigma**2)/(SQRT*sigma))

xs=[x/10.0 for x in range(-50,50)]
plt.plot(xs,[NDF(x,mu=0,sigma=1) for x in xs],'-')
plt.plot(xs,[NDF(x,mu=0,sigma=2) for x in xs],'--')
plt.plot(xs,[NDF(x,mu=0,sigma=0.5) for x in xs],':')
plt.plot(xs,[NDF(x,mu=-1,sigma=1) for x in xs],':')
plt.legend()
plt.show()


# In[58]:


#Normal Cumulative Distribution Function
def NDF_CDF(x,mu,sigma):
    return (1+math.erf((x-mu)/math.sqrt(2)/sigma))/2

xs=[x/10.0 for x in range(-50,50)]
plt.plot(xs,[NDF_CDF(x,mu=0,sigma=1) for x in xs],'-')
plt.plot(xs,[NDF_CDF(x,mu=0,sigma=2) for x in xs],'--')
plt.plot(xs,[NDF_CDF(x,mu=0,sigma=0.5) for x in xs],':')
plt.plot(xs,[NDF_CDF(x,mu=-1,sigma=1) for x in xs],':')
plt.show()


# In[61]:


# Using the Binomial(n, p) distribution plot a histogram to show the actual
# binomial samples. Use a line chart to show the normal approximation. Plot both
# in the same graph. Take n=100, p=0.75 and number of points should be 100.
def bernoulli_trial(p):
    return 1 if random.random()<p else 0

def binomial(n,p):
    return sum(bernoulli_trial(p) for _ in range(n))

def binomial_hist(p,n,num_points):
    data = [binomial(n, p) for _ in range(num_points)]
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
        [v / num_points for v in histogram.values()],
        0.8,
        color='0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
        for i in xs]
    plt.plot(xs,ys)
    plt.title("Binomial Distribution vs. Normal Approximation")
    plt.show()
binomial_hist(0.75, 100, 100)

