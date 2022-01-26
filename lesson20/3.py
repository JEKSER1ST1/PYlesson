list1=["zheka","den","vova","sasha"]
def name():
    for t in list1:
        yield t
a=name()
for i in a:
    print(i)
