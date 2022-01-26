def gen():
    i=1
    while True:
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
                else:
                    yield i
        i+=1
for g in gen():
    print(g)
