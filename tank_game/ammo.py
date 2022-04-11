from gun import Gun

class Ammo(Gun):
    
    """ g_type = gun type
        dmg = damage
        cbr = caliber
    """

    def __init__(self, g_type):
        Gun()
        self.g_type = g_type

    g_type = ('HE_cartridge',
           'HEAT_cartridge',
           'AP_cartridge')
    
        
    def get_damage(self):
        dmg = self.cbr * 3
        return dmg

    def get_penetration(self):
        dmgarmor = self.cbr
        return dmgarmor

class HECartridge(Ammo):
    super().get_damage

class HEATCartridge(Ammo):
    super().get_damage * 0.6

class APCartridge(Ammo):
    super().get_damage * 0.3


    


        

