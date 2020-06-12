                                                        #class and object in python#
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x) 

The __init__() Function
All classes have a function called __init__(), which is always executed when the class is being initiated.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 
Note: The __init__() function is called automatically every time the class is being used to create a new object.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 

Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc() 

Delete the p1 object:
del p1 

class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
Example
class Person:
  pass 

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() 

Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass 

Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname() 



Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
Example
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) 

By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019) 


Python RegEx
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

RegEx can be used to check if a string contains the specified search pattern.

Search the string to see if it starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 

Function 	Description
findall 	Returns a list containing all matches
search 	Returns a Match object if there is a match anywhere in the string
split 	Returns a list where the string has been split at each match
sub 	Replaces one or many matches with a string



#!/bin/python

import math
import os
import random
import re
import sys


class Rectangle:
    def __init__(self, w, h):
      self.w = w
      self.h = h
    def area(self):
        return (self.w*self.h)
class Circle:
    def __init__(self, r):
      self.r = r
    def area(self):
      a = float(self.r**2 * math.pi)
      return a
if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(raw_input())
    queries = []
    for _ in xrange(q):
        args = raw_input().split()
        shape_name, params = args[0], map(int, args[1:])
        if shape_name == "rectangle":
            a, b = params[0], params[1]
            shape = Rectangle(a, b)
        elif shape_name == "circle":
            r = params[0]
            shape = Circle(r)
        else:
            raise ValueError("invalid shape type")
        fptr.write("%.2f\n" % shape.area())
    fptr.close()































