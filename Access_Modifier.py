#1. Create a class with PRIVATE fields, private method and a main method. Print the fields
#in main method. Call the private method in main method.
class Parent:
    _name = None
    _age = None
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def _private(self):
        print('this is a private method')
    def main(self):
        print('Name: ',self._name)
        print('Age: ',self._age)
        self._private()
class Child(Parent):
    def __init__(self,name,age):
        Parent.__init__(self,name,age)
    def AccessPrivate(self):
        print('Name: ',self._name)
        print('Age: ',self._age)
        self._private()
        
parent_obj = Parent('Narasimha',23)
parent_obj.main()
child_obj=Child('Jala',50)
child_obj.AccessPrivate()

#2. Create a class with DEFAULT fields and methods. Access these fields and methods
#from any other class in the same package
class Parent:
    def ParentDefault(self,name = 'Narasimha',age = 23):
        self.name = name
        self.age = age
        print('this is a parent default method')

class Child(Parent):
    def ChildDefault(self):
        print('this is child default')
    def GetParentDefaultField(self):
        print(self.name)
        print(self.age)
    def GetParentDefault(self):
        self.ParentDefault()
obj = Child()
obj.ChildDefault()
obj.GetParentDefault()
obj.GetParentDefaultField()

#3. Create a class with PROTECTED fields and methods. Access these fields and methods
#from any other class in the same package.
class Parent:
    __name = 'Narasimha'
    __age = 23
    def __protected(self):
        print('this is a private method')
    def main(self):
        print('Name: ',self.__name)
        print('Age: ',self.__age)
        self.__protected()
class Child(Parent):
    def AccessProtected(self):
        self.main()
obj = Child()
obj.AccessProtected()

#4. Create a class with PUBLIC fields and methods.
#Access the public methods and fields from any class in the same package or different
#package.
class Parent:
    name = 'Narasimha'
    age = 23
    def public(self):
        print('this is a public method')
    def main():
        print('calling from parent class')
class Child(Parent):
    def AccessPublic(self):
        print('calling from child class')
        print(self.name,self.age)
        self.public()
obj = Child()
obj.AccessPublic()
