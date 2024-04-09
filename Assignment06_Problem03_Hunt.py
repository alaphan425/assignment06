class Employee():
    def __init__(self, name, position):
        if not isinstance (name, str):
            raise TypeError ("Variable type of name must be string!")
        if not isinstance (position, str):
            raise TypeError ("Variable type of position must be string!")
        self.name = name
        self.position = position
        
    def calculate_salary(self):
        pass
    
class HourlyEmployee(Employee):
    def __init__(self, name, position, hoursWorked, hourlyRate):
        if not isinstance (hoursWorked, (int, float)):
            raise TypeError ("Variable type of hours worked must be integer or float!")
        if not isinstance (hourlyRate, (int, float)):
            raise TypeError ("Variable type of hourly rate must be integer or float!")
        super().__init__(name, position)
        self.hoursWorked = hoursWorked
        self.hourlyRate = hourlyRate
        
    def calculate_salary(self):
       return self.hourlyRate*self.hoursWorked 
    
class SalariedEmployee(Employee):
    def __init__(self, name, position, annualSalary):
        if not isinstance (annualSalary, (int, float)):
            raise TypeError ("Variable type of annual salary must be integer or float!")
        super().__init__(name, position)
        self.annualSalary = annualSalary
    
    def calculate_salary(self):
        return (self.annualSalary/52)

class CommissionEmployee(Employee):
    def __init__(self, name, position, comissionRate, target):
        if not isinstance (comissionRate, (int, float)):
            raise TypeError ("Variable type of commission rate must be integer or float!")
        if not isinstance (target, int):
            raise TypeError ("Variable type of commission target must be integer or float!")
        super().__init__(name, position)
        self.comissionRate = comissionRate
        self.target = target
    
    def calculate_salary(self):
        return self.comissionRate*self.target

def totalSalary(list):
    salarySum = 0
    for employee in list:
        salarySum = salarySum+ employee.calculate_salary()
    print("The total weekly salary of the employees is "+str(salarySum)+".")

employee1 = HourlyEmployee("John Doe", "Software Engineer", 60, 40)
employee2 = SalariedEmployee("Robert Robertson", "Electrical Engineer", 95000)
employee3 = CommissionEmployee("Jane Doe", "Computer Scientist", 100, 100)

list = [employee1, employee2, employee3]

totalSalary(list)
    
