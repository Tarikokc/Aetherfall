from Entity.Character import Character

class Enemy(Character):
    
    # def __init__(self, name, pv, defense, attack, speed, stamina, dodge, agility,
    #              critical_rate, competence, status, equipment, pos_x, pos_y,symbol):
    #     super().__init__(name, pv, defense, attack, speed, stamina, dodge, agility,
    #                     critical_rate, competence, status, equipment, pos_x, pos_y,symbol)
    pass

class Wolf(Enemy) : 
   def __init__(self):
        super().__init__(
            name="Wolf", pv=200, defense=60, attack=40,
            stamina=50, dodge=0.8, agility=80,critical_rate=10,
            pos_x=0, pos_y=0,symbol="𓃥"
        )
        status="neutral"
        equipment=[], 
        
class Skeleton(Enemy) : 
   def __init__(self):
        super().__init__(
            name="Squeleton", pv=150, defense=40, attack=80,
            stamina=50, dodge=0.8, agility=80,critical_rate=10,
            pos_x=0, pos_y=0,symbol="𓀠"
        )
        status="neutral"
        equipment=[], 

class CorruptChamp(Enemy) : 
   def __init__(self):
        super().__init__(
            name="Corrupt Harroun", pv=150, defense=40, attack=80,
            stamina=50, dodge=0.8, agility=80,critical_rate=10,
            pos_x=0, pos_y=0,symbol="〠"
        )
        status="neutral"
        equipment=[]

class Bandit(Enemy) : 
   def __init__(self):
        super().__init__(
            name="Bandit", pv=150, defense=40, attack=80,
            stamina=50, dodge=0.8, agility=80,critical_rate=10,
            pos_x=0, pos_y=0,symbol="𓀪"
        )
        status="neutral"
        equipment=[]

class Boss(Enemy) : 
   def __init__(self):
        super().__init__(
            name="Magellan", pv=150, defense=40, attack=80,
            stamina=50, dodge=0.8, agility=80,critical_rate=10,
            pos_x=0, pos_y=0,symbol="𓆌"
        )
        status="neutral"
        equipment=[]