import time
import random
from Environment.Map import Map
from Environment.Forest import Forest
from Environment.Village import Village
from Factory.HeroFactory import HeroFactory
from Factory.HeroFactory import HeroFactory
from Inventory.Item import start_equipment
from Inventory.Inventory import Inventory
from Battle.Fight import Fight
from Entity.Enemy import Wolf, Skeleton, Bandit
import msvcrt

def introduction():
    print("#####################################")
    print("#         RPG AETHERFALL            #")
    print("#####################################\n")
    print("1. Start game")
    print("2. Quitter\n")

    choix = input("Choose an option (1 ou 2) : ")

    if choix == "1":
        print("\nYou wake up in a small village lost and weak asf ...")
        time.sleep(2)
        hero = choose_class()
        return hero
    elif choix == "2":
        print("\nGoodbye hero !")
    else:
        print("\nInvalid Choice. Relaunch Game.")
        return introduction()

    input("\nClick on any keystroke to exit game...")

def choose_class():
    print("\nWhat's your name hero ? : ", end="")
    name = input()
    print(f"\n{name} ... Not bad")
    time.sleep(2)
    print("\nLet's continue.")
    time.sleep(2)

    print("\n========================================== AETHERFALL CLASS ===============================================================================")
    print("\n  [1] WARRIOR                                       [2] MAGE                                          [3] THIEF")
    print("    ─────────────                                     ─────────────                                     ─────────────")
    print("    Specialization: Melee combat and resilience       Specialization: Offensive magic and control.      Specialization: Speed and criticals")
    print("    High HP to withstand damage                       High intelligence for magical damage.             High agility and critical rate")
    print("    Strength and defense as main stats                Mana as optional resource.                        Endurance as optional resource")
    print("    Skills: Powerful Strike, Heroic Charge            Skills: Fireball, Arcane Shield                   Skills: Sneak Attack, Perfect Dodge\n")


    choice = input("Choose your future (1 for warrior, 2 for mage, 3 for rogue) : ")
    print()
    
    hero = None

    if choice == "1":
        print("    ➤ You choose class WARRIOR.")
        hero = HeroFactory.create("Warrior",name)
    elif choice == "2":
        print("    ➤ You choose class MAGE.")
        hero = HeroFactory.create("Mage",name)
    elif choice == "3":
        print("    ➤ You choose class THIEF.")
        hero = HeroFactory.create("Thief",name)
    else:
        print("Choix invalide. Aucune classe sélectionnée.")

    start_equipment(hero)
    
    print("\n" + "="*50)
    print("YOUR EQUIPMENT")
    print("="*50)
    for item in hero.equipment:
        print(f"  • {item}")  
    print("="*50)
    
    time.sleep(1)
    input("Press a keystroke to continue...")
    
    return hero  

# def check_inventory(hero) : 
#     key = input("")
#     if key == "i" : 
#         hero.inventory.display_item()
#         input("\n Press Enter to continue...")
#         return True
#     return False

# def game(hero) : 
#     hero.move(True)
    
#     check_inventory(hero)

def main_menu(hero):
    exit = False 
    while not exit:
        print("\n========================================== HERO MENU ==========================================")
        print("1. Check inventory")
        print("2. Exit")
        choix = input("")

        if choix == "1":
            hero.inventory.display_item()
        elif choix == "2":
            print("Goodbye Hero !")
            exit = True
        else:
            print("Invalid choice. Press a keystroke to continue......")

if __name__ == "__main__":
    # pass
    # hero1 = HeroFactory.create("Warrior","alyssa")
    # print (hero1)
    # f1  = Village()
    # while True:
    #     hero1.move(True,f1)
    hero = introduction()
    
    if hero:
        hero.move(True)
        
        
        
    
    # HeroFactory.create("Mage","alyssa")
    # HeroFactory.create("Thief","alyssa")



