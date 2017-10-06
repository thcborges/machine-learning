
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt


# In[10]:


amostras = {}
amostras['age'] = []
amostras['year'] = []
amostras['nodes'] = []
amostras['survival'] = []
with open('haberman.data', 'r') as f:
    for linha in f.readlines():
        atrib = linha.replace('\n', '').split(',')
        amostras['age'].append(int(atrib[0]))
        amostras['year'].append(int(atrib[1]))
        amostras['nodes'].append(int(atrib[2]))
        amostras['survival'].append(int(atrib[3]))
print(amostras)


# In[21]:


plt.scatter(
    amostras['age'],
    amostras['year'],
    amostras['nodes'],
    sizes=amostras['nodes'],
    c=amostras['survival'],
    cmap='viridis',
    alpha=0.6
)
plt.show()


# In[29]:


fig = plt.figure()
ax = plt.subplot()
ax.scatter(
    amostras['age'],
    amostras['year'],
    amostras['nodes'],
    sizes=amostras['nodes'],
    c=amostras['survival'],
    cmap='viridis',
    alpha=0.6
)
ax.legend()
ax.set_ylabel('Year')
ax.set_xlabel('Age')
fig.savefig('haberman.png')
plt.show()


# In[27]:


ax = plt.subplot()
print(ax)


# In[33]:


fig = plt.figure()
ax = plt.subplot()
ax.scatter(
    amostras['age'],
    amostras['nodes'],
    sizes=amostras['year'],
    c=amostras['survival'],
    cmap='viridis',
    alpha=0.6
)
ax.legend()
ax.set_ylabel('Nodes')
ax.set_xlabel('Ages')
fig.savefig('haberman2.png')
plt.show()


# In[36]:


fig = plt.figure()
ax = plt.subplot()
ax.scatter(
    amostras['survival'],
    amostras['nodes'],
    sizes=amostras['age'],
    c=amostras['survival'],
    cmap='viridis',
    alpha=0.6
)
ax.legend()
ax.set_xlabel('Survival')
ax.set_ylabel('Nodes')
fig.savefig('haberman3.png')
plt.show()

