import random
from Environment.Map import Map


class Forest(Map):

    MAX_TREE = 20
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.visual = []
        return cls._instance
    
    def __init__(self):
        self.generate_map()
        self.display_map()

    def generate_map(self):

        if not self.visual:
            map_forest = []
            for i in range (0,Map.MAX_WIDTH):
                map_forest_line = []
                for j in range (0,Map.MAX_HEIGHT):
                    map_forest_line.append(".")
                map_forest.append(map_forest_line)

            for i in range (0,Forest.MAX_TREE):
                map_forest[random.randint(0,Map.MAX_WIDTH - 1)][random.randint(0,Map.MAX_HEIGHT - 1)] = "𖢔"
            self.visual = map_forest
    
f1  = Forest()
print ("")
f2 = Forest()
