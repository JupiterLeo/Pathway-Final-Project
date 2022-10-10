#!/usr/bin/env python
# coding: utf-8

# # Final Project
# 
# # Introduction to Computer Sciences
# 
# ## Group 4:
# ###       - Nguyen Nguyen Anh Song
# ###       - Hoang Le
# 
# 

# ## Project Topic No.4: Convertor
# 
# Create a program that can be used to convert temperature, length, weight, pressure.
# Your program should have a menu displayed for the user to choose from, where are listed the convertion options
#    

# In[72]:


def length():
    value = float(input ("Which value do you want to convert ?"))
    op = input('''Select your unit convert: 
        Miles to Km (1) 
        Km to Mile (2)
        ''')
    
    if op == "1":
        result = value*0.621371
        print ('Converted Length',value,'km = ',result,'mi')
    elif op == "2":
        result = value/0.621371
        print ('Converted Length',value,'mi = ',result,'km')
    else:
        print('Please input correct unit convert: (1) or (2)')


# In[73]:


def temperature():
    value = float(input ("Which value do you want to convert ?"))
    op = input('''Select your unit convert: 
        Celsius to Fahrenheit (1) 
        Fahrenheit to Celsius (2)
        ''')
    
    if op == "1":
        result = (value * 9/5)+32
        print ('Converted Temperature',value,'Celsius = ',result,'Fahrenheit')
    elif op == "2":
        result = (value - 32)*5/9
        print ('Converted Temperature',value,'Fahrenheit = ',result,'Celsius')
    else:
        print('Please input correct unit convert: (1) or (2)')


# In[74]:


def weight():
    value = float(input ("Which value do you want to convert ?"))
    op = input('''Select your unit convert: 
        Pound to Kilograms (1) 
        Kilograms to Pound (2)
        ''')
    
    if op == "1":
        result = value*0.45359237
        print ('Converted Temperature',value,'Celsius = ',result,'Fahrenheit')
    elif op == "2":
        result = value/0.45359237
        print('Converted Temperature',value,'Fahrenheit = ',result,'Celsius')
    else:
        print('Please input correct unit convert: (1) or (2)')


# In[75]:


def pressure():
    value = float(input ("Which value do you want to convert ?"))
    op = input('''Select your unit convert: 
        Kilopascals to Pounds per Inch (1) 
        Pounds per Inch to Kilopascals (2)
        ''')
    
    if op == "1":
        result = value*12.35
        print ('Converted Temperature',value,'Celsius = ',result,'Fahrenheit')
    elif op == "2":
        result = value/12.35
        print ('Converted Temperature',value,'Fahrenheit = ',result,'Celsius')
    else:
        print('Please input correct unit convert: (1) or (2)')


# In[76]:



useranswer_yes = True

while useranswer_yes != False:
    answerType = input('''Which type of conversion?
                           Temperature (t) 
                           Length (l)
                           Weight (w)
                           Pressure (p)
                           ''')
    if answerType =="l":
        length()
    elif answerType =="t":
        temperature()
    elif answerType =="w":
        weight()
    elif answerType =="p":
        pressure()
    print('Please input correct type of conversion: (t) or (l) or (w) or (p)')
   
    answerexit = input('Do you want to exit (y/n): ')
    if answerexit =="y":
        useranswer_yes = False
    print ("Thank you")

