
class Map:

    MAX_WIDTH = 10
    MAX_HEIGHT = 20

    def __init__(self):
        self.visual = []

    def generate_map(self):
        pass

    def hero_moving(self,hero,previous_position):
        if not previous_position[1] == Map.MAX_HEIGHT or previous_position[0] == Map.MAX_WIDTH:
            self.visual[previous_position[0]][previous_position[1]] = "."
        self.visual[hero.pos_x][hero.pos_y] = hero.symbol

    def display_map(self):
        for road in self.visual:
           print(" ".join(road))

