#Creates the Parent Class
class Animal:
    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name

#Creates the Child Class Lion
class Lion(Animal):
    #

#Creates the Child Class Elephant
class Elephant(Animal):
    #

#Creates the Child Class Monkey
class Monkey(Animal):
    #