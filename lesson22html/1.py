def a():
    b=2
    c=b*b
    yield c
    print("hello")
    yield c
    yield b
b = a()
print(next(b))
print(next(b))
print(next(b))
