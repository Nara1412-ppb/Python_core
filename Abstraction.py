#1. Create an abstract class with abstract and non-abstract methods.
from abc import ABC, abstractmethod
class Parent(ABC):
    @abstractmethod
    def AbstractMethod(self):
        pass
    def Method(self):
        print('this is a non abstract method')
class Child(Parent):
    def AbstractMethod(self):
        print('this is an abstractmethod')
    def display(self):
        obj = Parent()
        obj.Method()
        child = Child()
        child.AbstractMethod()
        child.Method()
    
o = Child()
o.display()
