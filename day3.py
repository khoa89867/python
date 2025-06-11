#Tuple
tuple1 = (1, 2, 3, 4, 5)
print(tuple1, '\n', type(tuple1), '\n')
tuple2 = (1, 2, 3, "Khoa", 3.14, True)
print(tuple2, '\n')
#Tuple constructor
tuple3 = tuple(['Huynh Dang Khoa', 22, 'HCM'])
print(tuple3, '\n')
#Tuple comprehension
tuple4 = (x for x in range(10) if x % 2 == 0)
tuple5 = tuple(tuple4)
print(tuple5, '\n')
#Tuple mathematical operations
tuple6 = (1, 10, 3)
tuple7 = (4, 8, 9)
tuple8 = tuple6 + tuple7
print(tuple8, '\n')
tuple9 = tuple6 * 2
print(tuple9, '\n')
a = 1 in tuple6
b = 10 not in tuple6
print(a, b, '\n')

#Tuple matrix or two-dimensional tuple
tuple11 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tuple11[0], '\n')
print(tuple11[1], '\n')
print(tuple11[2], '\n')
print(tuple11, '\n')
tuple12 = tuple11[0]
tuple12 = tuple12[:2] + (10,) + tuple12[3:]
tuple11 = (tuple12, tuple11[1], tuple11[2])
print(tuple11, '\n')

#Tuple methods
tuple12 = (1, 2, 3, 4, 5, 1, 3, 2, 3)
count = tuple12.count(3)
index = tuple12.index(3, 3, 7)
print('count =', count)
print('index =', index, '\n')

################################HASHABLE AND UNHASHABLE################################

#Hashable
hashable_int = 42
hashable_str = "Hello"
hashable_tuple = (1, 2, 3)
#Unhashable
unhashable_list = [1, 2, 3]
unhashable_dict = {"key": "value"}
unhashable_set = {1, 2, 3}






