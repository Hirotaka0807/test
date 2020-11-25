#!/usr/bin/env python
# coding: utf-8

# In[44]:


data = open('input.txt', 'r').readlines()
d = data[-1]
data.pop()
data = sorted(data)
data.append(d)


# In[47]:





# In[46]:


data = open('input.txt', 'r').readlines()
d = data[-1]
data.pop()
data = sorted(data)
data.append(d)

def FizzBuzz(data):
    m = int(data[-1])
    data.pop()
    for i in range(len(data)):
        lis = []
        num = int(data[i].split(':')[0])
        s = data[i].split(':')[1].replace('\n','')
        if m % num == 0:
            lis.append(s)
    if lis == []:
        lis.append(m)
    for s in lis: print(s, end ="")
        
FizzBuzz(data)

