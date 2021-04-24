#3. Apply private, public, protected and default access modifiers to the constructor
class Parent:
    _name = None
    __company = None 
    def __init__(self,name,company,age):
        self._name = name
        self.__company = company
        self.age = age
    def Private(self):
        print('this is Private member',self._name)
    def Protected(self):
        print('this is protected member',self.__company)
    def Public(self):
        print('this is Public member',self.age)
obj = Parent('Narasimha','JALA Tech',23)
obj.Private()
obj.Protected()
obj.Public()

#4. Write constructors with return type int and String
class Parent: 
    def __init__(self,name,age):
        self.name = name
        self.age = int(age)# constructure will print types only using rint not in return
        print(type(self.name),type(self.age))

Parent('Narasimha',23)

#5. Try to call the constructor multiple times with the same object
class Parent: 
    def __init__(self,name):
        self.name = name
        print(self.name)
obj = Parent('Narasimha')
obj1 = Parent('narasimha')
obj2 = Parent('JALA Tech')
































