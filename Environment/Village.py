import random
from Map import Map

#"𓇣"

class Village(Map):

    MAX_HOUSE = 15

    def generate_map(self):

        map_village = []
        for i in range (0,Map.MAX_WIDTH):
            map_village_line = []
            for j in range (0,Map.MAX_HEIGHT):
                map_village_line.append(".")
            map_village.append(map_village_line)

        for i in range (0,Village.MAX_HOUSE):
            map_village[random.randint(0,Map.MAX_WIDTH - 1)][random.randint(0,Map.MAX_HEIGHT - 1)] = "⌂"
        self.visual = map_village
    
village = Village()
village.display_map()