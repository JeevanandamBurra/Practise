
# coding: utf-8

# ## Please replace the astricks with the required logic in the following exercises

# ### 1) Write a python program to print from 1 to 6 except 3 and 6
# 
#        Expected Output:
# 
#        1  2  4  5 

# In[4]:



# Iterate over range from 1 to 6 using for loop
for x in range(1,6):

#check if x is 3 or 6
    if(x==3 or x==6):
        continue
#else print all using whitespace between elements    
    print(x, end = " ")    


    


# ### 2) Write a Python program to construct the following pattern, using a nested for loop.
# 
#         *
#         * *
#         * * *
#         * * * *
#         * * * * *
#         * * * *
#         * * *
#         * *
#         *

# In[6]:


# Initialize n to the maximum number of stars
n=5

# Iterate over range(n) 
for i in range(n):

#Iterate over range(i)
    for j in range(i):

#print * , use end to get  no white spaces in between the stars
        print ('*', end="")
    print('')


# Iterate over range(n)  to 0 hence reduce by -1
for i in range(n,0,-1):

#Iterate over range(i)
    for j in range(i):

#print * , use end to get  no white spaces in between the stars
        print('*', end="")
    
    print('')


# ### 3) Write a python program to print the sum of the first 10 numbers (1 to 10) using while loop
# 
#         Expected Output: 
#         The sum of the first 10 integers:  55

# In[12]:


# Initialize x to 1

x=1
# Initialize s to 0
s=0


# Iterate over x till 10
while (x<=10):

# Add each x to s
     s=s+x

# Increment x by 1
     x=x+1

#when x>10, print s
print("The sum of the first 10 integers: ",s)



# ### 4) We use break statement to terminate the while loop without completing all the iterations. The program control goes outside the while and the next print statement is executed. Q. Repeat the while using “break” and print the sum of the first 10 integers
# 
#         Expected Output:
#         The sum of the first 10 integers is: 55

# In[13]:


# Initialize x to 1
x=1

# Initialize s to 0
s=0

# Infinite loop using while
while (True):
    
#check for x =11
     if (x==11):
          break    

# Add each x to s
     s=s+x

#Increment x by 1
     x=x+1

#print sum s
print('The sum of first 10 numbers is:', s) 


# ### 5) Print the whether the number is positive or negative

# In[18]:


#initialize any negative number or positive number
num = 0

#check if num>0
if (num>0):

#print the number is positive
    print("positive number")

#use elif to check number is zero
elif (num==0):
    print("Zero")

#else print the number is negative
else:
    print("negative number")

