from Entity.Character import Character
from Entity.Enemy import Enemy
from Entity.Hero import Hero
import random

class Fight : 
    def __init__(self,hero,enemy):
        self.hero = hero
        self.enemy = enemy
        
    def attack_enemy(self,attacker,target) : 
        damage = max(0, attacker.attack - target.defense)
        critic = random.randint(1, 50)
        
        if critic : 
            damage *= 2
            print(f"Critic attack : {damage}")
        print(f"{attacker.name} attack {target.name} with {damage} damage ! ")

        target.pv -= damage
        print(f"{target.name} : {target.pv} PV")
        
        return target.pv <= 0
    
    def fight_enemy(self) : 
        
        
        while(self.hero.is_alive() and self.enemy.is_alive()) : 
            enemy_type = self.enemy.__class__.__name__
            print(f"\n  The fight against {enemy_type} and {self.enemy.name} begins!\n")

            print(f"{self.hero.name} : {self.hero.pv} PV")
            print(f"{enemy_type} : {self.enemy.pv} PV")
            
            print("")
            
            print(f"{self.hero.name} TURN !")
            enemyKO = self.attack_enemy(self.hero,self.enemy)
            if enemyKO : 
                print(f"Win !! The enemy {enemy_type} is DEAD")
                return True
            
            print(f"{self.enemy.name} TURN !")
            heroKO = self.attack_enemy(self.enemy,self.hero)
            if heroKO : 
                print(f"Lose !! The enemy {enemy_type} beat {self.name}")
                return False
            print("-" * 40 + "\n")

        return self.hero.is_alive()

            

            
    
    