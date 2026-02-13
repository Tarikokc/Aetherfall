import random
import time
from Battle.Skill import Skill
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
    
    # def fight_enemy(self) : 
    #     is_hero_turn = True
    #     while(self.hero.is_alive() and self.enemy.is_alive()) : 
    #         is_turn_hero = False
    #         enemy_type = self.enemy.__class__.__name__
    #         print(f"\nThe fight against {enemy_type} and {self.hero.name} begins!\n")
    #         time.sleep(2)
    #         print(f"{self.hero.name} : {self.hero.pv} PV")
    #         print(f"{enemy_type} : {self.enemy.pv} PV")
    #         time.sleep(2)
    #         print("")
            
    #         if is_turn_hero : 
    #             print(f"{self.hero.name} TURN !")
    #             time.sleep(2)
    #             enemyKO = self.attack_enemy(self.hero,self.enemy)
    #             if enemyKO : 
    #                 print(f"Win !! The enemy {enemy_type} is DEAD")
    #                 time.sleep(2)
    #                 return True
    #         else : 
    #             print(f"{self.enemy.name} TURN !")
    #             time.sleep(2)
    #             heroKO = self.attack_enemy(self.enemy,self.hero)
    #             if heroKO : 
    #                 print(f"Lose !! The enemy {enemy_type} beat {self.name}")
    #                 time.sleep(2)
    #                 return False
    #             print("-" * 40 + "\n")   
    #     return self.hero.is_alive()
    def fight_enemy(self):
        """Combat avec alternance de tours et choix de skills"""
        is_hero_turn = True  
        enemy_type = self.enemy.__class__.__name__
        
        print(f"\n{'='*50}")
        print(f"⚔️  {self.hero.name} VS {enemy_type}")
        print(f"{'='*50}\n")
        time.sleep(1)
        
        while self.hero.is_alive() and self.enemy.is_alive():
            print(f"{self.hero.name}: {self.hero.pv} PV")
            print(f"{enemy_type}: {self.enemy.pv} PV")
            time.sleep(1)
            print("")
            
            if is_hero_turn:
                print(f"{self.hero.name} TURN!")
                time.sleep(1)
                
                action = input("Attack (a) or Skill (s)? ").lower().strip()
                
                if action == "s":
                    skill_used = self.use_skill_menu()
                    if not skill_used:
                        enemyKO = self.attack_enemy(self.hero, self.enemy)
                    else:
                        enemyKO = not self.enemy.is_alive()
                else:
                    enemyKO = self.attack_enemy(self.hero, self.enemy)
                
                if enemyKO:
                    print(f"\nWin! The enemy {enemy_type} is DEAD")
                    time.sleep(2)
                    return True
            
            else:
                print(f"{enemy_type} TURN!")
                time.sleep(1)
                
                heroKO = self.attack_enemy(self.enemy, self.hero)
                
                if heroKO:
                    print(f"\n💀 Lose! The enemy {enemy_type} beat {self.hero.name}")
                    time.sleep(2)
                    return False
            
            print("-" * 40 + "\n")
            
            is_hero_turn = not is_hero_turn
            time.sleep(1)
        
        return self.hero.is_alive()
    def use_skill_menu(self):
    
        if not hasattr(self.hero, 'skills') or not self.hero.skills:
            print("No skills available!")
            return False
        
        print("\nAVAILABLE SKILLS:")
        for i, skill in enumerate(self.hero.skills, 1):
            print(f"  {i}. {skill.name} (Cost: {skill.cost} stamina)")
        print("  0. Cancel")
        
        try:
            choice = int(input("\nChoose skill number: "))
            
            if choice == 0:
                print("Cancelled!")
                return False
            
            if 1 <= choice <= len(self.hero.skills):
                skill = self.hero.skills[choice - 1]
                
                if self.hero.stamina < skill.cost:
                    print(f"Not enough stamina! (Need {skill.cost}, have {self.hero.stamina})")
                    return False
                
                print(f"\n✨ {self.hero.name} uses {skill.name}!")
                time.sleep(1)
                
                success = skill.use_skill(self.hero, self.enemy)
                
                if success:
                    return True
                else:
                    print("Skill failed!")
                    return False
            else:
                print("Invalid choice!")
                return False
        
        except ValueError:
            print("Invalid input!")
            return False


    def ask_action(self) : 
        print("\n Your Action : ")
        print("1- Attack")
        print("2- Skill")
        
        choice = input()
        if choice == 2 : 
            return "skill"
        else : 
            return "attack"
        
    
            

            
    
    