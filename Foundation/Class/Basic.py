# Creating dynamic class using the class keyword
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def print_car(self):
        return f'The car is {self.name} ' f'and its {self.color} in color'
    

car1 = Car('BMW', 'Green')
print('dynamic class using class keyword ' + car1.print_car())


# Creating dynamic class using the type keyword
def cars_init(self, name ,color):
    self.name = name
    self.color = color
Cars = type("Car",(),
            {'__init__': cars_init,
'print_car':lambda self:
f'The car is {self.name} '
f'and its {self.color} in color'})
car1 = Cars("BMW", "Green")
print('dynamic class using type keyword ' + car1.print_car())