'''n=int(input())
student=[]
for i in range(1,n+1):
    stud=int(input(f"enter the student{i}marks"))
    student.append(stud)
for i in student:
    print(i)                                    #student marks analysis
print("Total number os students-->",n)
print("The highest marks-->",max(student))
print("The lowest marks -->",min(student))
print("The total marks-->",sum(student))
r=sum(student)/n
print("Average of marks-->",r)'''

#annonymous function
#syntax a=lambda arg:expr #lambda keyword
'''
def check(n):
    print(2*n+5)
check(5)'''
'''
def check(n):
    print(2*n+5)
n=int(input())
check(n)'''
'''
a=lambda x:2*x+5
print(a(10))
'''
'''
n=int(input())
a=lambda n:n*2-10
print(a(n))'''
'''
while True:
    a=int(input())
    b=int(input())
    c=lambda a,b:a*b
    print(c(a,b))'''
'''
a="CodeGnan"
c=lambda a:a.upper()
print(c(a))
b="python course"
d=lambda b:b.title()
print(d(b))
'''
'''
a=input("Firstname:")
b=input("Lastname:")
c=lambda a,b:(a+" "+b).title()
print("fullname:",c(a,b))
'''
'''
#generator taking input in oneline 
a,b=[x for x in input("Enter names:").split(",")]
c=lambda a,b:(a+" "+b).title()
print("fullname:",c(a,b))'''
#filter it must two variables undali and manaki kavalasinavi matrame esthundhi vere vi remove chesthundhi
'''
a=[10,20,30,60,3,5]
for i in a:
    if i%2==0:
        print(i)'''
'''
a=[10,20,30,60,3,5]
b=list(filter(lambda x:x%2==0,a))
print(b)'''
'''
a=[]
b=()
c={}
d=set()
print(type(a))
print(type(b))
print(type(c))
print(type(d))'''
'''
a=[[],(),{},set(),"",None,3,5.6,"sanjana"]
b=list(filter(None,a))
print(b)'''




































