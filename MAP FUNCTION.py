#MAP FUNCTION ->each object from a collection and forms a new collection
'''
a=[2,46,7,8,9,89,98]
b=[1,3,5,6,8,56,45]
c=list(map(max,a,b))
print(c)
c=list(map(min,a,b))
print(c)'''
#runtime input formats
'''
a=input("data1")
b=input("data2")
print(a+b)'''

#for strings
'''
a,b=input("data").split(",")
print(a+b)

a,b=[x for x in input().split(",")]
print(a+b)#list comprehension

a,b=(x for x in input().split(","))
print(a+b)#generator

a,b=map(str,input().split(","))
print(a+b) #MAP'''
#for intergers as input in runtime
'''
a=int(input())
b=int(input())
print(a+b)
a,b=[int(x) for x in input().split(",")]
print(a+b)#list comprehension

a,b=(int(x) for x in input().split(","))
print(a+b)#generator
#map
a,b=map(int,input().split())
'''
'''
a,b=list(map(int,input().split()))
print(a+b)
print(type(a))
a,b=tuple(map(int,input().split()))
print(a+b)
print(type(a))
a,b=set(map(int,input().split()))
print(a+b)
print(type(a))

#dictionary is special case 
a=input()
b=dict(i.split(":") for i in a.split(","))
print(b)
'''
'''
#BMI CALCULATION
while True:
    b=float(input("Enter weight:"))
    h=float(input("Enter height:"))
    r=b/(h**2)
    if (r <=18.5):
        print("under weight-->",r)
    elif (18.5< r <24.5):
        print("healthy weight-->",r)
    elif (24.5 <r<29.5):
        print("Over weight-->",r)
    else :
        print("Obesity-->",r)
        '''







































