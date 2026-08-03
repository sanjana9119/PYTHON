#FILE HANDLING
#WRITE
'''
a=open("sanjana.txt","w")
a.write("she is full stack developer")
a.close()

a=open("sanjana.txt","w") #override avuthundhi manam kotha gha edhi write chesthe adhe untundhi mundhu dhi erase avuthundhi
a.write("she is python developer")
a.close()
'''
#append()
''' #text previous gha unadhaniki "add" avuthundhi append use chesthe 
a=open("sanjana.txt","a")
a.write("\tshe is job holder ")
a.close()
'''
#runtime input
'''1-->
a=open("sanjana.txt","w")
a.write(input("data"))
a.close()

2--->
a=open("sanjana.txt","w")
b=input("data")
a.write(b)
a.close()
'''
#read()
'''
a=open("sanjana.txt")
print(a.read())  #it will display entire matter in file
print(a.readline())#it will only one line
print(a.readlines())#it will display with \n all lines
print(a.read(6))#it will read only 6 lines
'''
#WRITELINES()-->it prints every object side by side
'''
names=["sanju","nani","chitti","laddu"]
a=open("sanjana.txt","w")
a.writelines("\n".join(names))
a.close()
'''
a=open("C:/Users/navan/OneDrive/Desktop/codegnan/data.py")
print(a.read())

























