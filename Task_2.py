'''a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in a:
    if(i%2!=0):
        print(i,"is odd")
    else:
        if(i%2==0):
            print(i,"is even")
#Factorial of 5.............
for i in range(1,6):
    a=5*1
    b=a*4
    c=b*3
    d=c*2
    e=d*1
print(e)'''
#....................
'''fact=1
for i in range(1,6):
    fact=fact*i
print(fact)
#Multiplication table 2............
for i in range(1,11,1):
    a=2
    print(i,"*",a,"=",i*2)'''
#Primenumbers............
'''for i in range(1,21):
    if i>1:
        for i in range(2,i):
            if(i%2!=0):
        print(i)
#Print numbers from 00 to 99 using a for loop
for i in range(100):
    print(str(i).zfill(2))
#Sum of Natural Numbers
sum = 0
for i in range(1,8):
    sum += i
print("Sum =", sum)
#Count Vowels in Name
name = "Haritha"
count = 0
for ch in name.lower():
    if ch in "aeiou":
        count += 1
print(count)
#Print the pattern
n = 5
s = ""
for i in range(1, n + 1):
    s += str(i) + " "
    print(s)'''
#...........
for i in range(10):
    for j in range(10):
        print(i,j)
