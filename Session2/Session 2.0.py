
# coding: utf-8

# ## 1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

# In[3]:


lst= input('Please enter some comma-separated numbers:')
New_lst=lst.split(",")
print('List :',New_lst)


# ## 2) Create the below pattern using a nested for loop in Python.
#     *
#     * *
#     * * *
#     * * * *
#     * * * * *
#     * * * *
#     * * *
#     * *
#     *

# In[11]:


def pattern(n):
    
    # For printing the upper part of pyramid
    for i in range (1, n+1): 
        for j in range (1, i+1):
             print ('*', end="")
        print('')
     
    # for printing the middle and lower part of pyramid
    for i in range (n, 1, -1):
        for j in range (i, 1, -1):
             print ('*', end="")
        print('')


# In[13]:


pattern(7)


# ## 3. Write a Python program to reverse a word after accepting the input from the user.

# In[22]:


User_Input= input('Please enter some text:')
Revr_text=User_Input[::-1]
print('Reversed Text :',Revr_text)


# ## 4. Write a Python program to print the given string in the format specified in the sample out put.
#     WE, THE PEOPLE OF INDIA, having solemnlyresloved to constitute India into SOVEREIGN,SOCIALIST,SECULAR,DEMOCRATIC REPUBLIC and to secure to all its citizens

# In[25]:


print('WE, THE PEOPLE OF INDIA,\n\thaving solemnly resloved to constitute India into SOVEREIGN,!\n\t\tSOCIALIST,SECULAR,DEMOCRATIC REPUBLIC\n\t\t and to secure to all its citizens')

