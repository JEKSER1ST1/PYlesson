class Car:
    def __init__(self,marka,models,age):
        self.marka=marka
        self.models=models
        self.age=age
        self.adometr=adometr=0
        print("car creat")
    def get_descript_name(self):
        print(f"Машина марки - {self.marka}, модель-{self.models},{self.age} года")
    def read_adometr(self):
        print(f"Пробег машины -- {self.adometr}")
    def update_adometr(self,n):
        if n>=self.adometr:
            self.adometr=n
        else: print("Пробег изменить нельзя")

    def increment_adometr(self,m):
        self.adometr+=m
        print(f"Пробег вашей машины {self.adometr}" )

class Electro_Car(Car):
    def __init__(self,marka,models,age):
        Car.__init__(self,marka,models,age)
        self.batareya=0
    def name_electro_Car(self):
        print(f"Машина марки - {self.marka}, модель-{self.models},{self.age} года")
    def new_batareya(self,bat):
        self.batareya=bat
        print(f"Батарея модели {self.batareya}")
        

my_new_car=Car("AYDI","RS8",2015)
my_new_car.get_descript_name()
my_new_car.adometr=23

n=int(input("Введите значение пробега -"))
m=int(input("Введите значение пробега после этоГО - "))

my_new_car.update_adometr(n)
my_new_car.read_adometr()
my_new_car.increment_adometr(m)
my_new_electre_car=Electro_Car("Tesla","XX", 2021 )
bat=int(input("Введите значение батареи -"))
my_new_electre_car.name_electro_Car()
my_new_electre_car.new_batareya(bat)
