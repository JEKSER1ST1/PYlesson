def gen(n):
    a,b=1,1
    for i in range(n):
        yield a
        a,b=b,a+b
n=int(input("vvedite "))
t=list(gen(n))
print(t)
for i in t:
    print(i)
