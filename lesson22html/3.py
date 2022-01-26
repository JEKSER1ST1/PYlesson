n = int(input("Kol-vo: "))
def gen():
    a,b=1,1
    for i in range(n):
        yield a
        a,b=b,a+b

for i in gen():
    print(i)
