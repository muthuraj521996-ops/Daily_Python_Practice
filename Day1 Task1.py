#Program to Check if a Number is Positive or Negative.....
num = float(input("Enter a number: "))
if num > 0:
    print("The number is Positive")
else:
    print("The number is Negative")
#Program to Check Whether a Number is Even or Odd.....
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
#Program to Find the Largest of Two Numbers.....
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print("Largest number is:", num1)
else:
    print("Largest number is:", num2)
#Program to Find the Largest of Three Numbers.....
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)
#Program to Check Whether a Number is Divisible by 5 and 11.....
num = int(input("Enter a number: "))
if num % 5 == 0 and num % 11 == 0:
    print("Divisible by both 5 and 11")
elif num % 5 == 0:
    print("Divisible by 5 only")
elif num % 11 == 0:
    print("Divisible by 11 only")
else:
    print("Not divisible by 5 and 11")
#Program to Check Whether a Year is a Leap Year.....
year = int(input("Enter year: "))
if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
#Program to Check Whether a Character is Vowel or Consonant.....
ch = input("Enter a letter: ")
if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")
#Program to Check Whether a Number is Multiple of 3 and 7.....
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("The number is a multiple of both 3 and 7")
elif num % 3 == 0:
    print("The number is a multiple of 3 only")
elif num % 7 == 0:
    print("The number is a multiple of 7 only")
else:
    print("The number is not a multiple of 3 or 7")
#Program to Check Whether a Number is a Three-Digit Number.....
num = int(input("Enter number: "))
if 100 <= num <= 999:
    print("Three digit number")
else:
    print("Not a three digit number")
#Program to Check Whether a Number is Greater Than 100.....
num = int(input("Enter number: "))
if num > 100:
    print("Greater than 100")
else:
    print("Not greater than 100")