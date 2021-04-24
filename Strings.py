#1. Different ways of creating atrings
'''1. by using the 'str' variable name we can cnvert any variable to string
    2. we get anything in the string formate when we take input from user'''
str1 = 1234
str2 = input('enter anything')
print('before the conversion',type(str1))
print('after the conversion',type(str(str1)))
print('type of input: ',type(str2))


#2. Concatenating two strings using + operator
str1 = input('enter a string to concatinate: ')
str2 = input('enter another string to concatinate: ')
str3 = str1+str2 
print(str3)

#3. Finding the length of the string
str1 = input('enter a string to concatinate: ')
print(len(str1))

#4. Extract a string using Substring
str1 = input('enter a string to concatinate: ')
str2 = input('enter a string to extract: ')
if str2 in str1:
    print('"'+str2+'"','in','"'+str1+'"')
else:
    print('"'+str2+'"','is not in','"'+str1+'"')

#5. Searching in strings using index() this gives the lowest index of a string
sentence = 'Python programming is very easy.'
index = sentence.index('is very')
print("Substring 'is vary':", index)
# returns a value error if the substring is not found in the specified range
index1 = sentence.index('programming',10,20)
print("Substring 'programming':", index1)

#6. Matching a String Against a Regular Expression With matches()
import re    
str1 = "python is easy to learn"
match = re.match( r'(.*) is (.*?) .*', str1)
if match:
   print("matchObj.group() : ", match.group())
   print("matchObj.group(1) : ", match.group(1))
   print("matchObj.group(2) : ", match.group(2))
   print("matchObj.group(2) : ", match.groups())
   
else:
   print("No match!!")

#7. Comparing strings using the methods equals()
str1 = 'python'
str2 = 'python'
str3 = 'java'
if str1.__eq__(str2):
    print(str1,str2,'are equal')
if str1.__eq__(str3):
    print(str1,str3,'are equal')
else:
    print(str1,str3,'are not equal')


#8. equalsIgnoreCase(), startsWith(), endsWith() and compareTo()
str1 = "python is easy to learn"
if str1.startswith('p'):
    print('yes it string is starting with', str1[0])
if str1.endswith('n'):
    print('yes it string is starting with', str1[-1])


#9. Trimming strings with strip()
str1 = "---python is easy to learn---"
str2 = "---python is easy to learn---"
x= str1.rstrip('---')
y = str1.lstrip('---')
z = str2.strip('---')
print('using rstrip() we gets: ',x)
print('using lstrip() we gets: ',y)
print('using strip() we gets: ',z)


#10. Replacing characters in strings with replace()
str1 = 'java is easy to learn'
print('origional string: ',str1)
print('new string :',str1.replace('java', 'python'),'\n')
print('***********************************','\n')
str2 = 'we can replace the string using replace function'
print('origional string: ',str2)
print('new string :',str2.replace('replace', "replace()"))


#11. Splitting strings with split()
str1 = 'python _is _easy _to _learn'
x =  str1.split()
print(x)
#splitting wth a charecter
y = str1.split('_')
print(y)

#12. Converting Numbers to Strings with int()
string = '1234'
x = int(string)
print('type of string before: ',type(string))
print('type of string after: ',type(x)) 


#13. Converting integer objects to Strings
int1 = 1234
x = str(int1)
print('type of int object before: ',type(int1))
print('type of int object after: ',type(x))


#14. Converting to uppercase and lowercase
name = 'python'
upper = 'JAVA'
print('converting into upper case: ', name.upper())
print('converting into lower case: ', upper.lower())






















































































