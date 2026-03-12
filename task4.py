#print odd number
for i in range(1, 51):
    if i % 2 == 0:
        continue
    print(i)
#------------------------------------------------------
#skip vowels in string
a = "python programming"
for ch in a:
    if ch in "aeiou":
        continue
    print(ch, end="")
#-----------------------------------------------
#skip negative numbers
a = [10, -5, 20, -3, 30, -90]
for num in a:
    if num < 0:
        continue
    print(num)
#-----------------------------------------------
#divisible by 5 from 1 to 50
for i in range(1, 51):
    if i % 5 != 0:
        continue
    print(i)
#--------------------------------------------------
#prime or not using break
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
#-----------------------------------------------------
#stop when user enter 0 using while
while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    print("You entered:", num)
#---------------------------------------------------------
#stop when number is found
a = [10, 20, 30, 40, 90, 80, 70]
search = 90
for num in a:
    if num == search:
        print("Number found:", num)
        break







