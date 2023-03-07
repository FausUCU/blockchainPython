# Follow the instructions explained in the problem video and try to implement a solution on your own. Compare it with my solution (video + downloadable files) thereafter.
# 1) Create a Food class with a “name” and a “kind” attribute as well as a “describe() ” method (which prints “name” and “kind” in a sentence).

#     class Food:
#     def  __init__(self, name, kind):
#         self.name=name
#         self.kind=kind
#     def describe(self):
#         print('im a {} of the kind {}'.format(self.name, self.kind))


# chocolate= Food('Barra de chocolate','Dulce')

# chocolate.describe()


# 2) Try turning describe()  from an instance method into a class and a static method. Change it back to an instance method thereafter.

# class Food:
#     def  __init__(self, name, kind):
#         self.name=name
#         self.kind=kind

#     @staticmethod
#     def static_describe():
#         print('im static and dont have acces to name and kind')

#     @classmethod
#     def class_describe(cls, name, kind):
#         print('class describe im a {} and my kind is {}'.format(cls.name, cls.kind))


# chocolate= Food('Barra de chocolate','Dulce')

# chocolate.static_describe()

# Food('Onion','Plant').class_describe()
# #it dosent work 


# 3) Create a  “Meat” and a “Fruit” class – both should inherit from “Food”. Add a “cook() ” method to “Meat” and “clean() ” to “Fruit”.

    #     from food import Food

    # class Meat(Food):
    #     def __init__(self, name, kind):
    #         super().__init__(name, kind)
    #         self.coccion=False
        
    #     def state(self):
    #         if self.coccion==True:
    #             print('im already done')
    #         else:
    #             print('im raw')
    #     def cook(self):
    #         self.coccion=True


    # beef=Meat('beef','cow')
    # beef.describe()
    # beef.state()
    # beef.cook()
    # beef.state()


    #==============================================================

        #     from food import Food

        # class Fruit(Food):
        #     def __init__(self, name, kind):
        #         super().__init__(name, kind)
        #         self.my_state=False
        #     def state(self):
        #         if self.my_state:
        #             print('im a dirty fruit')
        #         else:
        #             print('im a clean fruit')
        #     def clean(self):
        #         self.my_state=True
            

        # orange=Fruit('orange','Orange')

        # orange.describe()
        # orange.state()
        # orange.clean()
        # orange.state()

# 4) Overwrite a “dunder” method to be able to print your “Food” class.

    # class Food:
    #  def  __init__(self, name, kind):
    #      self.name=name
    #      self.kind=kind
    #  def describe(self):
    #     print('im a {} of the kind {}'.format(self.name, self.kind))
    #  def __repr__(self):
    #     return str(self.kind)

