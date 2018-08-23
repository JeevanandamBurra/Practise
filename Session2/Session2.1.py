
# coding: utf-8

# ## 1.1 Write a Python program to implement your own myreduce() function which works exactly like python builtin function reduce()

# In[179]:


def myreduce(func,lst):
    result = lst[0]
    for i in lst[1:]:
        result = func(result, i)
    return result
    


# In[180]:


def reducesum(lst):
    return myreduce(lambda a,b:a+b,lst)
        
reducesum([1,2,3,4,5])


# ## 1.2 Write a Python program to implement your own myfilter() function which works exactly like python builtin function filter()

# In[148]:


# other option we can do with list as well same like reduce 
def myfilter(fun, lst,initializer=None):
    New_lst=iter(lst)
    if initializer is None:
        initializer = bool
    for x in New_lst:
        if fun(x):
            yield x


# In[149]:


seq=[1,2,3,4]
list(myfilter(lambda item:item%2==0,seq))


# ## 2. Implement list comprehensions to produce the following lists.

# In[156]:


Value=input("Enter Text:")
result=[x for x in Value]
print(result)


# In[162]:


Value=list(input('Enter list of items:'))
result = [ item*num for item in Value for num in range(1,5)]
print (result)


# In[163]:


Value=list(input('Enter list of items:'))
result = [ item*num for num in range(1,5) for item in Value]
print (result)


# In[172]:


Value = [2,3,4]
result = [ [item+num] for item in Value for num in range(0,3)]
print(result)


# In[173]:


Value = [2,3,4,5]
result = [ [item+num for item in Value] for num in range(0,4)]
print(result)


# In[174]:


Value = [1,2,3]
result = [ (b,a) for a in Value for b in Value]
print(result)


# ## 3.Implement a function longestword that takes list of words and returns longest word.

# In[183]:


def Longestword(lst):
    return myreduce( (lambda x,y:y if len(y) > len(x) else x), lst)
    
    


# In[184]:


lst=["Hi","Jeevan","How",'are',"U"]
Longestword(lst)

