print("Hi!!")

#pip-> pip installs packages in python. It's also a package manager in python
#saves the file get-pip.py in your folder 
#open cmd from and runs the command -> python get-pip.py

#pip3 --version
#to check the version

#install package howdoi using pip 
#pip3 install howdoi

#howdoi is like google to python developers to ask python related queries

#howdoi write functions in python
import math
def make_cylinder_volume_func(r):
    def volume(h):
        return math.pi * r * r * h
    return volume

#howdoi declare variables in python

foo = 'bar' # the name 'foo' is now a name for the string 'bar'
foo = 2 * 3 # the name 'foo' stops being a name for the string 'bar',
# and starts being a name for the integer 6, resulting from the multiplication

#howdoi write class in python 
class Student(object):
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setGrade(self, course, grade):
        self.grades[course] = grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)

# Define some students
john = Student("John", 12, "male", 6, {"math":3.3})
jane = Student("Jane", 12, "female", 6, {"math":3.5})

# Now we can get to the grades easily
print(john.getGPA())
print(jane.getGPA())

#write your own class 
class Car(object):
    def __init__(self,model,colour,company,speed_limit):
        self.colour = colour
        self.company =company
        self.speed_limit = speed_limit
        self.model = model

    def start (self):
        print("started")

    def stop (self):
        print("stopped")

    def accelerate(self):
        print("acclerating")

    def change_gear(self,gear_type):
        print("gear changed")

audi = Car("A6","red","audi",80)
print(audi.colour)
print(audi.stop())
