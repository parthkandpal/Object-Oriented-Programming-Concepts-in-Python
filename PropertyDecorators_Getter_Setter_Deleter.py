class employee:
    raise_amount=1.04  #Class Variable

    def __init__(self, first, last,pay):     #Initialize instances automatically
        self.first = first
        self.last = last
        self.pay = pay


    @property           #method email() can be accessed as an attribute email
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)

    @property          #method fullname() can be accessed as an attribute fullname
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last


    @fullname.deleter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=None
        self.last=None


emp_1 = employee('John', 'Doe',20000)
emp_2 = employee('John', 'Smith',30000)

emp_1.fullname='Jim don'   #calls @fullname.setter and sets first name and last name

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname      #call @fullname.deleter