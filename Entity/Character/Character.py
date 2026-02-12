class Character :
    def __init__(self,name,pv,defense,force,stamina,dodge, agility,
                 critical_rate,competence, status,equipement,pos_x,pos_y ) : 
        self.name = name
        self.pv = pv
        self.defense = defense 
        self.force = force 
        self.stamina = stamina 
        self.dodge = dodge
        self.agility = agility
        self.critical_rate = critical_rate 
        self.competence = [] 
        self.status = "neutral"
        self.equipement = [] 
        self.pos_x = pos_x 
        self.pos_y = pos_y

    def show(self) :
        return f"{self.name}"
    
    
    
    
