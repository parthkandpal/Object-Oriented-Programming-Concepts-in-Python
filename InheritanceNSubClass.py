'''
Inheritance
In object-oriented programming, inheritance is the mechanism of basing an object or class upon another object (prototypical inheritance) or class (class-based inheritance),
retaining similar implementation. In most class-based object-oriented languages, an object created through inheritance
(a "child object") acquires all the properties and behaviors of the parent object(Except: constructors, destructor, overloaded operators and friend functions of the base class).




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
        self.pay=int(self.pay * self.raise_amount)

class developer(employee):   #sub class of employee and inheriting employee
    raise_amount = 1.10


    def __init__(self, first, last,pay,prog_lang):
        super().__init__(first,last,pay)                                  #employee.__init__(self,first,last,pay)
        self.prog_lang=prog_lang

class Manager(employee):
    def __init__(self, first, last,pay,employees=None):
        super().__init__(first,last,pay)                                  #employee.__init__(self,first,last,pay)

        if employees is None:
            self.employees=[]
        else:
            self.employees=employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())










dev_1=developer('Parth','kandpal',50000,'Python')
dev_2=developer('Steve','Smith',60000,'Java')
print(help(developer))

'''
 Method resolution order:
 |      developer       #derived class
 |      employee        #base class
 |      builtins.object
'''

print(dev_1.first)
print(dev_1.pay)
dev_1.raise_amount
print(dev_1.pay)


mgr_1=Manager('Sue','Smith',90000,[dev_1])
print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()


'''
isinstance() tells us if an object is an instance of particular class.
issubclass() tells us if a clas is subclass of another class.
'''

print(isinstance(mgr_1,Manager))   #True
print(isinstance(mgr_1,employee))   #True
print(isinstance(mgr_1,developer))  #False

print(issubclass(Manager,developer))    #False


