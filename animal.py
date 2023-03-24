class Animal:
    count = 0

    def __init__(self, kind, age):
        self.kind = kind
        self.age = age
        Animal.count += 1


pochi = Animal("犬", 5)
tama = Animal("猫", 3)
print(pochi.kind, pochi.age)
print(tama.kind, tama.age)
print(Animal.count)
