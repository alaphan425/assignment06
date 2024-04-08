class Employee():
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def calculate_salary(self):
        pass
    
class HourlyEmployee(Employee):
    def __init__(self, name, position, hoursWorked, hourlyRate):
        super().__init__(name, position)
        self.hoursWorked = hoursWorked
        self.hourlyRate = hourlyRate
        
    def calculate_salary(self):
       return self.hourlyRate*self.hoursWorked 
    
class SalariedEmployee(Employee):
    def __init__(self, name, position, annualSalary):
        super().__init__(name, position)
        self.annualSalary = annualSalary
    
    def calculate_salary(self):
        return (self.annualSalary/52)

class CommissionEmployee(Employee):
    def __init__(self, name, position, comissionRate, target):
        super().__init__(name, position)
        self.comissionRate = comissionRate
        self.target = target
    
    def calculate_salary(self):
        return self.comissionRate*self.target

def totalSalary(list):
    salarySum = 0
    for employee in list:
        salarySum += salarySum+ employee.calculate_salary()
    print("The total weekly salary of the employees is "+str(salarySum)+".")

employee1 = HourlyEmployee("John Doe", "Software Engineer", 60, 40)
employee2 = SalariedEmployee("Robert Robertson", "Electrical Engineer", 95000)
employee3 = CommissionEmployee("Jane Doe", "Computer Scientist", 100, 100)

list = [employee1, employee2, employee3]

totalSalary(list)

    
