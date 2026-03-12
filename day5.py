#____________________________________if else
#  check odd or even
'''a= int(input("enter a"))
b= 2

if(a%b==0):
    print("a is even")
else:
    print("a is odd")

#--------------------------------------------
#check a number divided by 5 and 3
a= int(input("enter a"))


if( a%5==0 and a%3==0):
    print("yeeyy ! it divide by both 3 and 5")
else:
    print("ohno ! it  does'nt divide by both 3 and 5")
#------------------------------------------------------
#            user name login
a= input(" enter the password")

if(a=="hari"):
    print("you are allowed to enter")
else:
   print("you are not allowed to enter")

#------------------------------------------------------------------------
     #       traffic sign speed
a=int(input("enter the speed"))
if(a>=90):
    print("you are going on high speed !!!!")
else:
    print("your speed is fine")
#________________________________________________________________________
  # check password lengths
a=input("enter the password")
if(len(a)>=8):
    print("your password is strong ")
else:
    print("your password is weak")
#____________________________________________________________________
#  e-commerce discount
a=int(input("enter the price"))
if(a>=6000):
    print("you are allowed to get discount for 10%")
else:
    print("sorry! you cant get discount ")

#---------------------------------------------------------------------
#--------------

#_______________________________

#---------------- 1)calculator:
a = int(input("enter the value for a ="))
b = int(input("enter the value for b ="))
c = input("enter the operator or operation to calculate =")

if(c=="+" or c=="add"):
    print(a+b)
elif(c=="-" or c=="sub"):
    print(a-b)
elif(c=="*" or c=="multiply"):
    print(a*b)
elif(c=="/" or c=="divide"):
    print(a/b)
elif(c=="%" or c=="mod"):
    print(a%b)
else:
    print(a**b)
#----------------------------------2)traffic signal system
a=input("enter the color")
if(a=="red"):
    print("you are allowed to enter")
elif(a=="yellow"):
    print(" ohh no ! walk fasttt!!!!")
else:
    print("you are not allowed to enter")
#______________________________________3)season find

a=input("enter the details to know abt the season : ")
if(a=="Rain"):
    print("It is rainy season")
elif(a=="hot"):
    print("It is summer season")
elif(a=="snow"):
    print("It is winter season")
else:
    print("it is spring season")'''
#_________________________________________________
#Nested if.......................
'''a=int(input("Enter the value a"))
b=int(input("Enter the value b"))
c=int(input("Enter the value c"))
if(a>b):
    if(a>c):
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")'''
#..................User name
'''a=input("Enter the Username")
b=input("Enter the password")
if(a=="harithakrishnan"):
    if(b=="hari11"):
        print("You are successfully LOGIN")
    else:
        print("Your Password is incorrect give correctly")
else:
    print("You are not allowed to Login")'''
#ATM PIN.........
'''a=int(input("Enter the PIN Number"))
b=int(input("Enter the amount"))
if(a==1121):
    if(b>=1000):
        print("Your amount collected")
    else:
        print("Your Balance is insufficient")
else:
    print("Your pin is incorrect")'''
#JOB ELIGIBILITY...........
'''age=int(input("Enter the age"))
degree=input("Enter the degree")
if(age==21):
    if(degree=="BE"):
        print("You are eligible to JOB")
    else:
        print("You are not finish the degree")
else:
        print("You are not eligible to JOB")'''
#NUMBERS............
a=int(input("Enter the number"))
if(a%3==0):
    print("a is divisible by 3")
    if(a%2==0):
        print("a is even number")
    else:
        print("a is odd number")
    if(a>0):
        print("a is positive value")
    else:
        print("a is not positive value")
else:
    print("a is not divisible by 3")
    if(a%2==0):
        print("a is even number")
    else:
        print("a is odd number")
    if(a>0):
        print("a is positive value")
    else:
        print("a is not positive value")


