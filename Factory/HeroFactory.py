
from Entity.Character.Character import Character
from Entity.Character.Hero import Mage
from Entity.Character.Hero import Thief
from Entity.Character.Hero import Warrior

class HeroFactory:
    def create(hero_type, name):
        if hero_type == "Warrior" : 
            return Warrior(name)
        if hero_type ==  "Mage" : 
            return Mage(name)
        if hero_type == "Thief" :
            return Thief(name)
        # raise ValueError(f"hero_type de classe inconnu: {hero_type}")

    
 
        