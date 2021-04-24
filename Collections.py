#1.List operations
arrayList = ['0','1','2','3','4','5','6','7','8','9']
print(arrayList)
arrayList.append('11')
print('list after adding an element: ',arrayList)
print('iteration through list: ')
for item in arrayList:
    print(item)
arrayList.insert(10,'10')
print('array after inserting the element at index 10: ', arrayList)
arrayList.pop()
print('array after removing the element: ', arrayList)
arrayList.pop(10)
print('array after removing the element at index 10: ', arrayList)
arrayList[0] = '10'
print('array after updating an element at index 0:',arrayList)
print('2 is present at the index 2:',arrayList[2]=='2')
print('value of an element at index 3: ',arrayList[3])
print('lenght of the arrayList: ',len(arrayList))
print('checking the given no(4) is the List: ', '4' in arrayList)
arrayList.clear()
print('clearing all the elements from the list: ',arrayList)

# HeatMap


#3.HeatSet
people = {"Jay", "Idrish", "Archi"}
people.add("Daxit")
# set using iterator
for i in range(1, 6): 
    people.add(i)   
print("\nSet after adding element:", end = " ")
print(people)

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}
  
# Union using union() function
population = people.union(vampires)
  
print("Union using union() function")
print(population)
  
# Union using "|" operator
population = people|dracula

set1 = set()
set2 = set()
  
for i in range(5):
    set1.add(i)
  
for i in range(3,9):
    set2.add(i)
  
# Intersection using intersection() function
set3 = set1.intersection(set2) 
print("Intersection using intersection() function")
print(set3)
  
# Intersection using "&" operator
set3 = set1 & set2 
print("\nIntersection using '&' operator")
print(set3)

set1 = set()
set2 = set()
  
for i in range(5):
    set1.add(i)
  
for i in range(3,9):
    set2.add(i)
  
# Difference of two sets using difference() function
set3 = set1.difference(set2)
  
print(" Difference of two sets using difference() function")
print(set3)
  
# Difference of two sets using '-' operator
set3 = set1 - set2
  
print("\nDifference of two sets using '-' operator")
print(set3)

set1 = {1,2,3,4,5,6}
  
print("Initial set")
print(set1)
  
# This method will remove all the elements of the set
set1.clear()  
print("\nSet after using clear() function")
print(set1)

set1 = set()
set2 = set()
  
# Adding elements to set1
for i in range(1, 6):
    set1.add(i)
  
# Adding elements to set2
for i in range(3, 8):
    set2.add(i)
  
print("Set1 = ", set1)
print("Set2 = ", set2)
print("\n")
  
# Union of set1 and set2
set3 = set1 | set2# set1.union(set2)
print("Union of Set1 & Set2: Set3 = ", set3)  
# Intersection of set1 and set2
set4 = set1 & set2# set1.intersection(set2)
print("Intersection of Set1 & Set2: Set4 = ", set4)
print("\n") 
# Checking relation between set3 and set4
if set3 > set4: # set3.issuperset(set4)
    print("Set3 is superset of Set4")
elif set3 < set4: # set3.issubset(set4)
    print("Set3 is subset of Set4")
else : # set3 == set4
    print("Set3 is same as Set4") 
# displaying relation between set4 and set3
if set4 < set3: # set4.issubset(set3)
    print("Set4 is subset of Set3")
    print("\n")

























  
print("\nUnion using '|' operator")
print(population)
