class Human:
    def __init__(self,name,surname,place_of_bth,year,age):
        self.name=name
        self.surname=surname
        self.place_of_bth=place_of_bth
        self.year=year
        self.age=age
        print("gotovo")
    def hello(self):
        print(f"Name:{self.name},Surname:{self.surname},Place:{self.place_of_bth},Year:{self.year},Age:{self.age}")
    def vozrast(self,n):
        return n-self.year


n=int(input("DDD ="))
p1=Human("Zheka","Tataru","UA",2004,17)
p1.hello()
t = p1.vozrast(n)
print(t)
p2=Human("Den","Dmiteiev","UA",1997,24)
p2.hello()
m=p2.vozrast(n)
print(m)
class Circle:
    PI=3.14
    C=0
    def __init__(self,radius):
        self.radius=radius
        Circle.C+=1
        print("kolo")
    def dlina(self):
        print(f"{2*self.PI*self.radius}")
    def plosha(self):
        print(f"{self.PI*self.radius**2}")

kolo1=Circle(7)
kolo1.dlina()
kolo1.plosha()
kolo2=Circle(9)
kolo2.dlina()
kolo2.plosha()
print(Circle.C)
