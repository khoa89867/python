

#String methods
strA = "Huynh Dang khoa"
strB = strA.capitalize()
strC = strA.upper()
strD = strA.lower()
strE = strA.swapcase()
strF = strA.title()
strG = strA.center(30, '*')
strH = strA.ljust(30, '*')
strI = strA.rjust(30, '*')
strJ = "Mã hoá ký tự"
strK = strJ.encode('utf-8')
strL = strA.join(['1', '2', '3'])
strM = strA.replace('o', '0')
strN = strA.strip('Huya')
strO = strA.split(' ', 2)
strP = strA.rsplit(' ', 1)
strQ = strA.partition('a')
strR = strA.count('k', 0, 15)
strS = strA.startswith('D', 6, 15)
strT = strA.endswith('a', -10, None)
strU = strA.find('k', 0, 15)
strV = strA.index('h', 0, 15)
strW = strA.islower()
strX = strA.isupper()
strY = strA.isalpha()
strZ = strA.isdigit()
a = " "
b = a.isspace()
c = '5'
d = c.isdigit()
print(strB, '\n', 
    strC, '\n', 
    strD, '\n', 
    strE, '\n', 
    strF, '\n', 
    strG, '\n', 
    strH, '\n', 
    strI, '\n', 
    strK, '\n', 
    strL, '\n', 
    strM, '\n', 
    strN, '\n', 
    strO, '\n', 
    strP, '\n',
    strQ, '\n',
    strR, '\n',
    strS, '\n',
    strT, '\n',
    strU, '\n',
    strV, '\n',
    strW, '\n',
    strX, '\n',
    strY, '\n',
    strZ, '\n',
    b, '\n',
    d, '\n')


##########################################LIST##########################################
listA = [1, 2, 3, "Khoa", 3.14, True]
print(listA, '\n', type(listA), '\n')
#List comprehension
listB = [x for x in range(10) if x % 2 == 0]
print(listB, '\n')
listC = [[x, y] for x in range(3) for y in range(3)]
print(listC, '\n')
listD = [[n, n*2, n*3] for n in range(1,6)]
print(listD, '\n')
#Constructing list
listE = list('Huynh Dang Khoa')
print(listE, '\n')
listF = [1, "Khoa", 3.14, True, [1, 2, 3]]
g = "Khoa" in listF
h = "Duy" in listF
i = listF[4][1]
print(g, '\n', h, '\n', i, '\n')
#Matrix or Two-dimensional list
listG = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listG[0], '\n')
print(listG[1], '\n')
print(listG[2], '\n')
print(listG, '\n')
listG[0][-1] = 10
listG[1][2] = 20
listG[2][0] = 30
print(listG, '\n')
#List methods
listH = [1, 2, 3, 4, 5, 1, 3, 2, 3]
count = listH.count(3)
index = listH.index(3, 3, 7)  
copy = listH.copy()
copy[0] = "Khoa"
listI = [1, 2, 3]
listI.append(4)
listJ = [5, 6, 7]
listJ.extend([8, 9, [10, 11]])
listK = [1, 2, 3, 4, 5]
listK.insert(2, "Khoa")
clear_list = listH.clear()
listL = [1, 2, 3, 4, 5]
pop = listL.pop(2)
listM = [1, 2, 3, 4, 5]
listM.remove(3)
listN = [1, 2, 3, 4, 5, 9, 10, 30, 20, 15]
listN.reverse()
listN.sort(reverse=True)
print('listH =', listH, '\n')
print('count =', count)
print('index =', index)
print('copy =', copy)
print('append_list =', listI)
print('extend_list =', listJ)
print('insert_list =', listK)
print('clear_list =', clear_list)
print('pop_list =', listL, '\n', 'pop =', pop, '\n')
print('remove_list =', listM, '\n')
print('reverse_list =', listN, '\n')
print('sort_list =', listN, '\n')




#Hashable types

