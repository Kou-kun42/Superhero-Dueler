class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    def bark(self):
        print("Woof!")


my_Dog = Dog("Rex", "SuperDog")
print(my_Dog.name)

print(my_Dog.breed)

my_Dog.bark()
