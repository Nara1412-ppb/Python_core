#1. Write a function to add integer values of an array
def IntArray(n):
    k = 0
    for i in n:
        if type(i) == int:
            k+=i
    return k
print(IntArray([1,4,6,'hii',True,7]))

#2. Write a function to calculate the average value of an array of integers
def AvgArray(n):
    total = sum(n)
    lenght = len(n)
    k = total/lenght
    return k
lst = [4,6,8,3,5]
print('Average of an array is :', AvgArray(lst))

#3. Write a program to find the index of an array element
lst = [1,4,7,3,6]
x= lst.index(7)
print('index of the given int in an array',x)

#4. Write a function to test if array contains a specific value
def ItemCheck(lst,element):
    print(f'is array {lst} contains {element}?: ', element in lst)
lst = [4,6,8,3,5]
element = 3
ItemCheck(lst,element)

#5. Write a function to remove a specific element from an array
def RemoveItem(lst,element):
    k = lst
    item = element
    k.remove(item)
    return k
lst = [4,6,8,3,5]
element = 6
print('array after removing the element from array: ',RemoveItem(lst,element))

#6. Write a function to copy an array to another array
lst = [1,2,3,4]
lst1 = lst.copy()
print(f'copy of array lst: ' , lst1)

#7. Write a function to insert an element at a specific position in the array
lst.insert(2,8)
print('array after inserting the element 8 at index 2 ',lst)

#8. Write a function to find the minimum and maximum value of an array

min_value =min(lst)
max_value = max(lst)
print('min and max values of the array: ',min_value,max_value)

#9. Write a function to reverse an array of integer values
rev_lst = lst[::-1]
print('origional array: ',lst)
print('reversed array of lst is: ',rev_lst)

#10. Write a function to find the duplicate values of an array
arr = [1,4,6,7,7,8,2,4,8]
duplicates = set(arr)
print('duplicate values are: ')
for i in duplicates:
    if arr.count(i)>1:
        print(i)
        
#11.Write a program to find the common values between two arrays
arr1 = [1,2,3,4,5]
arr2 = [3,4,4,5,6,7]
common_array = []
for i in arr1:
    for j in arr2:
        if j==i:
            if j not in common_array:
                common_array.append(j)
            
print(common_array)

#12. Write a method to remove duplicate elements from an array
arr = [1,4,6,7,7,8,2,4,8]
duplicates = set(arr)
new_arr = list(duplicates)
print(new_arr)

#13. Write a method to find the second largest number in an array
def SecondLarge(arr):
    largest_no = arr[0]
    second_large = 0
    for i in range(len(arr)):
        if arr[i]>largest_no:
            second_large = largest_no
            largest_no = arr[i]
        elif arr[i]>second_large and arr[i]<largest_no:
            second_large =  arr[i]
    return second_large
arr = [1,4,6,7,7,8,2,4,8]
print('second large in the array is: ',SecondLarge(arr))

#15. Write a method to find number of even number and odd numbers in an array
 
arr = [1,4,6,7,7,8,2,4,8]
evens = []
odds = []
for i in range(len(arr)):
    if arr[i]%2==0:
        evens.append(arr[i])
    else:
        odds.append(arr[i])
print('evens in array: ',evens)
print('odds in array: ',odds)

#16. Write a function to get the difference of largest and smallest value
def Diff(arr):
    largest_no = arr[0]
    smallest_no = arr[0]
    for i in range(len(arr)):
        if arr[i]>largest_no:
            largest_no = arr[i]
        elif arr[i]<smallest_no:
            smallest_no =  arr[i]
    return (largest_no - smallest_no)
arr = [1,4,6,7,7,8,2,4,8]
print('difference of largest and smallest value of array is: ',Diff(arr))

#17. Write a method to verify if the array contains two specified elements(12,23)

arr = [1,4,6,7,12,23,8,2,4,8]
ele1 = 12
ele2 = 23
print(f'{ele1} is in arr or not? :',ele1 in arr)
print(f'{ele2} is in arr or not? :',ele2 in arr)


#18. Write a program to remove the duplicate elements and return the new array
arr = [1,4,6,7,12,23,8,2,4,8]
new_arr = []
for i in range(len(arr)):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])
print('array after removing the duplicates: ',new_arr)

#19. Write a function to find the missing number of sorted array of 1 to 100
def FindMissing(lst):
    for i in range(1,101):
        if i not in lst:
            print(i)
x =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 2445, 46, 47, 48, 49,
    66, 67, 68, 69, 70, 71, 72, 73,94, 95, 96, 97, 98, 99]
print('missed elements in the range are: ')
FindMissing(x)

























