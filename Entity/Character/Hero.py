from Entity.Character.Character import Character

class Hero(Character):
    
    def __init__(self, name, pv, defense, force, speed, stamina, dodge, agility,
                 critical_rate, competence, status, equipement, pos_x, pos_y,symbol):
        super().__init__(name, pv, defense, force, speed, stamina, dodge, agility,
                        critical_rate, competence, status, equipement, pos_x, pos_y,symbol)


class Mage(Hero) : 
   def __init__(self, name):
        super().__init__(
            name=name, pv=100, defense=70, force=50, speed=60,
            stamina=50, dodge=0.5, agility=50,critical_rate=10, competence=[],
            status="neutral", equipement=[], pos_x=0, pos_y=0,symbol="𓀬"
        )
        self.mana = 150
        self.magic_attack = 80
        
class Thief(Hero) : 
   def __init__(self, name):
        super().__init__(
            name=name, pv=100, defense=70, force=50, speed=60,
            stamina=50, dodge=0.8, agility=80,critical_rate=10, competence=[],
            status="neutral", equipement=[], pos_x=0, pos_y=0,symbol="𓀡"
        )
    
class Warrior(Hero) : 
   def __init__(self, name):
        super().__init__(
            name=name, pv=150, defense=80, force=80, speed=60,
            stamina=50, dodge=0.8, agility=80,critical_rate=10, competence=[],
            status="neutral", equipement=[], pos_x=0, pos_y=0,symbol="𓀛"
        )