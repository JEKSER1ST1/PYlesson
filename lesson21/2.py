def gen():
    x=2
    print("Первый перебор")
    yield x
    x*=2
    print("Второй перебор")
    yield x
    x/=2
    print("Третий перебор")
    yield x
t =gen()
for j in gen():
    print(j)
#print(next(t))
#print(next(t))
#print(next(t))
