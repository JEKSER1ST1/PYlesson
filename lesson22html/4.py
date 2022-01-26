def gen():
    i=1
    p=0
    while 1:
        for j in range(2,i):
            if i%j==0:
                p+=1
        if p==0:
            yield i
        else:
            p=0
        i+=1
for k in gen():
    print(k)
