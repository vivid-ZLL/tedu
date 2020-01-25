class Animal:
    def eat(self):
        print("吃东西")


class Dog(Animal):
    def bite(self):
        print("咬")


class Bird(Animal):
    def fly(self):
        print("飞︿(￣︶￣)︿")


a01 = Animal()
d01 = Dog()
b01 = Bird()
t01 = (Animal, Dog)

print(isinstance(a01, Animal), end="  ")
print(isinstance(a01, Dog))

print(issubclass(Bird, Animal), end="  ")
print(issubclass(Animal, Bird))

print(issubclass(Animal, Animal))
print(isinstance(a01, t01))
