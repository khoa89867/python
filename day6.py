###################################CONDITIONAL STATEMENTS###################################
a = 10 
b = 20
if a > b:
    print("a lon hon b")
elif a < b:
    print("a be hon b")

age = 22
if age < 18:
    print("Chua du tuoi")
elif age < 30:
    print("Tuoi thanh nien")

diem = 20
if diem < 0 or diem > 10:
    print("Diem khong hop le")
elif diem >= 8:
    print("Gioi")
elif diem >= 6.5:
    print("Kha")
elif diem >= 4:
    print("Trung binh")
else:
    print("Yeu")

################################WHILE LOOP###################################

k = 1
while k < 6:
    print(k, ". I love you")
    k += 1

str = "Huynh Dang Khoa"
i = 0
while i < len(str):
    if i == len(str) - 1:
        print(str[i], end='\n')
    else:
        print(str[i], end='-')
    i += 1

# from random import randint

# list = ["Keo", "Bua", "Bao"]
# j = 0
# while True:
#     i  = randint(0, 2)
#     input_str = input("Nhap vao keo, bua hoac bao: ")
#     if input_str not in list:
#         print("Nhap sai, vui long nhap lai")
#         continue
#     elif list.index(input_str) == i:
#         print(f"Ban da chon {input_str}, hoa voi may")
#     elif (i % 3) == list.index(input_str):
#         print(f"Ban da chon {input_str}, ban thang")
#     else:
#         print(f"Ban da chon {input_str}, ban thua")
#     print("May da chon", list[i])
#     j += 1
#     if j == 5:
#         print("Het luot choi")
#         break

five_odd_number = []
k = 0
while len(five_odd_number) < 6:
    if k % 2 == 0: 
        five_odd_number.append(k)
        k+=1
        continue
    k += 1
print("5 so chan dau tien la:", five_odd_number)

################################FOR LOOP###################################

for i in range(1, 6):
    print(i, ". I love you")

for i in (1, 4, 2, 6, 10, 7):
    print(i, end=' ')
else: 
    print("Done") 

set = {5, 8, 1, 9, 4}
sum = 0
for i in set:
    sum += i
print("Tong cac phan tu trong set la:", sum)

x = range(1, 11)
print(x[6])
print(list(range(11, 1, -1)))

list = [1, (2, 3), "Huynh Dang Khoa", 3.14, True]
for i in range(len(list)):
    print(list[i])

#Comprehension
list2 = ['-'.join((a.title(), b.upper(),  c.lower())) for a, b, c in [("huynh", "dang", "khoa"), ("nguyen", "van", "a"), ("le", "thi", "b")]]
print(list2)
