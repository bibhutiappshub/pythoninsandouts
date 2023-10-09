
class Animal:
    def walk(self):
        return "Walking!!!"


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "woof!"

    def walk(self):
        return "Oscar is Walking!!"


oscar = Dog("Oscar", 8)
print(oscar.name)
print(oscar.age)
print(oscar.bark())
print(oscar.walk())

meena = Cat("Meena", 7)
print(meena.name)
print(meena.age)
print(meena.walk())
