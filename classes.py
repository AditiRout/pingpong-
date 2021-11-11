class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
p1.age = 40
print(p1.age)
del p1.age

del p1
class Student(Person):
  pass
#has prop.of parent class

#class Student(Person):
  #def __init__(self, fname, lname):
    #add properties etc...if this is used it longer has prop of parents class..in order retain we use syntax

class Student(Person):
  def __init__(self, fname, lname,year):
    Person.__init__(self, fname, lname)#can use  super().__init__(fname, lname) this as well
    self.graduationyear = year
    def myfunc(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)

g=Student("rahul","gong",1234)
g.myfunc()
