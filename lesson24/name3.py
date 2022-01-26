#a=[1,2,3,4,5]
#f=list(map(lambda x:x**2,a))
#print(f)

import random

"""Zadacha2"""
#a=[random.randit(0,10) for i in range(11)]
#f=list(map(lambda x:x**3,a))
#print(f)
"""zadacha3"""

def f(i):
    if i%2==0:
        return True
    else:return False
arr=[random.randint(0,15) for i in range(10)]
y=list(filter(f,arr))
print(y)
