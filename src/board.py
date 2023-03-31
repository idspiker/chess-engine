from tile import Tile


class Board:
    def __init__(self, window):
        self.tiles = []
        self.active_player = 1
        self.window = window

        self.load_tiles()
    
    def load_tiles(self):
        x = 0
        y = 0
        for i in range(64):
            self.tiles.append(Tile(i, x, y, self.window))
            if x == 7:
                x = 0
                y += 1
            else:
                x += 1