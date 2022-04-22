
class Engine:
    """ Класс двигателя """

    def __init__(self,v6,v8,v10,horse_power,
    acceleration_factor):
        self.v6 = v6
        self.v8 = v8
        self.v10 = v10
        self.horse_power = horse_power
        self.acceleration_factor = acceleration_factor

    def generate_power1_v6(self):
        print(self.horse_power * self.v6//self.acceleration_factor)
        
    def generate_power2_v8(self):
        print(self.horse_power * self.v8//self.acceleration_factor)
        
    def generate_power3_v10(self):
        print(self.horse_power * self.v10//self.acceleration_factor)
        

power = Engine(0.2, 0.4, 0.6, 180 , 0.8)
power.generate_power1_v6()
power.generate_power2_v8()
power.generate_power3_v10()


#_____________________________________________________________

class Wheel:
    """ Класс колес"""
    
    def __init__(self, diametr, wheel_weight):
        self.diametr = diametr
        self.wheel_weight = wheel_weight
    
    def check_range(self):
        if 16 < self.diametr < 21:
            print('Диаметр колес подходит!' + ' ' + 
            'Колесо весит ' +
            str(self.wheel_weight) + ' ' + 'kg')
    
bmw = Wheel(17, 10)
bmw.check_range()

#________________________________________________________________
pass

class Car:
    def __init__(self, car_type, car_weight):
        super().__init__()
        self.car_type = car_type
        self.car_weight = car_weight

    def start_engine_bmw(self):
        print('По коням!')

        




bmw = Car('седан', 1200)
bmw.start_engine_bmw()

    
    











