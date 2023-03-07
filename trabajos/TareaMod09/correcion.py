# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).
# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.

class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        return f"{self.name} is a {self.kind}."


class Meat(Food):
    def cook(self):
        return f"Cooking the {self.name}..."


class Fruit(Food):
    def clean(self):
        return f"Cleaning the {self.name}..."


print('Solution 1 and 3')
food = Food("apple", "fruit")
print(food.describe())

meat = Meat("steak", "meat")
print(meat.describe())
print(meat.cook())

fruit = Fruit("banana", "fruit")
print(fruit.describe())
print(fruit.clean())
print('-' * 20)

# 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.

class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    @classmethod
    def describe(cls, name, kind):
        return f'{name} is a {kind}'


print('Solution 2:')
print(Food.describe('Apple', 'fruit'))
print('-' * 20)

# 4) Overwrite a “dunder” method to be able to print your “Food” class.

class Food:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def describe(self):
        return f"{self.name} is a {self.kind}."

    def __str__(self):
        return self.describe()


print('Solution 4')
food = Food("Apple", "fruit")
print(food)
