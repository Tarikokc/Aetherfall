from Entity.Character import Character

class Hero(Character):
    
    def __init__(self, name, pv, defense, force, stamina,
                 dodge, agility, critical_rate, pos_x, pos_y):

        super().__init__(name, pv, defense, force, stamina,
                         dodge, agility, critical_rate, pos_x, pos_y)

        self.symbol = ""
        self.speed = 50
        
        
    def statistics(self):
        print("\n" + "=" * 50)
        print(f"{'STATISTICS':^50}")
        print("=" * 50)
        print(f"Name           : {self.name}")
        print(f'Classname      : {self.__class__.__name__}')
        print(f"Position       : {self.pos_x}, {self.pos_y}")
        print(f"Symbol         : {self.symbol}")
        print("-" * 50)
        print(f"PV             : {self.pv}")
        print(f"Defense        : {self.defense}")
        print(f"Strenght       : {self.force}")
        print(f"Speed          : {self.speed}")
        print(f"Endurance      : {self.stamina}")
        print(f"Dodge          : {self.dodge}")
        print(f"Agility        : {self.agility}")
        print(f"Critical Rate  : {self.critical_rate}%")
        print("=" * 50 + "\n")


class Mage(Hero) : 
    def __init__(self, name):
        super().__init__(
            name=name,
            pv=100,
            defense=70,
            force=50,
            stamina=50,
            dodge=0.5,
            agility=50,
            critical_rate=10,
            pos_x=0,
            pos_y=0,
        )
        self.mana = 150
        self.magic_attack = 80
        self.statistics()


    def statistics(self):
        print("\n" + "=" * 50)
        print(f"{'STATISTICS':^50}")
        print("=" * 50)
        print(f"Name           : {self.name}")
        print(f'Classname      : {self.__class__.__name__}')
        print(f"Position       : {self.pos_x}, {self.pos_y}")
        print(f"Symbol         : {self.symbol}")
        print("-" * 50)
        print(f"PV             : {self.pv}")
        print(f"Defense        : {self.defense}")
        print(f"Strenght       : {self.force}")
        print(f"Speed          : {self.speed}")
        print(f"Endurance      : {self.stamina}")
        print(f"Dodge          : {self.dodge}")
        print(f"Agility        : {self.agility}")
        print(f"Critical Rate  : {self.critical_rate}%")
        print(f"Magic Attack   : {self.magic_attack}")
        print(f"Mana           : {self.mana}")

        print("=" * 50 + "\n")

        
class Thief(Hero) : 
   def __init__(self, name):
        super().__init__(
            name=name,
            pv=100,
            defense=70,
            force=50,
            stamina=50,
            dodge=0.8,
            agility=80,
            critical_rate=10,
            pos_x=0,
            pos_y=0
        )
        self.symbol = "𓀡"
        self.speed = 60
        self.statistics()



    
class Warrior(Hero) : 
   def __init__(self, name):

        super().__init__(
            name=name,
            pv=150,
            defense=80,
            force=80,
            stamina=60,
            dodge=0.3,
            agility=50,
            critical_rate=15,
            pos_x=0,
            pos_y=0
        )

        self.symbol = "𓀛"
        self.speed = 60
        self.statistics()

