'''
Polymorphism is the ability of an object to take on many forms.
The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.
'''

class Parrot:
     def fly(self):
         print("Parrot can fly")

     def swim(self):
         print("Parrot can't swim")

class Penguin:
    def fly(self):
        print('Penguin can \'t fly')

    def swim(self):
        print('penguin can swim')

#common interface

def flying_test(bird):
    bird.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()

#passing the object

flying_test(blu)
flying_test(peggy)