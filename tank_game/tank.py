from armor import Armor
from gun import Gun
from ammo import Ammo
from typing import List

class Tank:
    def __init__(self,model:str, gun: Gun, armors: List[Armor], ammos: List[Ammo], health: int):
        self.model = model
        self.gun = gun
        self.armors = armors
        self.ammos = ammos
        self.health = health

    def _add_armors(self,width:int):
        self.armors.append(List[Armor])
        
    



