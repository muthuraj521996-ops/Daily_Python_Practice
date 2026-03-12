#If Loop Program
#Prime Number
num = int(input("Enter number: "))
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")
#Palindrome Number
num = int(input("Enter number: "))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
#Armstrong Number
num = int(input("Enter number: "))
temp = num
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit**3
    num = num // 10
if temp == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong")
#Second Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a > b and a < c) or (a > c and a < b):
    print("Second Largest:", a)
elif (b > a and b < c) or (b > c and b < a):
    print("Second Largest:", b)
else:
    print("Second Largest:", c)
#Perfect Number
num = int(input("Enter number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")
#Alphabet, Digit or Special Character
ch = input("Enter character: ")
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special Character")
#Divisible by 3 and 5
num = int(input("Enter number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not Divisible")
#String Starts with Vowel
text = input("Enter string: ")
if text[0].lower() in "aeiou":
    print("Starts with Vowel")
else:
    print("Does not start with Vowel")
#Grade using if-elif
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
#Number between 50 and 100
num = int(input("Enter number: "))
if num > 50 and num < 100:
    print("Number lies between 50 and 100")
else:
    print("Not in range")

#For Loop Program
#Fibonacci Series
n = int(input("Enter terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
#Sum of Digits
num = int(input("Enter number: "))
sum = 0
for digit in str(num):
    sum += int(digit)
print("Sum of digits:", sum)
#Reverse Number
num = int(input("Enter number: "))
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
print("Reversed number:", rev)
#Count Vowels
text = input("Enter string: ")
count = 0
for ch in text:
    if ch.lower() in "aeiou":
        count += 1
print("Vowel count:", count)
#Largest Element in List
numbers = [10, 20, 45, 30]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest:", largest)
#Second Largest in List
numbers = [10, 20, 45, 30]
numbers.sort()
print("Second Largest:", numbers[-2])
#Remove Duplicates
numbers = [1, 2, 2, 3, 4, 4]
new_list = []
for num in numbers:
    if num not in new_list:
        new_list.append(num)
print("Without duplicates:", new_list)
#Character Frequency
text = input("Enter string: ")
for ch in text:
    print(ch, ":", text.count(ch))
#Multiplication Table 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end=" ")
    print()
#Sum of Even Numbers in List
numbers = [1, 2, 3, 4, 5, 6]
sum = 0
for num in numbers:
    if num % 2 == 0:
        sum += num
print("Sum of even numbers:", sum)
#Square of Each Element
numbers = [1, 2, 3, 4]
for num in numbers:
    print(num**2)
#Common Elements in Two Lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
for num in list1:
    if num in list2:
        print("Common:", num)
#Maximum and Minimum
numbers = [10, 20, 5, 40]
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
#Star Pyramid Pattern
rows = 5
for i in range(1, rows+1):
    print("*" * i)
#Count Words in Sentence
sentence = input("Enter sentence: ")
words = sentence.split()
print("Word count:", len(words))