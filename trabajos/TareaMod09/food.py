class Food:
     def  __init__(self, name, kind):
         self.name=name
         self.kind=kind
     def describe(self):
        print('im a {} of the kind {}'.format(self.name, self.kind))
     def __repr__(self):
        return str(self.kind)
