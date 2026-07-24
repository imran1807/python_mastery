class Lion:
    def sound(slef):
        print("lion roar")
class tiger:
    def sound(self):
        print("tiger growl")
class dog:
    def sound(self):
        print("dog bark")
class pdf:
    def open(self):
        print("read pdf")
class word:
    def open(self):
        print("read word")
class Image:
    def open(self):
        print("open image")
class rectangle:
    def __init__(self,length, breadth):
        self.length=length
        self.breadth=breadth
    def __eq__(self,other):
        return (self.length==other.length and self.breadth==other.breadth)
class employee:
    def __init__(self,name,earn):
        self.name=name
        self.money=earn
    def __str__(self):
        return f"{self.name} earns rupees{self.money}"
def read_doc(file):
    file.open();      
def multiply(*numbers):
    ans=1
    for number in numbers:
        ans=ans*number
    return ans
def maximum(*numbers):
    ans=numbers[0]
    for number in numbers:
        ans=max(ans,number)
    return ans 
"""def employee(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

employee(
    name="Alice",
    age=22,
    city="Hyderabad"
)
"""


if __name__== "__main__":
   """ image1=Image()
    read_doc(image1)
    animals=[Lion(),tiger(),dog()]
    for animal in animals:
        animal.sound()"""
   print(maximum(2,1,5,3,7,4,7))
   r1=rectangle(2,9)
   r2=rectangle(3,8)
   print(r1==r2)
   e1=employee("nazir",1000)
   print(e1)
