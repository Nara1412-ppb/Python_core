class Employee:
    company = 'Jala_Tech'
    project_name = 'Dataai'
    def __init__(self,name,emp_id):
        self.name = name
        self.emp_id = emp_id
        print('printing all the variables in the main method',self.name,self.emp_id,Employee.company,Employee.project_name)
    @staticmethod
    def employee11(Name,Emp_id):
        print('instance variable in static method of employee1', Name,Emp_id)
        
    @staticmethod
    def employee22(Name,Emp_id): 
        print('instance variable in static method of employee2',Name,Emp_id)

    def employee1(self):
        print('static variable in instance method of employee1', Employee.company, Employee.project_name)

    def employee2(self):
        print('static variable in instance method of employee2', Employee.company, Employee.project_name)
e1 = Employee('Narasimha',1)
e1.employee1()
e2 = Employee('Ratheesh',2)
e2.employee2()

Employee.employee11('Sarat',3)
Employee.employee22('prasanth',4)
