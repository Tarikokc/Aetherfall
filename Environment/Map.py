class Map:

    MAX_WIDTH = 10
    MAX_HEIGHT = 20

    def __init__(self):
        self.visual = []
        self.generate_map()

    def generate_map(self):
        pass

    def display_map(self):
        for road in self.visual:
           print(" ".join(road))
