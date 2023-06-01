""" INHERITANCE """


class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print("Moving in water.")


nemo = Fish()
tiger = Animal()
nemo.swim()
print("--------------------")
tiger.breathe()
print("--------------------")
nemo.breathe()
print("--------------------")
print(tiger.num_of_eyes)
print(nemo.num_of_eyes)
