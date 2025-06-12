#####################################SET######################################
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, "Khoa", 3.14, True}
set3 = {('Huynh Dang Khoa', 22, 'HCM'), (1, 2, 3), (4, 5, 6)}
print(set1, '\n', type(set1), '\n')
print(set2, '\n')
print(set3, '\n')
#Set comprehension
set4 = {x for x in range(10) if x % 2 == 0}
set5 = {x for x in range(10) if x % 2 != 0 if x % 3 == 0 if x > 5}
print(set4, '\n')
print(set5, '\n')
#Set constructor
set6 = set('Huynh Dang Khoa')
set7 = set({(1, 2, 3, 4, 5), 1, 2, 3, "Khoa", 3.14, True})
set8 = set()
print(set6, '\n')
print(set7, '\n')
print(set8, type(set8), '\n')
#Set mathematical operations
set9 = {1, 2, 3}
set10 = {4, 5, 6, 1, 2}
print(4 in set9, 5 not in set9, '\n')
print(set9 - set10, '\n') 
print(set9 & set10, '\n') 
print(set9 | set10, '\n')
print(set9 ^ set10, '\n')
#Set methods
set11 = {1, 2, 3, 4, 5}
print("pop = ", set11.pop(), set11, '\n')
print("remove = ", set11.remove(2), set11, '\n')
print("discard = ", set11.discard(3), set11, '\n')
set12 = {1, 2, 3, 4, 5}
set13 = set12.copy()
print("copy = ", set13, '\n')
set12.add(6)
print("add = ", set12, '\n')
print("update = ", set12.update([7, 8]), set12, '\n')
print("clear = ", set12.clear(), set12, '\n')

#####################################DICTIONARY######################################
dict1 = {"name": "Khoa", "age": 23}
dict2 = {"name": "Duy", "age": 28, "address": "HCM"}
print(dict1, '\n', type(dict1), '\n')
print(dict2, '\n')
#Dictionary comprehension
dict3 = {x: x**2 for x in range(5)}
print(dict3, '\n')
#Dictionary constructor
dict4 = dict(name="Khoa", age=23, address="HCM")
dict5 = dict([("name", "Duy"), ("age", 28), ("address", "HCM")])
print(dict4, '\n')
print(dict5, '\n')
iterable = ("name", "address", "age")
dict6 = dict.fromkeys(iterable)
print(dict6, '\n')
dict7 = dict.fromkeys(iterable, "Unknown")
print(dict7, '\n')

#Take value from dictionary
name = dict1["name"]
age = dict1.get("age")
address = dict1.get("address", "No address")
print(name, age, address, '\n')

#Add and update value
print("Before update:", dict1, '\n')
dict1["address"] = "HCM"
dict1["phone"] = "0123456789"
dict1["age"] = dict1["age"] + 2
print("After update:", dict1, '\n')

#Delete value
del dict1["phone"]
print("After delete phone:", dict1, '\n')

#Dictionary methods

dict8 = {"name": "Khoa", "age": 23, "address": "HCM"}
dict9 = dict8.copy()
print("copy = ", dict9, '\n')
value = dict8.get("name")
print("get-value = ", value, '\n')
value2 = dict8.get("phone", "No phone")
print("get-value = ", value2, '\n')
items = dict8.items()
print("items = ", items, '\n')
keys = dict8.keys()
print("keys = ", keys, '\n')
values = dict8.values()
print("values = ", values, '\n')

dict10 = dict8.pop("age")
print("pop = ", dict10, dict8, '\n')
dict11 = dict8.pop("home", "No home")
print("pop = ", dict11, dict8, '\n')

dict12 = {"name": "Khoa", "age": 23, "address": "HCM"}
dict12.popitem()
print("popitem = ", dict12, '\n')

dict12.setdefault("phone", "0123456789")
print("setdefault = ", dict12, '\n')

dict12.update({"email": "google@gmail.com"})
print("update1 = ", dict12, '\n')
dict12.update([("name", "Duy"), ("age", 28)])
print("update2 = ", dict12, '\n')


#############################################FILE###########################################

#Read file
file = open('file/text.txt')
data = file.read()
file.close()
file = open('file/text.txt')
data2 = file.read()
file.close()
file = open('file/text.txt')
data3 = file.readline()
file.close()
file = open('file/text.txt')
data4 = file.readlines()
file.close()
print(data, '\n')
print(data2, '\n')
print(data3, '\n')
print(data4, '\n')

file = open('file/text.txt', 'r')
data5 = file.read()
print(data5, '\n')
file.seek(0)
data6 = file.read()
print(data6, '\n')
file.close()

#Write file
file = open('file/text.txt', 'a')
data7 = file.write("Hello, World!\n")
file.close()
print(data7, '\n')

with open('file/text.txt', 'a') as file:
    data8 = file.write("Number phone: 0358004048\n")
    print(data8, '\n')
