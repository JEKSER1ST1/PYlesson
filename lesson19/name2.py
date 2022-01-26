import random
n=int(input("Введите количество ---:    "))
m=int(input("Введите количество ---:    "))
A=[[random.randint(1,9) for i in range(m)] for r in range(n)]
print(A)
for i in A:
    print(i)
c=[A[r][i] for r in range(n) for i in range(m)if r==i]
print(f"главная диагональ --  {c} ")
b=[A[3][r] for r in range(m) if r==4]
print(b)
