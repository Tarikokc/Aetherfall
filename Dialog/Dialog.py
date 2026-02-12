import time

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
        choose_class()
    elif choix == "2":
        print("\nGoodbye hero !")
    else:
        print("\nInvalid Choice. Relaunch Game.")

    input("\nClick on any keystroke to exit game...")

def choose_class():
    print("\nWhat's your name hero ? : ", end="")
    name_aventurier = input()
    print(f"\n{name_aventurier} ... Not bad")
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

    if choice == "1":
        print("    ➤ You choose class WARRIOR.")
    elif choice == "2":
        print("    ➤ You choose class MAGE.")
    elif choice == "3":
        print("    ➤ You choose class THIEF.")
    else:
        print("    Choix invalide. Aucune classe sélectionnée.")

    input("Press a keystroke to continue...")
    main_menu()

def main_menu():
    exit = False

    while not exit:
        print("\n========================================== MENU AVENTURIER ==========================================")
        print("1. Check inventory")
        print("2. Exit")
        choix = input("")

        if choix == "1":
            print("Inventory : [empty]")
        elif choix == "2":
            print("Goodbye Hero !")
            exit = True
        else:
            print("Invalid choice. Press a keystroke to continue......")

if __name__ == "__main__":
     introduction()
