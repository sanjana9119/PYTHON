#MATH MODULE
#The math module in Python provides mathematical functions and constants. It is a built-in module, so you only need to import it.
#The ceil() function is used to round a number up to the nearest integer.
#math.ceil(x) → rounds up (toward positive infinity).
#math.floor(x) → rounds down (toward negative infinity).
'''
import math
print(math.pi)
print(math.pi*3)
print(math.sqrt(2))
print(math.pow(2,2))
print(math.log(10))
print(math.tan(45))
print(math.cos(60))
print(math.sin(30))
print(math.ceil(4.9))
print(math.floor(6.9))
'''
#FROM MODULE
#from math import sqrt... ani tesukunte malli manam print lo math ani mention cheyodhu
'''
from math import pi,sqrt,log,tan,cos
print(pi)
print(sqrt(4))
print(log(10))
print(tan(90))
print(cos(30))
'''
#system module
'''
import sys
print(sys.path)
'''
#OSmodule
'''
import os
print(os.path)
print(os.getcwd())#currednt working directory
print(os.listdir())#list directory
print(os.chdir("C:\\Users\\navan\\Downloads"))#changing your directory
print(os.listdir())
print(os.mkdir("july27"))#making new directory in above path
print(os.listdir())#this should again list directory in above path
'''
#RANDOM MODULE
#random module is used to generate random numbers in python and
#randint function is used and this function is defined in random module
'''
import random
a=random.sample(range(10,60),15)
print(a)

'''
#randint
#randint is use to generate single integer between number
'''
import random
a=random.randint(20,50)
print(a)
'''
#choice()
#is used to pick one number from given numbers
'''
import random
a=[1,2,3,4,5,6]
b=random.choice(a)
print(b)
'''
#DICE CODE
'''
import random
while True:
    input("enter the roll of dice")
    s=random.randint(1,6)
    print(s)
    o=input("roll again ?(y/n)")
    if o=="y":
        continue
    elif o=="n":
        break
    else:
        print("invalid option")
'''
#CALENDAR MODULE
'''
import calendar
year=2026
month=10
print(calendar.month(year,month))

import calendar
year=2026
print(calendar.calendar(year))

import calendar
y=int(input("ENTER YEAR:"))
m=int(input("ENTER MONTH:"))
print(calendar.month(y,m))
'''
#DATE
'''
from datetime import date
a=date.today()   #today is attribute
print(a)
import datetime
a=datetime.datetime.now()
print(a)

import time
a=time.time()
print(a)
b=time.localtime(a)
print(b)
print(f"today date {b.tm_mday}-{b.tm_mon}-{b.tm_year}")
print(f"today time {b.tm_hour}-{b.tm_min}-{b.tm_sec}")
print(f"today {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")

import random
import time
for i in range(10):
    a=random.randint(1,10)
    print(a)
    b=time.sleep(2)      #sleep is attribute is used to stop for some seconds
'''
#ERROR HANDLING
#1.SYNTAX ERROR -->compile error
'''
for i in range(10)  #errorthat comes in compiler is called syntax error
    print(i)
    '''
#2.RUNTIME ERROR -->during execution time it will happens
'''
a=Int(input())
b=int(input())
print(a//b)
'''

#3.LOGICAL ERROR -->error in logic (it can't be visible)
'''
a=2
b=1
if a<b:       #logic is wrong so output can not visible 
    print("less")
'''
    
#EXPECTIONAL HANDLING (is used in backend)
#TRY --> instructions from which we are expecting the exceptions
#EXPECT-->exception are raised in try block it will be handle by this block
#ELSE-->optional(no exceptions)
#FINALLY-->always it will display
'''
while True:
    a=int(input("a"))
    b=int(input("B"))
    try:               #try tho patu except or finnaly kud aundali lekapothe error osthundhi
        c=a//b
        print(c)
    except:           #manam echina value error unte adhi except lo unadhi print avuthundhi
        print("True")               #error ni print chestham exception lo
    else:#try correct aythe else and finally block print avuthundhi and try wrong aythe else print avvodhu
        print("False")
    finally:#program edhi emina finally block print avuthundhi 
        print("Program ends")
        '''
#REGEX 
#REGULAR EXPRESSION-->regular expression powerful tooles (module embeeded in python which is mainly used to find a pattern within
#   a given string or sttatement or files and we mainly used text manipulation)
#\n is used to print in nextline
#\t is used to print in tab space
#r"" --> raw string ela unte ala print avuthundhi
#rstring
'''
a="sanjana\nreddy\t3rd year"
print(a)

a=r"sanjana\nreddy\t3rd year" #r means raw string it print same in the string dontchange anything  
print(a)
'''
#compile(),search(),findall(),split(),sub()
#sequence characters
'''
\w-->it matches alphanumeric
\W-->it matches non-alphanumeric
\d-->it matches any digit
\D-->it matches non digit
\s-->it matches white spaces
\S-->it matches non-white spaces

#compile()
import re
a="mat cup match money cash cat dog"
b=re.compile(r"m\w\w\w\w")
print(b)

#search() okate word print avuthundhi 
c=b.search(a)
print(c)

c=re.search(r"m\w+",a)
print(c)

#findall() print totoal 
d=re.findall(r"m\w+",a)
print(*d)

#split() oka okati word split avvadaniki use chestham 
e=re.split(r"m",a)
print(a)
f=re.split(r"\s",a)
print(f)

#sub() #replacing "m" with "a"
g=re.sub(r"m","a",a)
print(g)

import re
a="match , map,dog ,1,2,3,"
c=re.findall(r"\d+",a)
print(c)
'''













































