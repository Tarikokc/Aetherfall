from Entity.Character.Enemy import Wolf
from Entity.Character.Enemy import Bandit
from Entity.Character.Enemy import Skeleton
from Entity.Character.Enemy import CorruptChamp
from Entity.Character.Enemy import Boss

  
class EnnemyFactory:
    def create(ennemy_type, name=None):
        if ennemy_type == "Wolf":
            return Wolf(name) 
        if ennemy_type == "Bandit":
            return Bandit(name) 
        if ennemy_type == "Skeleton":
            return Skeleton(name) 
        if ennemy_type == "Corrupt Harroun":
            return CorruptChamp(name) 
        if ennemy_type == "Magellan":
            return Boss(name) 
        
        # raise ValueError(f"Type d'ennemi inconnu: {ennemy_type}")
