###################################FUCTIONS###################################
def khoa():
    print("Hello, I am Khoa")
khoa()

def khoa2(name, age, address = "HCM"):
    print(f"Name: {name}, Age: {age}, Address: {address}")
khoa2("Khoa", 22)
khoa2("Khoa", 22, "Hanoi")

def khoa3(list=[]):
    list.append("Khoa")
    print(list)
khoa3()
khoa3(["Duy", "Huy"])

# positional arguments
def add(a, b):
    return a + b
print(add(5, 10)) 
# keyword arguments
def add2(a, b):
    return a + b
print(add2(b=10, a=5)) 

#Unpacking arguments

def add3(*args):
    return sum(args)
print(add3(1, 2, 3, 4, 5))
def add4(*args):
    return sum(args)
print(add4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
def add5(*args):
    return sum(args)
print(add5(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))

# Unpacking keyword arguments
def add6(**kwargs):
    return sum(kwargs.values())
print(add6(a=1, b=2, c=3))
def add7(**kwargs):
    return sum(kwargs.values())
print(add7(a=1, b=2, c=3, d=4, e=5))

