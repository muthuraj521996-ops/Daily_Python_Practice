#Create Dictionary with Student Details
student = {"name": "Siva", "age": 24}
print(student)
#Access Dictionary Values Using Keys
student = {"name": "Haritha", "age": 21}
print(student["name"])
print(student["age"])
#Add New Key-Value Pair
student = {"name": "Muthu", "age": 60}
student["city"] = "Chennai"
print(student)
#Update Value in Dictionary
student = {"name": "Raji", "age": 50}
student["age"] = 51
print(student)
#Delete Key from Dictionary
student = {"name": "Lingam", "age": 28}
del student["age"]
print(student)
#Print All Keys
student = {"name": "Sowndharya", "age": 27, "city": "Thanjavur"}
print(student.keys())
#Print All Values
student = {"name": "Maran", "age": 1, "city": "Tenkasi"}
print(student.values())
#Print Key-Value Pairs
student = {"name": "Bharathi", "age": 30}
for k, v in student.items():
    print(k, ":", v)
#Check Whether Key Exists
student = {"name": "Venkat", "age": 29}
if "name" in student:
    print("Key exists")
else:
    print("Key not found")
#Count Number of Items in Dictionary
student = {"name": "Mukundh", "age": 1, "city": "Tirunelveli"}
print(len(student))
#Merge Two Dictionaries
d1 = {"name": "Siva"}
d2 = {"age": 24}
d1.update(d2)
print(d1)
#Create Dictionary from Two Lists
names = ["Haritha", "Muthu", "Raji"]
ages = [21, 60, 51]
d = dict(zip(names, ages))
print(d)
#Sort Dictionary by Keys
d = {"Muthu": 60, "Siva": 24, "Raji": 51}
for key in sorted(d):
    print(key, d[key])
#Sort Dictionary by Values
d = {"Siva": 24, "Haritha": 21, "Maran": 1}
for key in sorted(d, key=d.get):
    print(key, d[key])
#Find Maximum Value
marks = {"Siva": 80, "Haritha": 90, "Muthu": 70}
print(max(marks.values()))
#Find Minimum Value
marks = {"Raji": 85, "Lingam": 60, "Venkat": 75}
print(min(marks.values()))
#Remove Duplicate Values
d = {"Siva": 80, "Haritha": 90, "Muthu": 80}
new = {}
for k, v in d.items():
    if v not in new.values():
        new[k] = v
print(new)
#Print Dictionary in Reverse Order
d = {"Siva": 21, "Haritha": 22, "Maran": 23}
for key in reversed(list(d.keys())):
    print(key, d[key])
#Create Dictionary Using Loop
d = {}
for i in range(1,6):
    d[i] = i*i
print(d)
#Count Frequency of Characters Using Dictionary
text = "bharathi"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch,0) + 1
print(freq)
#Convert Dictionary Keys into List
d = {"Siva": 21, "Haritha": 22, "Muthu": 23}
keys = list(d.keys())
print(keys)
#Convert Dictionary Values into List
d = {"Siva": 21, "Haritha": 22, "Muthu": 23}
values = list(d.values())
print(values)
#Check Whether Dictionary is Empty
d = {}
if not d:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")
#Copy Dictionary
d1 = {"Siva": 21, "Haritha": 22}
d2 = d1.copy()
print(d2)
#Clear Dictionary
d = {"Muthu": 21, "Raji": 22}
d.clear()
print(d)