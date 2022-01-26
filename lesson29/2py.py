class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("Person created")
    def hello(self):
        print(f"{self.name} says hello")
class Student(Human):
    def __init__(self,name,age,course,mark):
        Human.__init__(self,name,age)
        self.course=course
        self.mark=mark
    def study(self):  #метод#
        print(f"{self.name} studing")
    def info_university(self):
        print(f"{self.name} studing on {self.course} course and have mark {self.mark}")
    def hello(self):
        print(f"Student created, {self.name} not says hello")
class Teacher(Human):
    def teach(self):
        print(f"{self.name}-teachs, age:{self.age}")
              
s1=Student("Zheka",17,1,5)
t1=Teacher("Sasha",16)
#s2=Student("Vova",15)
t2=Teacher("Vlad",16)
s1.hello()
s1.info_university()
#s1.hello()
#s2.hello()
#t1.hello()
#t2.hello()              
#s1.study()
#s2.study()
#t1.teach()
#t2.teach()


              
