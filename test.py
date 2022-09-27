#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT WEEK 3
# ## 25 Sep 2022
# Name: **Nguyen Nguyen Anh Song**

# **1.**

# In[11]:


num1 = int(input('Input 1st number: '))
num2 = int(input('Input 2nd number: '))
x = lambda num1,num2: num1*num2
print('The result of (',num1,'*',num2,'): ',x(num1,num2))


# **2.**

# In[12]:


r = float(input('Input the radius: '))
from math import pi
a = r**2*pi
print('The area of the cirle is: ',a)


# **3.**

# In[13]:


num1 = int(input('Input 1st number: '))
num2 = int(input('Input 2nd number: '))
op = str(input('Selection a operation (multiply:m, divide:d; add:a; subtract:s): '))
def result(num1,num2,op):
    if op == 'm':
        return num1*num2
    elif op == 'd' and num2!=0:
        return num1/num2
    elif op == 'd' and num2==0:
        print('Error: division by zero')
    elif op == 'a':
        return num1+num2
    elif op =='s':
        return num1-num2
    else:
        print('It is not an operation')
print('The result is: ',result(num1,num2,op))


# **4.**

# In[14]:


class rectangle():
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def area(self):
        return self.length*self.width    

a = int(input('Input the length of the rectangle: '))
b = int(input('Input the width of the rectangle: '))

result = rectangle(a,b)
print('The area of the rectangle is: ',result.area())


# **5.**

# In[15]:


class Shape():
    def __init__(self,name,length):
        self.name = name
        self.length = length
    def area(self):
        return 0

class Square(Shape):
    def area(self):
        return self.length**2
    def describe(self):
        return self.name
    
s = Square('square',5)
print("""The area is: 
    """,s.area())
print('This is a:',s.describe())

