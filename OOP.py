# class BankAccount:
#     def __init__(self, accountType,amount, withdraw, deposit):
#         self.accountType=accountType
#         self.__amount=float(amount)
#         self.withdraw=float(withdraw)
#         self.deposit=float(deposit)
            
#     def description(self):
#         print("This is a "+ self.accountType)
    
#     def getBalance(self):
#         return self.__amount

#     def setBalance(self, amount):
#         self.__amount=amount

#     def withdrawMoney(self):
#         if self.__amount>self.withdraw:
#             self.__amount=self.__amount-self.withdraw
#             print(f"After withdraw total amount is { self.__amount} ")
#         else:
#             print("Insufficient balance.")
    
#     def depositMoney(self):
#         self.__amount=self.__amount+self.deposit
#         print(f"After deposit total amount is {self.__amount}")

# account1=BankAccount("savings", 100,10,20)
# print(f"Initial balance: {account1.getBalance()}")
# account1.withdrawMoney()
# account1.depositMoney()


# Encapsulation
# name - public
# _name - protected
# __name - private


# Polymorphism
# having many forms.

# class Animal:
#     def make_sound(self):
#         return "Some generic animal sound"

# class Dog(Animal):
#     def make_sound(self):
#         return "Bark"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow"

# animals = [Dog(), Cat(), Animal()]

# for animal in animals:
#     print(animal.make_sound())

# class Plane:
#     def __init__(self,name):
#         self.name=name
    
#     def move(self):
#         print("Fly " + self.name)

# class Boat:
#     def __init__(self,name):
#         self.name=name

#     def move(self):
#         print("Sail " + self.name)

# plane=Plane("Boeing")
# plane.move()

# boat=Boat("Cruise")
# boat.move()



# Inheritance
class Person: #Parent class
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname

    def printName(self):
        print(self.fname+ " " + self.lname)

class Student(Person): #Child class
    pass

student1=Student("John", "Doe")
student1.printName()

# Data Abstraction
