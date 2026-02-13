from Battle.Status import Status

class Character :
    def __init__(self, name, pv, defense, attack, stamina, dodge, agility,
                 critical_rate, pos_x, pos_y, symbol=""):  
        self.name = name
        self.pv = pv
        self.defense = defense
        self.attack = attack  
        self.stamina = stamina
        self.dodge = dodge
        self.agility = agility
        self.critical_rate = critical_rate
        self.symbol = symbol  
        self.skill = []
        self.status = []
        self.equipment = []
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def is_alive(self) :
        return self.pv > 0 
        
    def add_status(self,status) : 
        self.status.append(status)
        print(f" {self.name} Is affected by: {status.get_name()}")
        
    def equip_item(self,item) : 
        self.equipment.append(item)

        if item.type == "weapon" or item.type== "armor" :
            for stat, value in item.stat_bonus.items() : 
                if stat == "attack" :
                    self.attack += value
                elif stat == "defense" : 
                    self.defense += value 
                elif stat == "agility":
                    self.agility += value
                elif stat == "critical_rate":
                    self.critical_rate += value 
        
        print(f" {item.name} is equipped by {self.name}")
  
    
