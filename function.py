#Positional args.............
def student(name,age):
    print(name,age)
student("Hari",21)
#Keyword args................
def student(name,age):
    print(name,age)
student(age=21,name="Hari")
#Default args................
def greet(name="student"):
    print("hello",name)
greet()
#Variable length args.........
# *args..............
def demo(*degree):
    print(degree)
demo("BCA","BE","BSC","BBA")
# **KWargs
def student(**simple):
    print(simple)
student(Name="Hari",age=21,Course="Python")
#examples.............
def example(name,age,*marks,**extrainformation):
    print(name,age,marks,extrainformation)
example("hari",21,98,99,82,81,Degree="BE",Dept="CSE",Passedout=2026)
