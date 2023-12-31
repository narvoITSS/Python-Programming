# Title:    Lab9A2
# Author:   Nicholas Arvo
# Purpose:  This program will create a class to store employee information along
#           wih methods ot access and modify that information. Two employees will
#           be created from this class and both will receive a pay raise.

def main():
    emp01 = EmployeeData("Helen Calder", "Analyst", 45000, 5)
    emp02 = EmployeeData("Fred Aramis", "Accountant", 67000, 3)
    emp01.setRaise(0.20)
    emp02.setRaise(0.15)

    objectTuple = (emp01, emp02)

    for objects in objectTuple:
        print("Employee Name: " + objects.getName())
        print("Employee Salary: " + str(objects.getSalary()))
        print("Employee Job Title: " + objects.getTitle())
        print()

class EmployeeData(object):
    def __init__(self, empName, empTitle, empyPay, empYears):
        self.name = str(empName)
        self.jobTitle = str(empTitle)
        self.salary = float(empyPay)
        self.yearsWorked = int(empYears)

    def getName(self):
        return self.name
    
    def getSalary(self):
        self.salary = "%0.2f" % (self.salary)
        return self.salary    
    
    def getTitle(self):
        return self.jobTitle
    
    def getYearsWorked(self):
        return self.yearsWorked
    
    def setRaise(self, percentageIncrease):
        self.salary = self.salary * (1.00 + percentageIncrease)
    
if __name__ == "__main__":
    main()