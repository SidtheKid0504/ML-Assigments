#!/usr/bin/env python
# coding: utf-8

# In[1]:


def do_sum(x1, x2): 
    return x1 + x2

def my_reduce(func, ite):
    first = ite[0]
    for i in ite[1:]:
        first = func(first, i)
    return first

print(my_reduce(do_sum, [1, 2, 3, 4]))


# In[2]:


def my_filter(delete, ls):
    return [x for x in ls if x != delete]
          
li = [1, 2, 3, 4, 5, 6, 7, 8]
my_filter(2,li)



# In[3]:


letters = "ACADGILD"
alphabet = [ alph for alph in letters ]
print (str(alphabet))


# In[4]:


letter_list = ['x','y','z']
result = [ l*num for l in letter_list for num in range(1,5)  ]
print(str(result))


# In[5]:


number_list = [2,3,4]
output = [[a+n] for a in number_list for n in range(0,3)]
print(str(output))


# In[6]:


number_list_2 = [2,3,4,5]
output2 = [[a+n for a in number_list_2] for n in range(0,4)]
print(str(output2))


# In[7]:


patterned_numbers=[1,2,3]
output3 = [ (b,t) for t in patterned_numbers for b in patterned_numbers]
print(str(output3))


# In[ ]:




