#ZADACHA1
print("#ZADACHA1")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i<5:
        print(i)
print("============")        
#ZADACHA2
print("#ZADACHA2")
import random
n=int(input("n= "))
b=[random.randint(0,15) for r in range(n)]
print(b)
print(b[0])
print(b[-1])
c=1
print("============")
for i in b:
    c*=i
    
    print(c)
print("============")
#ZADACHA3
print("#ZADACHA3")
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217]

for i in numbers:
    if i%2==0:
        print(i)
    elif i==237:
        break
        
        print(i)
        
print("============")
#ZADACHA4
print("#ZADACHA4")
age=int(input("age= "))
if age<2:
    print("Младенец")
elif age>=2 and age<4:
    print("Малыш")
elif age>=4 and age<13:
    print("ребенок")   
elif age>=13 and age<20:
    print("подросток")
elif age>=20 and age<65:
    print(" взрослый")
else:
    print("пожилой человек")
print("============")
#ZADACHA5
print("#ZADACHA5")
z=["sad","sad","sad"]
v=[]
while z:
    del_users=z.pop(0)
    b.append(del_users)
print("============")    
for i in b:
    print(f"user{i} gotovo ")
print("============")     
#ZADACHA6
print("#ZADACHA6")
bluda=['pizza', 'falafel', 'carrot cake']
d1=bluda[:]
print(bluda)
print(d1)
m=(input("bludo= "))
d1.append(m)
print(d1)
print("============")
for i in d1:
    print(i)
print("============")
for i in bluda:
    print(i)
print("============")
#ZADACHA7
print("#ZADACHA7")
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
o=1
for i in lst:
    if i<30 and i%3==0:
        print(i)
    else:
       o+=i
       print(i)
print("============")       
#ZADACHA8
print("#ZADACHA8")
slov={'a': 2, 'b': 4, 'c': 6, 'd': 8}
for a,b in slov.items():
    if b>2:
        print(b)
print("============")         
#ZADACHA9
print("#ZADACHA9")
spisok1=["red","blue","green","yelow","white","grey"]
spisok2=[1,3,7,2,6,10]
slovar9=dict(zip(spisok1,spisok2))
j=int(input("степень --> "))
for i,x in slovar9.items():
    h=x**n
print(f"Я знаю твой ключ – {i}, его значение является {h}")
print(slovar9)    
print("============") 
#ZADACHA11
print("#ZADACHA11")
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(dic)
for x,z in dic.items():
    if z%2 == 0:
        print("even")
    else:
        print("odd")
print("============") 
#ZADACHA12
print("#ZADACHA12")
import random
n=int(input("Количество рядков --> "))
m=int(input("Количество столбцов --> "))
A=[[random.randint(1,9) for i in range(m)] for r in range(n)]
print("--------------------")
for i in A:
    print(i)
c=[A[r][i] for r in range(n)for i in range(m)if r==i]
print(f"главная диагональ --> {c}")
w=int(input("строка= "))
g=int(input("столбец= "))
u=A[w-1]
t=A[g-1]
print(f"вы выбрали строку: {u}")
print(f"вы выбрали столбец: {t}")
b=[A[w-1][g-1]]
print(f"индекс  --> {b}")