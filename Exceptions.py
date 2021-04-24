#1. Write a program to generate Arithmetic Exception without exception handling
a = 2
b = 0
print(a/b)

#2. Handle the Arithmetic exception using try-catch block
def Calculate(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Division is not available with zero')    
Calculate(1,0)

#3. Write a method which throws exception, Call that method in main class without try block
def Calculate(a,b):
    return a/b
print(Calculate(1,0))

#4. Write a program with multiple catch blocks4
def Calculate(x,y):
    try:
        a = int(x)
        b  = int(y)
        print(a/b)
    except ValueError:
        print('enter numerical value only')
    except ZeroDivisionError:
        print('Division is not available with zero')
    except Exception as e:
        print('Error occured please try again with valid inputs .....!')
x = input('enter first no')
y = input('enter second no')
Calculate(x,y)

#5. Write a program to throw exception with your own message
def Calculate(x,y):
    try:
        a = int(x)
        b  = int(y)
        print(a/b)
    except Exception as e:
        print('Error occured please try again with valid inputs .....!')

x = input('enter first no')
y = input('enter second no')
Calculate(x,y)

#7. Write a program with finally block
def Calculate(x,y):
    try:
        a = int(x)
        b  = int(y)    
    except ValueError:
        print('enter numerical value only')
    finally:
        c =x+y
        print('printing with finally block',c)

x = input('enter first no')
y = input('enter second no')
Calculate(x,y)


#8. Write a program to generate Arithmetic Exception
a = 2
b = 0
print(a/b)

#9. Write a program to generate ArrayIndexOutOfBoundException

arr = [1,2,3,4]
k = 2
l = 0
for i in range(len(arr)):
    k +=i
    i+=arr[k]
print(l)
    
#10. Write a program to generate ClassNotFoundException
class Parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name,self.age)
a = Parents('JALA',50)
a.display()

#11. Write a program to generate FileNotFoundException
with open('new.txt') as file:
     x = file.read()
     print(x)

#12.Write a program to generate IOException


#13. Write a program to generate NoSuchFieldException

#14. Write a program to generate NoSuchMethodException

     
#15. Write a program to generate NullPointerException
     
#16. Write a program to generate NumberFormatException
     
#17. Write a program to generate StringIndexOutOfBoundsException
string = 'JALAtechnologies'
for i in range(len(string)):
    string[i] = string[len(string)]


#18. Write a program to generate SQLException


































        
