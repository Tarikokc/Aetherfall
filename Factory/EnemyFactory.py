from Entity.Enemy import Wolf
from Entity.Enemy import Bandit
from Entity.Enemy import Skeleton
from Entity.Enemy import CorruptChamp
from Entity.Enemy import Boss

  
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
