from gun import Gun

class Ammo:
    
    AMMO_TYPES = {
        1: 'HE_cartridge',
        2: 'HEAT_cartridge',
        3: 'AP_cartridge',
    }

    def __init__(self, gun: Gun, ammo_type):
        self.gun = gun
        self.ammo_type = self.AMMO_TYPES[ammo_type]

        
    def get_damage(self):
        dmg = self.gun.calibr * 3
        return dmg

    def get_penetration(self):
        return self.gun.calibr


class HECartridge(Ammo):
    def __init__(self, gun: Gun, ammo_type):
        super().__init__(gun, ammo_type)


class HEATCartridge(Ammo):
    def __init__(self, gun: Gun, ammo_type):
        super().__init__(gun, ammo_type)
    
    def get_damage(self):
        return super().get_damage() * 0.6


class APCartridge(Ammo):
    def __init__(self, gun: Gun, ammo_type):
        super().__init__(gun, ammo_type)
    
    def get_damage(self):
        return super().get_damage() * 0.3

    


        

