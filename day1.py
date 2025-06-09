#Variable
a = 18
b = "Khoa"
c = 3.14
#Type of variable
print(type(a), type(b), type(c))


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
#Mu