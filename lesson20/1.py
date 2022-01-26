def y(n):
    print("perebor1")
    yield n
    print("perebor2")
    yield n+1
m=int(input("vvedite --> "))
v=y(m)
print(next(v))
print(next(v))
