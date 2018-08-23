
# coding: utf-8

# ## 1.1) The function "echo_name" takes 2 parameters: a string value, "name1"and an integer value, "echo_int". It returns a string that is a concatenation of "echo_int" copies of "name1".

# In[20]:


def echo_name(name1, echo_int):
            print(name1*echo_int)


# In[22]:


echo_name("Hi",0)


# In[23]:


echo_name=(lambda name1,echo_int:name1*echo_int )
result = echo_name ("acadgild",5)
print(result)


# ## 2) Convert temperature in Celsius to Fahrenheit using map() and lambda functions

# In[26]:


Celsius = [49.2, 26.5, 47.3, 47.8]
    
Fahrenheits=list( map(lambda x: (float(9)/5)*x + 32, Celsius))
 
print("Temperature lists in Celsius:",Fahrenheits)


# ## 3) The function filter(function, list) filters out all the elements of a list, for which the function function returns True

# In[27]:


def vowel_check(char):
    if (char.isalpha() == True):
        if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
            return True
        else:
            return False


# In[29]:


fib = [0,1,1,2,3,5,8,13,21,34,55]
result = list(filter(lambda x: x % 2 == 0, fib))
print (result)


# In[33]:


str1='welcome to Acardgild'
vowels=['a','e','i','o','u','A','E','I','O','U']
vowels=list(filter(lambda letter: letter in vowels, str1))
print(vowels)


# ## 4) Use generator expression to print out only alphabets from the following string

# In[40]:


string = "123@Welc34ometo12@ac#adGild"

def alph(str):
    return ''.join([c for c in string if c.isalpha()])

alph(string)


# In[52]:


# option 2 but not exactly 
string = "123@Welc34ometo12@ac#adGild"

x=([c for c in string if c.isalpha()])
print (x)


# ## 5) Implement a function longestWord() that takes a list of words and returns the longest one.

# In[70]:


def longestWord(arg_word):
    max_len = max(len(x) for x in arg_word)
    return [y for y in arg_word if len(y) == max_len]


# In[71]:


word= ["January","Feburary","March","April","May","June","July"]
longestWord(word)

