"""
    继承和多态
    获取对象信息
"""
class Animal:
    def __init__(self, name, meat):
        self.name = name
        self.meat = meat
    def run(self):
        print("Animal is running")

class Dog(Animal):
    def __init__(self, name, meat):
        super().__init__(name, meat)
    def run(self):
        print("Dog is running")

class Cat(Animal):
    def __init__(self, name, meat):
        super().__init__(name, meat)
    def run(self):
        print("Cat is running")

Dog = Dog("雪纳瑞", "骨头")
Cat = Cat("狸花猫","鱼刺")
animal = Animal("动物","需要")
def run(animal):
    animal.run()

run(animal)
run(Dog)
run(Cat)
print(type(animal))
print(type(Dog))
print(isinstance(animal, Animal))
print(isinstance(Dog, Animal))
print(hasattr(Animal, "run"))
print(hasattr(Dog, "name"))
print(dir(Cat))