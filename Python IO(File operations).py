#1. Write a program to write text to .txt file using OutputStream
with open('myfile.txt','w') as file:
    file.write('This is JALA Techologies \n')

#2. Write a program to append text from .txt file
with open('myfile.txt','a') as file:
    file.write('A software company in ')

#3. Write a program to read text from .txt file using InputStream
file = open('myfile.txt')
x = file.read()
print(x)
file.close()
#4. Reading and writing data from excel files
dict1 = {'a':[1,2,3,4],'b':[5,6,7,8]}
import pandas as pd
df = pd.DataFrame(dict1)
df.to_excel('my.xlsx',sheet_name = 'First_Sheet', index = False)
excel = pd.read_excel('my.xlsx',sheet_name = 'First_Sheet')
print(excel)


