import random
from Environment.Map import Map

class Village(Map):

    MAX_HOUSE = 15
    MAX_CHEST = 4
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.visual = []
            cls._instance.house_position = []
        return cls._instance
    
    def __init__(self):
        self.generate_map()
        self.display_map()


    def generate_map(self):

        if not self.visual:
            map_village = []
            for i in range (0,Map.MAX_WIDTH):
                map_village_line = []
                for j in range (0,Map.MAX_HEIGHT):
                    map_village_line.append(".")
                map_village.append(map_village_line)

            for i in range (0,Village.MAX_HOUSE):
                position_house = [random.randint(1,Map.MAX_WIDTH - 2),random.randint(1,Map.MAX_HEIGHT - 1)]
                print("position house")
                print(position_house)
                map_village[position_house[0]][position_house[1]] = "⌂"
                self.house_position.append([position_house[0],position_house[1]])
            for i in range (0,Village.MAX_CHEST):
                position_house = [random.randint(1,Map.MAX_WIDTH - 2),random.randint(1,Map.MAX_HEIGHT - 1)]
                print("position house")
                print(position_house)
                map_village[position_house[0]][position_house[1]] = "𖡧"
                self.house_position.append([position_house[0],position_house[1]])
            position_pnj = [random.randint(1,Map.MAX_WIDTH - 1),random.randint(1,Map.MAX_HEIGHT - 1)]
            while position_pnj in self.house_position:
                position_pnj = [random.randint(1,Map.MAX_WIDTH - 1),random.randint(1,Map.MAX_HEIGHT - 1)]
            map_village[position_pnj[0]][position_pnj[1]] = "⛿"
            self.house_position.append([position_pnj[0],position_pnj[1]])

            position_merchand = [random.randint(1,Map.MAX_WIDTH - 1),random.randint(1,Map.MAX_HEIGHT - 1)]
            while position_merchand in self.house_position:
                position_merchand = [random.randint(1,Map.MAX_WIDTH - 1),random.randint(1,Map.MAX_HEIGHT - 1)]
            map_village[position_merchand[0]][position_merchand[1]] = "฿"

            self.visual = map_village
    