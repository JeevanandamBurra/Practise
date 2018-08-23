
# coding: utf-8

# ### 1) Write a single statement to print all multiples of 4 between 0 and 100 inclusive

# In[14]:


print({4*n for n in range(26)})


# In[9]:


print (list(range(0,101,4)))


# ### 2) Write a function that returns true if a given number is prime

# In[10]:


def prime(n):
    if (n>1):
        for i in range(2,n):
            if(n%i)==0:
                print(n,'is not a prime')
                break
            else:
                print(n,'is a prime')
    else:
            print(n,'is not a prime')
            
    
prime(5)


# ### 3) Use the function to filter out all the prime numbers between 1 and 100 inclusive

# In[36]:


def Listprime(n1,n2):
    print('List of Prime Numbers Range from {0} to {1}'.format(n1,n2))
    for num in range(n1,n2):
        if all(num%i!=0 for i in range(2,num)):
            print (num)
                
Listprime (2,10)  



# In[32]:


for num in range(2,10):
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            print(num)
            break
    


# ### Write a program to generate the following array

# In[ ]:


1 2 3 4 5
1 4 9 16 25
1 8 27 64 125
1 16 81 256 625 
1 32 243 1024 3125


# ### 4) Write a  function to get the side of a square and return its perimeter

# ### Write code to get the side from user and call the function to print perimeter. Also use format in the print statement to print the perimeter to 2 decimal places.

# In[17]:




