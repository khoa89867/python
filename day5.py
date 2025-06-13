###################################ITERATION###################################
iter = (x for x in range(4))
print(iter, '\n')
print(next(iter), '\n')
print(next(iter), '\n')

iter2 = (x for x in range(10) if x % 2 == 0)
print(sum(iter2, start=-10), '\n')
iter3 = (x for x in range(10) if x % 2 == 0)
print(max(iter3, default=20), '\n')

iter4 = (1, 6, 9, 2, 7, 5)
print(iter4, type(iter4), '\n')
print(sorted(iter4, reverse=True), type(sorted(iter4)), '\n')

# ###############################HAM XUAT##################################
print("Huynh Dang Khoa")
print(2003)
print("HCM")
print("Huynh Dang Khoa", 2003, "HCM", sep=' | ',)
print("Huynh Dang Khoa", 2003, "HCM", end='Huhu.\n')
from time import sleep
print("start")
# sleep(2)
print("end")

print("line1\nline2\nline3")
print("line4", end=' ')
# sleep(3)
print("line5")

with open("file/test.txt", "w") as file:
    print("Hello, World!", file=file)

print("start", end=' ', flush=True)
sleep(2)
print("end")

####################################HAM NHAP##################################

name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")
print(f"Name: {name}, Age: {age}, Address: {address}")

#####################################BOOLEAN######################################

print(True, False, type(True), type(False), sep='\n')
print(1 > 3, '\n')
print(1 < 3, '\n')
print(1 < 3 | 1 > 0, '\n')
print(1 < 3 and 1 > 0, '\n')
print(100 == 49 + 51, '\n')

o1 = ord('A')
o2 = ord('a')
print(o1 > o2, '\n')
print(o1 < o2, '\n')
print('a' > 'ABC'   , '\n')

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(list1 == list2, '\n')
print(list1 is list2, '\n')
print(list1 is not list2, '\n')
print(list1 is list3, '\n')
