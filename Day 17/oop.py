#Object Oriented Programming

class User:
    def __init__(self, name):
        self.name = name
        self.followers = 0
        print("New User Created!")

    def add_follower(self):
        self.followers += 1
        print(f"Followers: {self.followers}")



user_1 = User("Richard Barnett")
print(user_1.name)
user_1.add_follower()