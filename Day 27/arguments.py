# Advanced Python Arguments


def foo(a, b=4, c=6): 
    print(a, b, c)
 
foo(1, 7, 9)
foo(1)


# * is what is important, not args. *args is a tuple
def add(*args):
    num = 0
    for n in args:
        num += n
    print(num)

add(1, 2, 3, 4)
add(20, 30, 50)



# kwargs stands for key word arguments. **kwargs is a dictionary
def calculate(**kwargs):
    for (key, value) in kwargs.items():
        print(key)
        print(value)
 
calculate(add=20, multiply=30)



# .get is used so that if said value is not passed, it will not return an error
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

car = Car(make="Nissan")
print(car.make)