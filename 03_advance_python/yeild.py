def file1():
    yield "A"
    yield "B"

def file2():
    yield "C"
    yield "D"

def file3():
    yield "E"
def infiniteeven():
    num=2
    while True:
        yield num
        num=num+2

def read_all():


    yield from file1()
    yield from file2()
    yield from file3()

for i in infiniteeven():
    print(i)

