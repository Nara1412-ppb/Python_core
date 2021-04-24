#1. Write a function for arithmetic operators(+,-,*,/)
def Arithmetic(a,b,operation=None):
    try:
        x = int(a)
        y = int(b)
    except Exception as e:
        print(e,' please try again')
    if operation=='Add':
        return x+y
    elif operation=='Sub':
        return x-y
    elif operation =='Mul':
        return x*y
    elif operation =='Div':
        if y!=0:
            return x/y
        return 'please input second no >0'
    return 'please select the correct operation'
a = input('enter first no: ')
b = input('enter second number: ')
operation = input('select an operation: ')
print('result is: ',Arithmetic(a,b,operation))

#4. Write a program to find the two numbers equal or not.
a = int(input('enter  first no: '))
b = int(input('enter second no: '))
if a==b:
    print('Two numbers are equal')
else:
    print('the Two numbers are not equal')

#7. Print the smaller and larger number
a = int(input('enter  first no: '))
b = int(input('enter second no: '))
if a>b:
    print('larger no:',a)
    print('smaller no: ',b)
elif a<b:
    print('larger no:',
          b)
    print('smaller no: ',a)
else:
    print('both the numbers are equal')
