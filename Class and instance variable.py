'''
Class
instances
class variables
regular method--takes instance as first argument called self
class method--takes class as first argument called cls  @classmethod decorator is used to make a method classmethod
static method--do not take any argument  and are like regular function but we include them in class for specific reasons       @staticmethod decorator is used to make a method classmethod
'''

class employee:
    raise_amount=1.04  #Class Variable
    num_of_employee=0
    def __init__(self, first, last,pay):     #Initialize instances automatically
        self.first = first
        self.last = last
        self.pay = pay
        self.email= first+ '.' + last +'@email.com'

        employee.num_of_employee +=1


    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)    #self.pay=int(self.pay * employee.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):               #passing class as first argument
        cls.raise_amount=amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def isworkday(day):

        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

emp_1 = employee('John', 'Doe',20000)               #instance variable
emp_2 = employee('John', 'Smith',30000)

print(emp_2.fullname())

print(employee.fullname(emp_1))


#working with Class variable
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(employee.raise_amount)

print(emp_1.__dict__)
print(employee.__dict__)

print(emp_1.raise_amount)

employee.raise_amount=1.05

emp_1.raise_amount=1.08

print(employee.raise_amount)

print(emp_1.raise_amount)

print(emp_1.__dict__)
print(employee.__dict__)


print(employee.num_of_employee)

employee.set_raise_amount(1.10)          #Class method is called here

print(employee.raise_amount)

print(emp_1.raise_amount)

print(emp_2.raise_amount)

#using classmethod as alternative constructors

emp_str_1='John-Doe-70000'
emp_str_2='Steve-Smith-50000'
emp_str_3='Jane-Don-90000'



new_employee_1=employee.from_string(emp_str_1)
print(new_employee_1.first)


#static method
import datetime

date=datetime.date(2018,10,13)      #its saturday
date2=datetime.date(2018,10,15)     #its Monday
print(employee.isworkday(date))
print(employee.isworkday(date2))
