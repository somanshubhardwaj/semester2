class Animal:
    def __init__(self, species):
        self.species = species
    
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


if __name__ == "__main__":
    dog = Dog("Canine")
    cat = Cat("Feline")
    
    print("Dog says:", dog.speak())
    print("Cat says:", cat.speak())
