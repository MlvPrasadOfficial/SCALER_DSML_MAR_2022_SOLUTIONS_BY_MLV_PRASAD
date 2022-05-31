class Animal:
    def __init__(self):
        print("Animal is Here")

    def sound(self):
        print("Animal Sounds")
        
# Define class Dog
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__()
        self.name = name
        self.breed = breed
        
    def getname(self):
        return name
    
    def getbreed(self):
        return breed

    def sound(self):
        print("Dog Barks")

# Define class Cat
class Cat(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def getname(self):
        return name
    
    def getbreed(self):
        return breed
    
    def sound(self):
        print("Cat Meows")


def main():
# Create the instances for the classes here
    A1 = Animal()
    A1.sound()
    D1 = Dog("Bolt", "Doberman")
    D1.sound()
    C1 = Cat("Robin", "Persian")
    C1.sound()