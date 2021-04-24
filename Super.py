#using super method in the class for constructur and for method

class Parent:
    def __init__(self,name,emp_id,age):
        self.name = name
        self.age = age
        self.emp_id = emp_id
    def display(self):
        print('employee age',self.age)
class Child(Parent):
    def __init__(self,name,emp_id,age):
        super().__init__(name,emp_id,age)
    def display(self):
        super().display() 
        print('Name',self.name)
        print('Emp_id',self.emp_id)

obj = Child('NArasimha',123,23)
obj.display()

