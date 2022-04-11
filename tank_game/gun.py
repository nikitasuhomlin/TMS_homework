class Gun:
    
    """ cbr = calibr
        tbl = turret barell length
        dmg = damage
        a_dmg = armor damage
    """
    cbr = (
        30,
        40,
        50,
    )

    tbl = (
        40,
        50,
        60
    )


    def __init__(
        self, dmg, crithit, dice,
        is_on_target: bool = False) -> None:

        self.dmg = dmg
        self.crithit = crithit
        self.is_on_targer = is_on_target
        self.dice = []

    def hitornot(self):
        result = (self.tbl * self.dice)> 100
        return result 




    
    
    

