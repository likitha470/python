class Employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary
    def showDetails(self):
        print("Role=",self.role)
        print("Department=",self.department)
        print("salary=",self.salary)
class Engineer(Employee):
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("Name=",self.name)
        print("Age=",self.age)
        super().__init__("software_engineer","IT","75000")
        



E1=Engineer("KIRAN","34")

E1.showDetails()        
        
