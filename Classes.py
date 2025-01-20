#Object-oriented programming in Python

#Python is a multi-paradigm programming language. It supports different programming approaches.
#One of the popular approaches to solve a programming problem is by creating objects. 
#This is known as Object-Oriented Programming (OOP).
#An object has two characteristics:
#attributes
#behavior
#Let's take an example:
#Parrot is an object,
#name, age, color are attributes
#singing, dancing are behavior
#The concept of OOP in Python focuses on creating reusable code. 
#This concept is also known as DRY (Don't Repeat Yourself).
#In Python, the class is defined by using the class keyword.
#A class is a blueprint for the object.
#We can think of class as an sketch of a parrot with labels. 
# It contains all the details about the name, colors, size etc. 
# Based on these descriptions, we can study about the parrot. Here, a parrot is an object.
#The example for class of parrot can be :
#class Parrot:
#    pass
#Here, we use the pass keyword, which is generally used as a placeholder. It is a null statement in Python.
#Classes in Python
#Classes provide a means of bundling data and functionality together. 
# Creating a new class creates a new type of object, allowing new instances of that type to be made. 
# Each class instance can have attributes attached to it for maintaining its state. 
# Class instances can also have methods (defined by its class) for modifying its state.
#To create a class, use the keyword class:
#Example
#Create a class named MyClass, with a property named x:
#class MyClass:
#  x = 5
#Create Object
#Now we can use the class named MyClass to create objects:
#Create an object named p1, and print the value of x:

#p1 = MyClass()
#print(p1.x)
#The __init__() Function
#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#To understand the meaning of classes we have to understand the built-in __init__() function.
#All classes have a function called __init__(), which is always executed when the class is being initiated.

# class MyClass:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def myfunc(self):
#     print("Hello my name is " + self.name)

# MyName = MyClass("John", 36) #This is the object of the class MyClass
# print(MyName.name)
# MyName.myfunc()



#Restaurant class
# class Restaurant:
#     def __init__ (self, name, cuisine):
#         self.name=name
#         self.cuisine=cuisine
   
#     def description (self):
#       print("The name of the restaurant is " + self.name + " and it serves " + self.cuisine + " cuisine.")
    
#     def open(self):
#       print("The restaurant is open.")

# restaurant1 = Restaurant("The Golden Dragon", "Chinese")
# restaurant1.description()
# restaurant1.open()




class Bank:
   def __init__(self, name, location):
      self.name=name
      self.location=location

   def description(self):
      print("The bank name is "+self.name + " and it is located at " + self.location)

bank1=Bank("Ceylon", "Colombo")
bank1.description()