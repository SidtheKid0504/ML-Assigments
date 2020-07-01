#!/usr/bin/env python
# coding: utf-8

# In[7]:


import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition
from sklearn.decomposition import PCA
from sklearn import datasets


# In[8]:


iris = datasets.load_iris()


# In[9]:


X_reduced = PCA(n_components=3).fit_transform(iris.data)
Y = iris.target

fig = plt.figure(1, figsize = (8, 6))
ax = Axes3D(fig, elev= -150, azim= 110)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c = Y, cmap = plt.cm.rainbow_r)

ax.set_title("First Three PCA Directions")
ax.set_xlabel("1st Eigenvector")
ax.set_ylabel("2nd Eigenvector")
ax.set_zlabel("3rd Eigenvector")

plt.show()


# In[ ]:




