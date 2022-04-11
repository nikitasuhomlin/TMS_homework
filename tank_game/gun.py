import random

class Gun:

    def __init__(self, calibr: int, turret_length: int) -> None:
        self.calibr = calibr
        self.turett_length = turret_length
       
        
       
    def is_on_target(self, dice = (random.randint(1,6))):
        result = self.calibr * dice > 100
      
        return result 




    
    
    

