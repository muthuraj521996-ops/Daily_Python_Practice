#1st Method..........
var1="Dhoni"
print(var1,"is my captain")
#....................
var1="Dhoni"
var2=150
print(var1,"scored",var2,"runs")
#....................
var1="Ramesh"
var2="Suresh"
print(var1,"and",var2,"are bestfriends")
#2nd Method..........
var1="Dhoni"
print("%s is my captain"%(var1))
#....................
var1="Dhoni"
var2=150
print("%s scored %d runs"%(var1,var2))
#....................
var1="Ramesh"
var2="Suresh"
print("%s and %s are bestfriends"%(var1,var2))
#3rd Method..........
var1="Dhoni"
print("{} is my captain".format(var1))
#....................
var1="Dhoni"
var2=150
print("{} scored {} runs".format(var1,var2))
#....................
var1="suresh"
var2="ramesh"
print("{} and {} are bestfriends".format(var1,var2))
#....................
#India Scored 350 runs in 50 overs against pakistan in 1996
var1="India"
var2=350
var3=50
var4="Pakistan"
var5=1996
print(var1,"Scored",var2,"runs in",var3,"overs against",var4,"in",var5)
#....................
var1="Besant Tech"
print(var1[3:9])
print(var1[-8:-2])
print(var1[3:-2])
print(var1[-8:9])
#....................
a=123
print(type(a))
#....................
a=("Besant")
print(type(a))
print(len(a))
#....................
num1=1234
print(type(num1))
num2=str(num1)
print(type(num2))
print(len(num2))
#....................
a="1234"
print(type(a))
b=int(a)
print(type(b))
#.....................
name1="BESANT TECH"
name2="BeSant Tech"
print(name1.lower())
print(name2.lower())
print(name1.title())
print(name2.title())
print(name1.upper())
print(name2.upper())
print(name1.capitalize())
print(name2.capitalize())
print(name1.swapcase())
print(name2.swapcase())