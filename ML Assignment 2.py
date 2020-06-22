#!/usr/bin/env python
# coding: utf-8

# In[12]:


n = 5


for i in range(n):
    for j in range(i):
        print('*', end="")
    print('')
    
for i in range(n,0,-1):
    for j in range(i):
        print("*", end="")
    print("")


# In[19]:


a = input()[::-1]
print(a)


# In[ ]:




