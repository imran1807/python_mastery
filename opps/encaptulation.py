class Student:
    def __init__(self):
        self.name="nazir"
        self._marks=20
        self.__grade="a"
    def getgrade(self):
        return self.__grade
    

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
        self.__password=1234
    
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,password):
        self.__password=password
    

if __name__=="__main__":
    s1=Student()
    print(s1.name)
    print(s1._marks)
    print(s1._Student__grade)
    e1=Employee('imran',1000)
    e1.password=1234
    print(e1.name)
    print(e1._salary)
    print(s1.getgrade())
    print(e1.password)



    

