import ipdb

class Animal:

    all = []


    def __init__(self, name, age):
        self.name = name
        self.age = age 

        Animal.all.append(self)

    def make_animal_sound(self):
        print("Animal Sound!")


class Dog(Animal):

    all = []

    def __init__(self, name, age, odedience_level = 3, bark_volume = 3):
        super().__init__(name, age)
        self.obedience_level = odedience_level
        self.bark_volume = bark_volume

        Dog.all.append(self)
    
    def make_animal_sound(self):
        exclamation = "!" * self.bark_volume
        print(f"Bark{exclamation}")
    

class Cat(Animal):

    all = []

    def __init__(self, name, age):
        super().__init__(name, age)
        Cat.all.append(self)

    def make_animal_sound(self):
        print("Meow!")


ipdb.set_trace()