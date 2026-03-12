#Print numbers from 1 to 10
for i in range(1, 11):
    print(i)
#Print even numbers from 1 to 50
for i in range(2, 51, 2):
    print(i)
#Print odd numbers from 1 to 50
for i in range(1, 51, 2):
    print(i)
#Find sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Sum =", total)
#Multiplication table of a number
num = int(input("Enter number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
#Count numbers in a list
numbers = [10, 20, 30, 40, 50]
count = 0
for i in numbers:
    count += 1
print("Count =", count)
#Print all elements in a list
numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i)
#Count vowels in a string
text = input("Enter name: ")
count = 0
for ch in text:
    if ch.lower() in "aeiou":
        count += 1
print("Vowel count =", count)
#Print numbers from 10 to 1 (reverse)
for i in range(10, 0, -1):
    print(i)
#Find factorial of a number
num = int(input("Enter number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial =", fact)
#Find largest number in a list
numbers = [10, 45, 23, 89, 12]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print("Largest =", largest)
#Count number of digits in a number
num = int(input("Enter number: "))
count = 0
for i in str(num):
    count += 1
print("Digit count =", count)
#Print square of numbers from 1 to 10
for i in range(1, 11):
    print(i, "Square =", i * i)
#Print cube of numbers from 1 to 10
for i in range(1, 11):
    print(i, "Cube =", i * i * i)
#Find sum of elements in a list
numbers = [5, 10, 15, 20]
total = 0
for i in numbers:
    total += i
print("Sum =", total)