
class Person():
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def display(self):
        print(f"Name: {self.name}\nJob: {self.job}\nPay: {self.pay}\n")
    def lastName(self):
        return self.name.split()[-1]
    def payRise(self,ip):
        self.pay = (self.pay*(100+ip))/100
    def __repr__(self):
        return '[Personal Details: %s, %s, %s]' % (self.name,self.job,self.pay)
    def __add__(self,other):
        return self.name + " " + other.name

class Manager(Person):
    def __init__(self,name,pay):
        Person.__init__(self,name,'Manager',pay)
    def payRise(self,ip,bonus=10):
        Person.payRise(self,ip+bonus)

if __name__=='__main__':

    bob = Person('Bob Smith') # __int__ method ---> Operator Overloading
    sue = Person('Sue Jones','Dev',1000) # __init__ method ---> Operator Overloading

    bob.display()

    sue.display()      

    print(bob.lastName())

    sue.payRise(10)
    print(sue.pay)

    print(bob) # __repr__ method ---> Operator Overloading
    print(sue) # __repr__ method ---> Operator Overloading

    print(bob + sue) # __add__ method ---> Operator Overloading

    josh = Manager('Josh Hunt',10000) # Subclassing, Inheritance and Augmenting Methods
    josh.payRise(10) # Subclassing, Inheritance and Augmenting Methods
    print(josh)

class Point():
    origin = (0,0)

    def __init__(self,t):
        print('Point created')
        self.x = t[0]
        self.y = t[1]
    
    def distance(self,other):
        return ((self.x-other.x)**2 + (self.y-other.y)**2)**(0.5)

p = Point((2,3))
q = Point((3,4))

print(p.distance(q))


