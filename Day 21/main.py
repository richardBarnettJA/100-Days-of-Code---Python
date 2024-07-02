#Inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

    def thinking(self):
        print("Thinking about something")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water.")

    def thinking(self):
        super().thinking()
        print("Thinking under water")

nemo = Fish()
nemo.swim()
nemo.breathe()
nemo.thinking()

