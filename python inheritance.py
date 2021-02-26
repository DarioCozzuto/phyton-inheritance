#Links
#https://micropyramid.medium.com/understanding-self-and-init-method-in-python-class-c9018db5fc8a
#https://www.delftstack.com/it/tutorial/python-3-basic-tutorial/python-class-inheritance/
#https://www.w3schools.com/python/python_inheritance.asp



#Examples
class Person:
    
  def __init__(self,fname,lname ):
  
    self.firstname = fname
    self.lastname = lname


x = Person("Dario","Cozzuto")
print(x.firstname)
print(x.lastname)



class quadrato:

  def __init__(self,latoa, latob):
    self.lato1=latoa
    self.lato2=latob
  
  def perimetro(self):
    return 2*(self.lato1+self.lato2)
    
  def area(self):
    return self.lato1*self.lato2

x = Quadrato(2,4)
print(x.perimetro())
print(x.area())



#Multiple inheritance
class A:
	def dispA(self):
		print('You are in class A')

		
class B:
	def dispB(self):
		print('You are in class B')

		
class C(A, B):
	def dispC(self):
		print('You are in class C')

Cobj = C()
Cobj.dispA()
You are in class A

Cobj.dispB()
You are in class B

Cobj.dispC()
You are in class C




#Overriding inheritance
class Auto:
	def __init__(self, e, n):
		self.engine = e
		self.name = n
	def display(self):
		print("Name of Auto: ", self.name)
		print("Engine of auto: ", self.engine)

		
class Car(Auto):
	def __init__(self):
		self.x= input("Enter name of car: ")
		self.y= input("Enter engine of car: ")
		Auto.__init__(self,self.y,self.x)
    def display(self):
		print("You are in child class")

		
c = Car()
Enter name of car: Prius
Enter engine of car: 1.51
c.display()
You are in child class






#Add with super - examples1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)



#Add with super - examples2
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)



#Add with super - examples3
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
