#Function with return value
def calc_rectangle_per(length, width):
    perimeter = (length + width) * 2
    return perimeter
lenght = 5
width = 3
perimeter = calc_rectangle_per(lenght, width)
print(perimeter, '\n')
print(calc_rectangle_per(10, 5), '\n')\

def calc_rectangle_area_per(lenght, width):
    area = lenght * width
    perimeter = (lenght + width) * 2
    return area, perimeter
area, perimeter = calc_rectangle_area_per(10, 5)
print("Area:", area, "Perimeter:", perimeter, '\n')

#Yield function
# Yield la mot generator
def gen_numbers(n):
    for i in range(n):
        yield i * 2
gen = gen_numbers(5)
for number in gen:
    print(number, end=' ')

def gen():
    yield 1
    yield 2
    yield 3
for value in gen():
    print(value, end=' ')

def gen_numbers():
    while True:
        x = yield
        yield x ** 2
g = gen_numbers()
print(next(g))
print(g.send(5))
print(next(g)) 
print(g.send(10))

#Lambda function
calc = lambda x, y: x + y
print(calc(5, 3), '\n')

#Default argument
calc2 = lambda x, y=10: x * y
print(calc2(5), '\n')
print(calc2(5, 3), '\n')

def khoa():
    gen = lambda x: x + 'Dang Khoa'
    return gen
call = khoa()
print(call('Huynh '), '\n')
print(call, '\n')

list_lambda = [lambda x: x ** 2, lambda x: x + 10, lambda x: x * 3]
print(list_lambda[0](5), '\n')
print(list_lambda[1](5), '\n')
print(list_lambda[2](5), '\n')
#Lambda list
key = 'name'
dict = {   'name': lambda: 'Huynh Dang Khoa', 
          'age': lambda : 20, 
          'address': lambda : 'HCM'}
print(dict[key](),'\n')
print(dict['age'](), '\n')
#Condition in lambda
is_even = lambda x: x % 2 == 0
print(is_even(4), '\n')
print(is_even(5), '\n')

