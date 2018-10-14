'''
Dunder stands for Double Underscore

https://dbader.org/blog/python-dunder-methods'''

class employee:
    raise_amount=1.04  #Class Variable

    def __init__(self, first, last,pay):     #Initialize instances automatically
        self.first = first
        self.last = last
        self.pay = pay
        self.email= first+ '.' + last +'@email.com'



    def fullname(self):
            return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)


    def __repr__(self):     #Unambiguous representation of an object . Used for logging, Debugging etc.
        return "Employee('{}', '{}', '{}')".format(self.first,self.last,self.pay)

    def __str__(self):      #Meant to be more readable representation of an object. Used for display to the end-user
        return "{} {}".format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay + other.pay
    def __len__(self):
        return len(self.fullname())

emp_1 = employee('John', 'Doe',20000)
emp_2 = employee('John', 'Smith',30000)

print(emp_1)
'''Output before defining __repr__ and __str__  : <__main__.employee object at 0x0070A030>
 Output after defining __repr__ :  Employee('John', 'Doe', '20000')
  Output after defining __str__ :   John Doe John.Doe@email.com
 
 
 '''

print(repr(emp_1))
print(str(emp_1))


print(emp_1.__repr__())
print(emp_1.__str__())




#___add__

print(int.__add__(1,2))
print(str.__add__('a','b'))

print(emp_1+emp_2)   #add emp based on pay and return added pay

#___len__

print(len('test'))
print('test'.__len__())

print(len(emp_1))       #returns length of employee's full name