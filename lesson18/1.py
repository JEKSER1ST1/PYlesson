import random
n= int(input("vvesti n:"))
m= int(input("vvesti m:"))
massive=[ [random.randint(1,9) for r in range(m)] for a in range(n)]
print("matrica --->")
for r in massive:
        print(f"\t\t{r}")
massive2=[massive[a][r] for a in range(n) for r in range(m) if a==r]
print(f"Главная диагональ ------> {massive2}")
massive3=[massive[a][r] for a in range(n) for r in range(m) if a==1]
print(f"Вторая строка ------> {massive3}")
massive4=[massive[a][r] for a in range(n) for r in range(m) if r==2]
print(f"Третий столбец ------> {massive4}")
