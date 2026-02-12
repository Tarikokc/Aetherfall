import random
from Map import Map


class Forest(Map):

    MAX_TREE = 20

    def generate_map(self):

        map_forest = []
        for i in range (0,Map.MAX_WIDTH):
            map_forest_line = []
            for j in range (0,Map.MAX_HEIGHT):
                map_forest_line.append(".")
            map_forest.append(map_forest_line)

        for i in range (0,Forest.MAX_TREE):
            map_forest[random.randint(0,Map.MAX_WIDTH - 1)][random.randint(0,Map.MAX_HEIGHT - 1)] = "𖢔"
        self.visual = map_forest
    
forest = Forest()
forest.display_map()