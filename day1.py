#Variable
a = 18
b = "Khoa"
c = 3.14
#Type of variable
print(type(a), type(b), type(c))

#Decimal
from decimal import*
getcontext().prec = 30
print(Decimal(10)/Decimal(3))


#fraction
from fractions import*
frac1 = Fraction(10, 3)
frac2 = Fraction(1, 3)
frac3 = frac1 + frac2
print(frac1, frac2, frac3, type(frac1))

#Complex number
from cmath import*
c1 = complex(2, 3)
print(c1.real, c1.imag, c1.conjugate(), abs(c1))
c2 = complex(1, 4)
c3 = c1 + c2
print(c1, c2, c3, type(c1))

#String
name = "Khoa"
multiLine = """sdjkgdfiubkjdshukdshfjk\ndfskjghvdfujvhdvf\ndhjgsdjyhgsdbfd"""
print('\a')
print(name, multiLine)
#Muliply string
name2 = "Duy\n"
name3 = name2 * 10
print(name3)
#Check if string B is in string A
strA = "Khoa"
strB = "K"
print(strB in strA)
#Take one character from string
strD = 'HuynhDangKhoa'
strE = strD[5]
print(strE)
#Split string
strF = strD[-5:None:-1]
print(strF)
#EpsKieeur
strG = int("68")
strH = float("3.14")
strI = str(123)
print(strG, strH, strI, type(strG), type(strH), type(strI))
#Replace letter in string
strJ ="HuynhDangKhoa"
strK = strJ.replace("a", "@")
print(strK)
#Format string
strL = "My name is %s. I'm %s years old"%("Khoa", 22)
strP = "My name is {2}. I'm {1} years old. I live in {0}. My phone number is {3}.".format("HCM", 22, "Khoa", "0123456789")
print(strL)
print(strP)
#Template string
name = "Khoa"
address = "HCM"
age = 22
phone = "0123456789"
result = f"My name is {name}. I'm {age} years old. I live in {address}. My phone number is {phone}."
print(result)
#Text alignment
strQ = "{:*^10}".format("Khoa")
strQ += "{:a<10}".format("22")
strQ += "{:b>10}".format("HCM")
print(strQ)