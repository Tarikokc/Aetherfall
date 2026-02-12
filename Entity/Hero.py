import copy
from Entity.Character import Character
from Environment.Forest import Forest
from Environment.Village import Village
from Environment.Map import Map

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

    def move(self,move,map):

        while move:
            position = [copy.deepcopy(self.pos_x), copy.deepcopy(self.pos_y)]
            Village()
            key = input("")
            if key == "q":
                self.pos_y -=1
            elif key == "z":
                self.pos_x -= 1
            elif key == "f":
                self.pos_y +=1
            elif key == "d":
                self.pos_x +=1
            elif key == "i":
                print("trigger inventory")

            print(self.pos_x, self.pos_y)
            print(position)

            if [self.pos_x, self.pos_y] in map.house_position:
                self.pos_x = copy.deepcopy(position[0])
                self.pos_y = copy.deepcopy(position[1])
                print("Physical barrier in the direction you choose, turn around")
                break

            if self.pos_x > Map.MAX_WIDTH - 1 or self.pos_y > Map.MAX_HEIGHT - 1 or self.pos_x == -1 or self.pos_y == -1 :
                print("")
                print(self.pos_x, self.pos_y)
                print(position)
                self.pos_x = copy.deepcopy(position[0])
                self.pos_y = copy.deepcopy(position[1])
                print(self.pos_x, self.pos_y)
                print(position)

                print("Out of the map, turn around")
                break

            map.hero_moving(self,position)

        


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

