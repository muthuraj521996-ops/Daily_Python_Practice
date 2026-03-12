'''#Index Error
try:
    num=[10,20,30]
    print(num[5])
except Exception as e:
    print(e)
#Key Error
try:
    Student={name:"Haritha",age:21}
    print(student[marks])
except Exception as f:
    print(f)

#ELSE AND FINALLY
try:
    a=int(input("Enter no"))
    b=int(input("Enter no"))
    result=a/b
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("invalid input")
else:
    print(result)
finally:
    print("Completed")
#Normal program
num=-5
if num<0:
    raise Exception("Negative number not allowed")
print(num)
#Raise Program
try:
    num=int(input("Enter no"))
    if num<0:
        raise ValueError("Negative number not allowed")
    print(num)
except ValueError as e:
    print(e)
#task age
try:
    num=int(input("Enter no:"))
    if num<18:
        raise ValueError("Hello")
    print("Eligible for vote")
except ValueError as e:
    print(e)
#user defined
class AgeError(Exception):
    pass
try:
    age=int(input("enter your age:"))
    if age<18:
        raise AgeError("Not Eligible for vote")
    print("Eligible")
except AgeError as e:
    print(e)'''
#user defined ATM.........
class ATMError(Exception):
    pass
try:
    amount=int(input("Enter Amount:"))
    if amount<500:
        raise ATMError("You will collect amount only greater than 500")
    print("You will collect your amount")
except ATMError as e:
    print(e)
