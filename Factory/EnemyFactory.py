from Entity.Enemy import Wolf
from Entity.Enemy import Bandit
from Entity.Enemy import Skeleton
from Entity.Enemy import CorruptChamp
from Entity.Enemy import Boss

  
class EnemyFactory:

    ENNEMY_TYPE = ["Wolf","Bandit","Skeleton","Corrupt Harroun","Magellan"]

    def create(Enemy_type):
        if Enemy_type == "Wolf":
            return Wolf() 
        if Enemy_type == "Bandit":
            return Bandit() 
        if Enemy_type == "Skeleton":
            return Skeleton() 
        if Enemy_type == "Corrupt Harroun":
            return CorruptChamp() 
        if Enemy_type == "Magellan":
            return Boss() 
        
        # raise ValueError(f"Type d'ennemi inconnu: {Enemy_type}")
