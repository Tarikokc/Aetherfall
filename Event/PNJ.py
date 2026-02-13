import time

class PNJ:
    def merchand():
        print("shop")

    def triggered(*args):
        print(args[1][0])
        if args[1][0] == "villager":
            print("Villager :  Hi, Welcome,  i never see you here, where are you from ?\n")
            time.sleep(5)
            answer = input("1. Just arrive in town\n2. Not your business\n")
            if answer == "1":
                print("Villager :  Ooohhh Interesting ... Nice to meet you")
            elif answer == "2":
                print("Villager : What a sweet way to introduce yourself ...")
            else:
                print("Villager : Thank you for your clear answer, do you really understand our language ? ...")
            time.sleep(5)
            print("Villager : But whatever, By the way as a new citizen of a village and my lovely neighboor can you do a little favor for me with, you seem so strong ... ")
            answer = input("1. I don't really get the link but tell me \n2. Wtf are you talking about \n")
            print("Villager : There is some donjon behind a huge door in the dark forest, \nthe key of the door must be somewhere in the forest \ncould you go inside a get the golden chest in the last room")
            time.sleep(5)
            print(f"{args[1][1].name} : Why are you not going by yourself ?")
            time.sleep(5)
            print("I'm too old for this type of trip but don't worry it's not dangerous, you will be back in a few seconds... I will wait for you in the village,\ndon't open it")
            args[1][1].quest["start"] = False
            args[1][1].quest["pnj"] = True
            time.sleep(3)
            print("\n========================================== NEW QUEST UNLOCK : FOUND THE KEY ===============================================================================")
            time.sleep(3)

        elif args[1][0] == "merchand":
            print("Merchand :  Welcome kid, come on, take a look on my products !\n")
            PNJ.merchand()







