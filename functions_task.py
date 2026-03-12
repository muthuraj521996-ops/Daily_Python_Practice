#Function to add two numbers
'''def add(a, b):
    return a + b
print(add(10, 5))
#Function to subtract two numbers
def subtract(a, b):
    return a - b
print(subtract(15, 5))
#Function to multiply two numbers
def multiply(a, b):
    return a * b
print(multiply(4, 5))
#Function to divide two numbers
def divide(a, b):
    return a / b
print(divide(10, 2))
#Function to find square of a number
def square(n):
    return n * n
print(square(5))
#Function to check even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(7))
#Function to find largest of two numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b
print(largest(8, 5))
#Function to count vowels in a string
def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count += 1
    return count
print(count_vowels("Hello"))
#Function to reverse a string
def reverse_string(text):
    return text[::-1]
print(reverse_string("Python"))
#Function to find factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))
#Function to find sum of list elements
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum_list([1, 2, 3, 4]))
#Function to find maximum number in a list
def max_number(numbers):
    return max(numbers)
print(max_number([10, 25, 7, 40]))
#Function to check whether a number is prime
def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return "Prime"
    else:
        return "Not Prime"
print(is_prime(7))
#Function to count characters in a string
def count_characters(text):
    return len(text)
print(count_characters("Python"))
#Function to return multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
multiplication_table(5)'''
#.......................
#FUNCTIONS PART2
#Function to Return Fibonacci Series
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()
fibonacci(6)
#Function to Find Second Largest Number in List
def second_largest(lst):
    lst.sort()
    return lst[-2]
numbers = [10, 5, 8, 20, 15]
print(second_largest(numbers))
#Function to Find Average of Numbers in List
def average(lst):
    total = sum(lst)
    avg = total / len(lst)
    return avg
numbers = [10, 20, 30, 40]
print(average(numbers))
#Function to Return Even Numbers from List
def even_numbers(lst):
    for num in lst:
        if num % 2 == 0:
            print(num)
numbers = [1,2,3,4,5,6]
even_numbers(numbers)
#Function to Calculate Sum of Digits
def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total
print(sum_digits(1234))
#Function to Remove Duplicates from List
def remove_duplicates(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list
numbers = [1,2,2,3,4,4,5]
print(remove_duplicates(numbers))
#Function to Count Character Frequency in String
def char_frequency(text):
    for ch in text:
        print(ch, ":", text.count(ch))
char_frequency("hello")
#Function to Return Maximum and Minimum
def max_min(lst):
    return max(lst), min(lst)
numbers = [10, 20, 5, 40]
print(max_min(numbers))
#Function to Check Palindrome String
def palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
print(palindrome("haritha"))
print(palindrome("level"))
#Function to Sort List Without Using sort()
def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n):
            if lst[i] < lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst
numbers = [5, 2, 8, 1, 3]
print(sort_list(numbers))