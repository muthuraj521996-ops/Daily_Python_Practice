#Program to calculate square root, power, factorial using math module
import math
num = int(input("Enter a number: "))
print("Square Root =", math.sqrt(num))
print("Power (num^2) =", math.pow(num, 2))
print("Factorial =", math.factorial(num))
#Program to display all functions in math module using dir()
import math
print("Functions in math module:")
print(dir(math))
#Program to generate random numbers using random module
import random
num = random.randint(1, 100)
print("Random Number =", num)
#Program to shuffle elements of a list
import random
list1 = [10, 20, 30, 40, 50]
random.shuffle(list1)
print("Shuffled List =", list1)
#Program to generate random password
import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
for i in range(8):
    password = password + random.choice(characters)
print("Random Password =", password)
#User-defined module for arithmetic operations
import arithmetic
a = 10
b = 5
print("Addition :", arithmetic.add(a, b))
print("Subtraction :", arithmetic.sub(a, b))
print("Multiplication :", arithmetic.mul(a, b))
print("Division :", arithmetic.div(a, b))
#Module to store student information
import student
student.display("Haritha", 101, "CSE")
student.display("Siva", 102, "ECE")
#Modules of area calculations
import area
print("Area of Circle =", area.circle(5))
print("Area of Square =", area.square(4))
print("Area of Rectangle =", area.rectangle(5,3))
#Program to import user-defined module and call functions
import arithmetic
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition =", arithmetic.add(a,b))
print("Subtraction =", arithmetic.sub(a,b))
#Program to display current date, time and year using datetime module
import datetime
now = datetime.datetime.now()
print("Current Date =", now.date())
print("Current Time =", now.time())
print("Current Year =", now.year)