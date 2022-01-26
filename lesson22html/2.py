def gen():
    x=2
    print("First perebor")
    yield x
    x*=2
    print("Second perebor")
    yield x
    x/=2
    print("Third perebor")
    yield x
a=gen()
#print(next(a))
#print(next(a))
#print(next(a))
for i in gen():
    print(i)
