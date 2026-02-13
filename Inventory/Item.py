import json
class Item:
    with open("items_data.json", 'r', encoding='utf-8') as f:
        _items_data= json.load(f)
        
    def __init__(self, name,data):
        self.name = name
        self.type = data["type"]
        self.description = data["description"]
        
        if "stat_bonus" in data:
            self.stat_bonus = data["stat_bonus"]
        
        if "effect" in data:
            self.effect = data["effect"]
            self.value = data["value"]  
            self.quantity = 1 
            
    def __str__(self): 
        if hasattr(self, 'quantity'):
            return f"{self.name} x{self.quantity}"
        return self.name    
    
    @classmethod
    def create_item(classe,category,name,quantity=1) : 
        data = classe._items_data[category][name]
        item = Item(name,data)
        
        return item
    
STARTING_EQUIPMENT = {
    "Warrior": {
        "weapon": "Épée de Fer",
        "consumables": [
            ("Potion", 3),
            ("Élixir", 2)
        ]
    },
    "Mage": {
        "weapon": "Bâton de Bois",
        "consumables": [
            ("Potion", 2),
            ("Potion de Mana", 3)
        ]
    },
    "Thief": {
        "weapon": "Dague Rouillée",
        "consumables": [
            ("Potion", 2),
            ("Fiole de Poison", 2)
        ]
    }
}

def start_equipment(hero) : 
    class_name = hero.__class__.__name__
    
    
    equipement = STARTING_EQUIPMENT.get(class_name)
    
    weapon = Item.create_item("weapons", equipement["weapon"])
    hero.equip_item(weapon)
    
    for item_name , quantity in equipement["consumables"] : 
        item = Item.create_item("consumables", item_name, quantity)
        hero.equipement.append(item)
        print(f"{item} added to inventory")    