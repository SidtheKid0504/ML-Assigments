#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Triangle_Lengths:
    def __init__(self, a, b, c,s):
        self.a = a
        self.b = b
        self.c = c
        self.s = s
class Triangle_Area:
    def __init__(self, a, b, c, s):
        self.a = a
        self.b = b
        self.c = c
        self.s = s
    
    def calcAge(a, b, c):
        s = (a+b+c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(area)
        
z = Triangle_Area.calcAge(int(input()), int(input()), int(input()))


# In[3]:


def length_conv(some_words):
    a_length = []
    for word in some_words:
        a_length.append(len(word))
    return a_length

someList = ["four", 'five', 'dhdsbd']
length_conv(someList)


# In[4]:


def is_vowel(char):
    the_vowels = ('a', 'e','i', 'o', 'u')
    if char not in the_vowels:
        return False
    else:
        return True
is_vowel('a')


# In[ ]:




