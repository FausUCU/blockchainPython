from vehicle import Vehicle
class Bus(Vehicle):
    def __init__(self, starting_speed=100):
        super().__init__(starting_speed)#para agrwegar el constructor de vheicle, si no lo ago cunado pongo cualquier constructor en bus sobrescribo el de vheicle
        self.passengers=[]

    def add_group(self, passengers):
        self.passengers.extend(passengers)

b1=Bus(150)
b1.drive()