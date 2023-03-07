from food import Food

class Fruit(Food):
    def __init__(self, name, kind):
        super().__init__(name, kind)
        self.my_state=False
    def state(self):
        if self.my_state:
            print('im a dirty fruit')
        else:
            print('im a clean fruit')
    def clean(self):
        self.my_state=True
    

orange=Fruit('orange','Orange')

orange.describe()
orange.state()
orange.clean()
orange.state()

print(orange)
    