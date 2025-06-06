class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")
    
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

class Mouse(Animal):
    def speak(self):
        print(f"{self.name} says Squeak!")

dog = Dog("Buddy")
cat = Cat("Whiskers")
mouse = Mouse("Mickey")

print(dog.name) #Prints Buddy
print(dog.speak())