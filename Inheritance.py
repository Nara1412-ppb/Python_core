class A:
    def methodA1(self):
        print('this is the first method in class A')
    def methodA2(self):
        print('this is the second method in class A')
    def OverMethodA(self):
        print('overriding method in class A')
class B(A):
    def methodB1(self):
        print('this is the first method in class B')
    def methodB2(self):
        print('this is the second method in class B')
    def OverMethodB(self):
        super().OverMethodA()
        print('overriding method in class B')

class C(B):
    def methodC1(self):
        print('this is the first method in class C')
    def methodC2(self):
        print('this is the second method in class C')
    def OverMethodC(self):
        super().OverMethodB()
        print('overriding method in class C')
        
class Main:
    def main(self):
        objA = A()
        objA.methodA1()
        objA.methodA2()
        objB = B()
        objB.methodB1()
        objB.methodB2()
        objC = C()
        objC.methodC1()
        objC.methodC2()
        objC.OverMethodC()
obj_main = Main()
obj_main.main()


















    
    
    
    
