def den ():
    b=2
    d=b**b
    yield d
    print("Привет")
    yield b
t=den()
print(next(t))
print(next(t))
next
