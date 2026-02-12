from Entity.Character.Character import Character

class Ennemy(Character):
    
    def __init__(self, name, pv, defense, force, speed, stamina, dodge, agility,
                 critical_rate, competence, status, equipement, pos_x, pos_y,symbol):
        super().__init__(name, pv, defense, force, speed, stamina, dodge, agility,
                        critical_rate, competence, status, equipement, pos_x, pos_y,symbol)


class Wolf(Ennemy) : 
   def __init__(self, name):
        super().__init__(
            name="Wolf", pv=150, defense=80, force=80, speed=60,
            stamina=50, dodge=0.8, agility=80,critical_rate=10, competence=[],
            status="neutral", equipement=[], pos_x=0, pos_y=0,symbol="𓃥"
        )
        
class Skeleton(Ennemy) : 
   def __init__(self, name):
        super().__init__(
            name="Squeleton", pv=150, defense=80, force=80, speed=60,
            stamina=50, dodge=0.8, agility=80,critical_rate=10, competence=[],
            status="neutral", equipement=[], pos_x=0, pos_y=0,symbol="𓀠"
        )

class CorruptChamp(Ennemy) : 
   def __init__(self, name):
        super().__init__(
            name="Corrupt Harroun", pv=150, defense=80, force=80, speed=60,
            stamina=50, dodge=0.8, agility=80,critical_rate=10, competence=[],
            status="neutral", equipement=[], pos_x=0, pos_y=0,symbol="〠"
        )

class Bandit(Ennemy) : 
   def __init__(self, name):
        super().__init__(
            name="Bandit", pv=150, defense=80, force=80, speed=60,
            stamina=50, dodge=0.8, agility=80,critical_rate=10, competence=[],
            status="neutral", equipement=[], pos_x=0, pos_y=0,symbol="𓀪"
        )

class Boss(Ennemy) : 
   def __init__(self, name):
        super().__init__(
            name="Magellan", pv=150, defense=80, force=80, speed=60,
            stamina=50, dodge=0.8, agility=80,critical_rate=10, competence=[],
            status="neutral", equipement=[], pos_x=0, pos_y=0,symbol="𓆌"
        )