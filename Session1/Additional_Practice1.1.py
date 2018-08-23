
# coding: utf-8

# ## Install Jupyter notebook and run the first program and share the screenshot of the output.

# In[17]:


v1='Hello'
v2='Jeevan!'
v3='Welcome to DataScience Class.'

print (v1+" "+v2+" "+v3)


# ## 2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[21]:


#option1
lst=range(2000,3201)
list(filter(lambda a:a%7==0 and a%5!=0,lst))


# In[26]:


#option2
def numbe(lst):
    return list(filter(lambda a:a%7==0 and a%5!=0,lst))


# In[28]:


lst=range(1,20)
numbe(lst)


# ## 3. Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[38]:


def RevName():
    FName= input("Enter First Namr :")
    LName=input("Enter Last Name :")
    return print('Hello '+LName+" "+FName+" "+'Welcome!')

RevName()



# ## 4. Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r3

# In[37]:


def sphereVol(x):
    pi=3.183
    r=x/2
    v=4/3*pi*r**3
    print('The Volume of Sphere with Diameter:{} is :'.format(x),v)

sphereVol(12)

