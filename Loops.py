#1. Write a program to print “Bright IT Career” ten times using for loop
str1 = "Bright IT Career"
for i in range(10):
    print(str1)
    
#2. Write a program to print 1 to 20 numbers using the while loop
i = 1
while i<21:
    print(i)
    i+=1

#4. Write a program to print the odd and even numbers.
lst = [1,2,3,4,5,6,7]
evens = list(filter(lambda x:x%2==0,lst))
odds = list(filter(lambda x:x%2==1, lst))
print(evens)
print(odds)

#5. Write a program to print largest number among three numbers.
lst = [5,8,7]
largest_num = 0
for i in lst:
    if i>largest_num:
        largest_num=i
print(largest_num)


#6. Write a program to print even number between 10 and 100 using while

n = 11
even_list = []
while n>10 and n<100:
    if n%2==0:
        even_list.append(n)
    n+=1
print(even_list)

'''without if condition'''
n = 12
even_list = []
while n>10 and n<100:
    even_list.append(n)
    n+=2
print(even_list)

#8. Write a program to find Armstrong number or not

def ArmstrongNo(n):
    k = 0
    if int(n)>0:
        for i in range(len(n)):
            k+=int(n[i])**len(n)
        if k ==int(n):
            return 'Armstrong no'
        return 'not Armstrong no'
    return 'please provide a no greater then 0'       
num = input('enter a num >0 : ')
print(ArmstrongNo(num))

#9. Write a program to find the prime or not.
def PrimeNumber(n):
    if n>1:
        if n==2:
            return '{} is an even prime num'.format(n)
        for i in range(2,n):
            if n%i==0:
                return '{} is not a prime num'.format(n)
            return '{} is a prime num'.format(n)
    return 'please enter a num greater than 1'
        
num = int(input('please enter a positive num >1: '))
print(PrimeNumber(num))

#10. Write a program to palindrome or not.
def IsPalindrome(n):
    x = n[::-1]
    if x==n:
        return '{} is a palindrome'.format(n)
    return '{} is not a palindrome'.format(n)
n = input('Input to check wether it is a palindrome or not: ')
print(IsPalindrome(n))

#13. Program for multiple if else statement(Largest number in 10,20 and 30)
lst = [10,20,30]
largest_num = 0
if lst[0]>lst[1]:
    if lst[0]>lst[2]:
        largest_num = lst[0]
    else:
        largest_num = lst[2]
else:
    if lst[1] > lst[2]:
        largest_num = lst[1]
    else:
        largest_num = lst[2]    
print(largest_num)


































































