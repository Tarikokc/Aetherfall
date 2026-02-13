import random
from Environment.Map import Map

class Key:
    
    def triggered(*args):
        position_key = [random.randint(1,Map.MAX_WIDTH - 1),random.randint(1,Map.MAX_HEIGHT - 1)]
        while position_key in args[1][0].house_position:
            position_key = [random.randint(1,Map.MAX_WIDTH - 1),random.randint(1,Map.MAX_HEIGHT - 1)]
        args[1][0].visual[position_key[0]][position_key[1]] = "𖤝"
        args[1][0].house_position.append([position_key[0],position_key[1]])
        
        