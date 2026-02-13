from Entity.Enemy import Wolf
from Entity.Enemy import Bandit
from Entity.Enemy import Skeleton
from Entity.Enemy import CorruptChamp
from Entity.Enemy import Boss

  
class EnemyFactory:
    def create(Enemy_type, name=None):
        if Enemy_type == "Wolf":
            return Wolf(name) 
        if Enemy_type == "Bandit":
            return Bandit(name) 
        if Enemy_type == "Skeleton":
            return Skeleton(name) 
        if Enemy_type == "Corrupt Harroun":
            return CorruptChamp(name) 
        if Enemy_type == "Magellan":
            return Boss(name) 
        
        # raise ValueError(f"Type d'ennemi inconnu: {Enemy_type}")
