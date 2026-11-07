#Creates the Parent Class
class Animal:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    def eat(self):
        print(self.name,"is eating.")
    def make_sound(self):
        print(self.name, "makes a sound")

#Creates the Child Class Lion
class Lion(Animal):
    def make_sound(self):
        print(self.name, "roars loudly!")
    def eat(self):
        print(self.name,"eats fresh meat.")

#Creates the Child Class Elephant
class Elephant(Animal):
    def make_sound(self):
        print(self.name, "trumpets!")
    def eat(self):
        print(self.name,"eats grass and fruits.")

#Creates the Child Class Monkey
class Monkey(Animal):
    def make_sound(self):
        print(self.name, "chatters!")
    def eat(self):
        print(self.name,"eats bananas.")

# Create objects
lion1 = Lion("Lionel")
elephant1 = Elephant("Epelant")
monkey1 = Monkey("Moneykey")
# Output using for loop to execute the method make_sound() of each object
animals = [lion1, elephant1, monkey1]
for animal in animals:
    animal.make_sound()
for animal in animals:
    animal.eat()