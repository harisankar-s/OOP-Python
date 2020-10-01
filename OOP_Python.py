# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:42:04 2020

@author: harisankar.sivankutty
"""

#Problem 1 : How to define a class

class MyFirstClass():
    #Class Attributes
    var = 10

firstObject = MyFirstClass()
print(firstObject)      #Printing object's memory hex
print(firstObject.var)  #Accessing Class Attributes

secondObject = MyFirstClass()
print(secondObject)
print(secondObject.var)


#Problem 2
#In this example we will be seeing how instance methods are used
#Instance methods are accessed by: instance.method()

class Vehicle():
    #Class Methods/ Attributes

    #Here self is passed as an argument because instance is passed as first argument
    def type(self):     #Without self it throws an error
        print(self)
        print('I have a type')

car = Vehicle()
print(car)
car.type()


#Problem3
#In this example we will be seeing how instance Attributes are used
#Instance attributes are accessed by: object.attribute
#Attributes are looked First in the instance and THEN in the class

import random
class Vehicle():
    #Class Methods/ Attributes
    def type(self):
        #NOTE: This is not a class attribute as the variable is binded to self. Hence it becomes
        #instance attribute
        self.randomValue = random.randint(1,10) #Setting the instance attribute

car = Vehicle()
car.type()              #Calling the class Method
print(car.randomValue)  #Calling the instance attribute



#Problem4
#This example shows the use of __init__ constructor

class Vehicle():
    #__init__ is used to set values as soon as new object are created
    #__init__ is a keyword hence it has to be named like it is
    def __init__(self):     #called automatically hence known as magic method
        print('Calling init')
        self.val = 0
        self.cost = 10000   #Setting the default value when the object is created

    def incrementVehicle(self):
        self.val += 1


car = Vehicle()     #__init__ is called
print('First obj value:',car.val)
car.incrementVehicle()
car.incrementVehicle()
print('First obj value after incrementing:',car.val)      #2

bike = Vehicle()       #__init__ is called makes val 0 for this ANOTHER instance
print('Second obj value:',bike.val)



#Problem4
#In this assignment we would see the use of OOP

class MaxSizeList(object):
    def __init__(self, value):
        self.myList = []
        self.value = value

    def push(self, String):
        try:
            String = str(String)
            self.myList.append(String)
        except ValueError:
            print('You can only push strings!')

    def getList(self):
        print(self.myList[self.value:])

if __name__ == '__main__':
    a = MaxSizeList(3)
    b = MaxSizeList(1)

    a.push('Hey')
    a.push('Hello')
    a.push('Hi')
    a.push('Let\'s')
    a.push('Go')

    b.push('Hey')
    b.push('Hello')
    b.push('Hi')
    b.push('Let\'s')
    b.push('Go')

    a.getList()
    b.getList()

# Problem 5---Inheritance
#This program illustrates the concept of inheritance
#Python looks up for method in following order: Instance attributes, class attributes and the
#from the base class

class Data(object):
    def getData(self):
        print('In data!')

class Time(Data):           #Inheriting from Data class
    def getTime(self):
        print('In Time!')

if __name__ == '__main__':
    data = Data()
    time = Time()

    data.getData()
    time.getTime()
    time.getData()          #Inherited Data method
    
    
#Problem 6 This program illustrates the advanced concepts of inheritance
#Python looks up for method in following order: Instance attributes, class attributes and
#from the base class
#mro: Method Resolution order

class Data(object):
    def __init__(self, data):
        self.data = data

    def getData(self):
        print('Data:',self.data)

class Time(Data):           #Inhertiting from Data class
    def getTime(self):
        print('Time:',self.data)

if __name__ == '__main__':
    data = Data(10)
    time = Time(20)     #inherited Class -> Value passed to __init__of Data (Base class)

    time.getTime()
    data.getData()
    time.getData()

    print(Time.mro())
    

#Problem7
#This program shows the order in which the classes are accessed in case of multiple inheritance
#Python uses DEPTH FIRST SEARCH algorithm for lookups

class A(object):
    def doThis(self):
        print('Doing this in A')

class B(A):
    pass

#If class C was also being derived from A then the lookup order would be D,B,C,A
class C(object):
    def doThis(self):
        print('Doing this in C')

class D(B, A):
    pass

if __name__ == '__main__':
    dObj = D()
    dObj.doThis() #A method gets called because order for lookup is D,B,A,C this is shown by function mro

    print(D.mro())
    

#========================Program 8=========================================================
# This program illustrates all the OOP concepts learned uptil now

class BankAccount(object):
    defaultAccNumber = 1        # Class Attribute

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.accountNumber = BankAccount.defaultAccNumber
        BankAccount.defaultAccNumber = BankAccount.defaultAccNumber + 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Not enough balance!')
        else:
            self.balance -= amount

    def getBalance(self):
        return self.balance

if __name__ == '__main__':
    myObj = BankAccount('Hari', 1000)
    myObj.deposit(1000)
    print(myObj.getBalance())
    myObj.withdraw(500)
    print(myObj.getBalance())    
    
#=========================Program 9 ===================
    
 In this example we will see how the private variables work in Python
class Person(object):
    def __init__(self, name):
        self.name = name
        self.__education = 'Engineering'         # Private Variable

    def displayInfo(self):
        name = self.name
        education = self.__education             # Can only be accessed within the class
        print('My name is', name, 'and I have completed my', education)

if __name__ == '__main__':
    myObj = Person('Hari')
    myObj.displayInfo()
    print(myObj.name)                           # Can be accessed as it is public variable
    # print(myObj.__education)                  # Throws an error
    print(myObj._Person__education)             # Private variable can be accessed like this but NEVER EVER
                                                # do this please!!!
                                                
     # Program 11 ====================================                                           
# In this example we will see what are Python Magic Methods (or Special Methods) and how to overload them
# Now why these methods are called Magic or Special methods anyway? The reason is that these
# methods are invoked directly after creation of a class instance. For example:
# __init__ is a Magic method. Also __str__, __repr__, __add__ are all magic methods.

class Employee(object):
    def __init__(self, firstname, lastname, salary = 0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def __str__(self):
        return 'Full Name: ' + self.firstname + ' ' + self.lastname

    # Implements behaviour for built in type comparison to int
    def __int__(self):
        return self.salary

    # For overloading the (==)
    def __eq__(self,other):
       return self.salary==other.salary   

    # For overloading the (+)
    def __add__(self, other):
        return self.salary + other.salary

    # For overloading the (*)
    def __mul__(self, other):
        return self.salary * other.salary

if __name__ == '__main__':
    Omkar = Employee('Omkar', 'Pathak', 1000)
    Jagdish = Employee('Jagdish','Pathak', 2000)
    print(Omkar)                # Full Name: Omkar Pathak (This output because of __str__ method overloading)
    print(Jagdish)              # Full Name: Jagdish Pathak
    print(Omkar + Jagdish)      # 3000 (This output because of __add__ method overloading)
    print(Omkar * Jagdish)      # 2000000 (__mul__)
    print(int(Omkar))           # 1000 (__int__)
    print(int(Jagdish))         # 2000 (__int__)
    print(Omkar==Jagdish)
                                                
    
#This shows the usage of property decorators

#Python @property is one of the built-in decorators. The main purpose of any decorator is to change your class methods or attributes in such a way so that the users neeed not make any additional changes in their code.

#Without property decorators

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.total= self.name+ " has "+self.balance+ " dollars in the account"

user1=BankAccount("Elon Musk","10000")
user1.name="Tim cook"
print(user1.name)
print(user1.total)

# Output: Tim cook
#         Elon Musk has 10000 dollars in the account


#With property decorators

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    @property
    def total(self):
        return self.name+ " has "+self.balance+ " dollars in the account"

user1=BankAccount("Elon Musk","10000")
user1.name="Tim cook"
print(user1.name)
print(user1.total)

#Output: Tim cook
#        Tim cook has 10000 dollars in the account
