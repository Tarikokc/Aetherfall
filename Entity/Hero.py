import copy
import random
from Entity.Character import Character
from Environment.Forest import Forest
from Environment.Village import Village
from Environment.Map import Map
from Event.Event import Event
from Event.PNJ import PNJ
from Environment.Village import Village
from Factory.EnemyFactory import EnemyFactory  
from Inventory.Inventory import Inventory
from Battle.Fight import Fight
from Battle.Skill import Skill
from Factory.EnemyFactory import EnemyFactory
class Hero(Character):
    
    def __init__(self, name, pv, defense, attack, stamina,
                 dodge, agility, critical_rate, pos_x, pos_y):

        super().__init__(name, pv, defense, attack, stamina,
                         dodge, agility, critical_rate, pos_x, pos_y)

        self.symbol = ""
        self.speed = 50
        self.quest={"start":True,"pnj":False,"key":False,"Boss":False}
        self.map = Village()
        self.inventory = Inventory()


        self.beaten = 0
        
        
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
        print(f"Strenght       : {self.attack}")
        print(f"Speed          : {self.speed}")
        print(f"Endurance      : {self.stamina}")
        print(f"Dodge          : {self.dodge}")
        print(f"Agility        : {self.agility}")
        print(f"Critical Rate  : {self.critical_rate}%")
        print("=" * 50 + "\n")

    def move(self,move):
        while move:
            position = [copy.deepcopy(self.pos_x), copy.deepcopy(self.pos_y)]
            can_move = True
            stayed = False
            self.map.display_map()
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
                self.inventory.display_item()
            print(self.pos_x, self.pos_y)
            print(position)

            if self.pos_y ==  Map.MAX_HEIGHT:
                choice = input("Would you like to go on the Forest ? \n")
                if choice == "yes":
                    self.map = Forest()
                    self.pos_x = 0
                    self.pos_y = 0
                else:
                    print(f"{self.name} : I stay in the {self.map.__class__.__name__} for the moment")
                    stayed = True
                    can_move = False
            
            elif self.map.__class__.__name__ == "Forest":
                if [self.pos_x,self.pos_y] in self.map.house_position and self.map.visual[self.pos_x][self.pos_y] != "𖢔" and self.map.visual[self.pos_x][self.pos_y] != "𖤝":
                    print("ENNEMY TRIGGERED")
                    enemy_index = random.randint(0,len(EnemyFactory.ENNEMY_TYPE)-1)
                    enemy = EnemyFactory.create(EnemyFactory.ENNEMY_TYPE[enemy_index])
                    Fight(self,enemy).fight_enemy()
                    
            elif self.pos_x > Map.MAX_WIDTH - 1 or self.pos_y > Map.MAX_HEIGHT - 1 or self.pos_x == -1 or self.pos_y == -1 :
                self.pos_x = copy.deepcopy(position[0])
                self.pos_y = copy.deepcopy(position[1])
                print("Out of the map, turn around")
                break

                elif [self.pos_x,self.pos_y] in self.map.house_position and self.map.visual[self.pos_x][self.pos_y] == "𖤝":
                    print("KEY OBTAINED")
                    self.quest["key"] = True
                    self.map.visual[self.pos_x][self.pos_y] == "."

            elif self.map.visual[self.pos_x][self.pos_y] == "⛿":
                Event.trigger_event(PNJ(),"villager",self)
                self.pos_x = copy.deepcopy(position[0])
                self.pos_y = copy.deepcopy(position[1])
                can_move = False

            elif self.map.visual[self.pos_x][self.pos_y] == "฿":
                Event.trigger_event(PNJ(),"merchand",self)
                self.pos_x = copy.deepcopy(position[0])
                self.pos_y = copy.deepcopy(position[1])
                can_move = False

            elif [self.pos_x, self.pos_y] in self.map.house_position:
                self.pos_x = copy.deepcopy(position[0])
                self.pos_y = copy.deepcopy(position[1])
                print("Physical barrier in the direction you choose, turn around")
                break

            if can_move:
                self.map.hero_moving(self,position)

    

class Mage(Hero) : 
    def __init__(self, name):
        super().__init__(
            name=name,
            pv=100,
            defense=70,
            attack=50,
            stamina=50,
            dodge=0.5,
            agility=50,
            critical_rate=10,
            pos_x=0,
            pos_y=0,
        )
        self.mana = 150
        self.magic_attack = 80
        self.inventory = []
        self.skills = [
            Skill(
                name="Boule de feu",
                skill_type="magic",
                damage=60,
                cost=25,
                cooldown=1,
            ),
            Skill(
                name="Bouclier arcanique",
                skill_type="buff",
                damage=0,
                cost=20,
                cooldown=3,
                effect="defense_up",
                effect_duration=2,
            )
        ]
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
        print(f"Strenght       : {self.attack}")
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
            attack=50,
            stamina=50,
            dodge=0.8,
            agility=80,
            critical_rate=10,
            pos_x=0,
            pos_y=0
        )
        self.inventory = []
        self.skills = [
            Skill(
                name="Attaque sournoise",
                skill_type="physical",
                damage=50,
                cost=15,
                cooldown=1,
            ),
            Skill(
                name="Esquive parfaite",
                skill_type="buff",
                damage=0,
                cost=25,
                cooldown=4,
                effect="dodge_up",
                effect_duration=2,
            )
        ]        
        self.symbol = "𓀡"
        self.speed = 60
        self.statistics()



    
class Warrior(Hero) : 
   def __init__(self, name):

        super().__init__(
            name=name,
            pv=150,
            defense=80,
            attack=80,
            stamina=60,
            dodge=0.3,
            agility=50,
            critical_rate=15,
            pos_x=0,
            pos_y=0
        )
        self.inventory = []
        self.skills = [
            Skill(
                name="Coup puissant",
                skill_type="physical",
                damage=40,
                cost=20,
                cooldown=2,
            ),
            Skill(
                name="Charge héroïque",
                skill_type="buff",
                damage=0,
                cost=30,
                cooldown=3,
                effect="defense_up",
                effect_duration=2,
            )
        ]
        self.symbol = "𓀛"
        self.speed = 60
        self.statistics()

        
