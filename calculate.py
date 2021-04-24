import math
# step:-1 creating a classes for the both basic and scientific calculations..................!
class BaseCalculate:
    result = None
    def __init__(self, a , operator, b):
        self.a = a
        self.operator = operator
        self.b = b
    def checkInt(self):
        try:
            self.a = int(self.a)
            self.b = int(self.b)
        except Exception as e:
            print('please enter a numeric value')
    def checkSecondNum(self):
        if self.b ==0:
            print("Second Num should be >0 ")
        else:
            BaseCalculate.result = self.a / self.b
    def doCalculation(self):
        self.checkInt()
        if self.operator == 'add':
            BaseCalculate.result = self.a + self.b
        elif self.operator == 'sub':
            BaseCalculate.result = self.a - self.b
        elif self.operator == 'mul':
            BaseCalculate.result = self.a * self.b
        elif self.operator == 'div':
            self.checkSecondNum()
    def getResult(self):
        print(BaseCalculate.result)
class ScientficCalculate:
    result =0
    def __init__(self,a,operator):
        self.a = a
        self.operator = operator
    def checkDouble(self):
        try:
            self.a = float(self.a)
        except:
            print('Give the input in numbers')
    def doCalculation(self):
        self.checkDouble()
        if self.operator =='sin':
            ScientficCalculate.result = math.sin(math.radians(self.a))
        elif self.operator =='cos':
            ScientficCalculate.result = math.cos(math.radians(self.a))
        elif self.operator =='tan':
            ScientficCalculate.result = math.tan(math.radians(self.a))
        elif self.operator =='log':
            ScientficCalculate.result = math.log(math.radians(self.a))
    def getResult(self):
        print(ScientficCalculate.result)


#step:-2 created a class calculator to do normal calculation bycreating instance to base calculate class
class Calculator:
    def __init__(self,first_no,operator,second_no):
        self.first_no = first_no
        self.operator = operator
        self.second_no = second_no
    def userInput(self):
        obj = BaseCalculate(self.first_no,self.operator,self.second_no)
        obj.doCalculation()
        obj.getResult()

#step:-3 created a class ScientficCalculator to do normal calculation by inheriting properties from   Scientificcalculate class
class ScientficCalculator(ScientficCalculate):
    def __init__(self,num,operator):
        super().__init__(num,operator)
        self.num = num
        self.operator = operator
    def userInput(self):
        self.doCalculation()
        self.getResult()

#stpe 4:-created a class to get inputs from the user based on the type of operation user want's to do
# with and applied while loop for a continuos operation
class UseCalculator:
    def UserOperation(self):
        self.option = input("Enter '1' for basic; '2' for Scientfic (or) 'n' to Exit the calculation: ")
        while True:
            if self.option == '1':
                operator = input("enter operator name ex 'add','sub','mul','div' or enter 'n'  to exit: ")
                first_no = input('Enter firs num: ')
                second_no = input("enter second no: ")
                if operator == 'n':
                    break
                else:
                    obj = Calculator(first_no,operator,second_no)
                    obj.userInput()
            elif self.option == '2':
                try:
                    operator = input("enter the operator for ex 'sin','cos','tan' or 'log' or 'n' to exit: ")
                    num = int(input('Enter the Degree value: '))
                    if operator == 'n':
                        break
                    else:
                        obj = ScientficCalculator(num,operator)

                        obj.userInput()
                except Exception as e:
                    print('give value in numbers')
            elif self.option=='n':
                break
obj = UseCalculator()
obj.UserOperation()