#!/usr/bin/env python
# coding: utf-8

# In[1]:


warning = 'You must quit smoking!' #

print(len(list(warning)))


# In[5]:


warning = 'You must quit smoking!'

print(list(warning))


# In[6]:


empty_list_1 = []
empty_list_1.append('tunahan')
empty_list_1.append('bu sporu yapıyor')

print(len(empty_list_1))
print(empty_list_1)


# In[7]:


city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
city.insert(2, 'Stockholm')

print(city)


# In[9]:


city = ['New York', 'London', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
city.insert(0, 'Adana')

print(city)


# In[14]:


city = ['New York', 'London', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
city.remove('London')
print(city)  


# In[25]:


city = ['New York', 'Stockholm', 'Istanbul', 'Seoul', 'Sydney', 'Addis Ababa']
city.del(2)
print(city)  


# In[33]:


my_list = [1, 3, 5, 7]
list(my_list)


# In[29]:


a = ["apple","banana"]
b = ["grape","cherry"]


print(a, b)


# In[32]:


count = list(range(99))
print(count)
print(count[0:11:2])


# In[ ]:


x ="Clarusway"


# y = 168

# In[45]:


x = ["ali" , "veli"]
len(x)


# In[48]:



len(["1","2","3"])


# In[5]:


numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
dict = {i:numbers.count(i) for i in numbers}
print (dict)    #or print(my_dict) in python-3.x


# In[6]:





# In[10]:


a="%.2f"
type (a)


# In[11]:


x = 12
y = x + 21
x = 2
print(y//x)


# In[13]:


print(12 + 21)


# In[15]:


print("1" + str("1"))


# In[19]:


number="32"
print(1988 + int(number))


# In[23]:


print("xyyzxyzxzxyy".count('xyy',2,11))



# In[24]:


print("abcdefcdghcd".split('cd'))


# In[ ]:


colors = ['red', 'purple', 'blue', 'yellow', 'green']
print(colors[2])  # If we start at zero, 
# the second element will be 'blue'.

