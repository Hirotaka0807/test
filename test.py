#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = open('input.txt', 'r').readlines()
d = data[-1]
data.pop()
data = sorted(data)
data.append(d)
print(data)

def FizzBuzz(data):
    m = int(data[-1])
    data.pop()
    lis = []
    for i in range(len(data)):
        num = int(data[i].split(':')[0])
        s = data[i].split(':')[1].replace('\n','')
        if m % num == 0:
            lis.append(s)
    if lis == []:
        lis.append(m)
    for u in lis:print(u, end ="")
        
FizzBuzz(data)

