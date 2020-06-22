#!/usr/bin/env python
# coding: utf-8

# In[1]:


def zero_error():
    try:
        x = 5/0
        print(x)
    except:
        print("There was an error dividing by zero")
zero_error()


# In[2]:


subject=["Americans ","Indians"]
verb=["play","watch"]
obj=["Baseball","Cricket"]
all_sentences = [(sub+" "+ ver + " " + ob) for sub in subject for ver in verb for ob in obj]
for sentence in all_sentences:
    print (sentence)


# In[ ]:




