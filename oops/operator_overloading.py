class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        if self.age > other.age :
            return True
        else:
            return False

sheru = Dog("Sheru", 5)
rockey = Dog("Rockey", 10)

# We have to findout which Dog is older by comparing the two Dog objects
print(sheru > rockey)