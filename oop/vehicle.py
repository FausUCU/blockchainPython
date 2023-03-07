class Vehicle:
    def __init__(self,starting_speed=100):
        self.top_speed=starting_speed
        self.warnings=[]
  

    def __repr__(self):
        print('imprimiendo')
        return 'Top speed {}, Warning {}'.format(self.top_speed, len(self.warnings))
    
    def add_warning(self, warning_text):
        if len(warning_text)>0:
            self._warnings.append(warning_text)

    def get_warnings(self):
        return self._warnings

    def drive(self):
        print('manejo rapido pero no mas rapido que {}'.format(self.top_speed))