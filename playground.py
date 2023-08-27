def add(*args):
    total =0
    for n in args:
        total += n
    print(total)

add(2,3,2)

def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n+=kwargs["add"]
    n*= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make =kw.get("make")
        self.model = kw.get("model")
        self.color =kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Ford", model="Fussion", color= "blue", seats="4")
print(my_car.seats)