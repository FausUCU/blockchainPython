from food import Food

class Meat(Food):
    def __init__(self, name, kind):
        super().__init__(name, kind)
        self.coccion=False
    
    def state(self):
        if self.coccion==True:
            print('im already done')
        else:
            print('im raw')
    def cook(self):
        self.coccion=True
    


beef=Meat('beef','cow')
print(beef)
#print(beef.state())
