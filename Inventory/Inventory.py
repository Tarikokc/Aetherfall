import time
class Inventory:
    def __init__(self) : 
        self.equipment = []
        self.items = []
        self.gold = 100
    
    def add_item(self,item) : 
        self.items.append(item)  
    
    def add_equipment(self,item) : 
        self.equipment.append(item)
    

    def display_item(self):
        """Affiche l'inventaire"""
        print("\n" + "="*50)
        print("🎒 INVENTORY")
        print("="*50)
        print(f"💰 Gold: {self.gold}")
        print("\nEquipment:")
        for item in self.equipment:
            print(f"  • {item}")
        print("\n🧪 Items:")
        for item in self.items:
            print(f"  • {item}")
        print("="*50)
        time.sleep(3)
    