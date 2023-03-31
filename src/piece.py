class Piece:
    def __init__(self, piece_id, team, window):
        self.piece_id = piece_id
        self.team = team
        self.is_alive = True
        self.occupied_tile = None
        self.image = None
        self.x = None
        self.y = None
        self.image_option1 = None
        self.image_option2 = None
        self.window = window

    def pick_image(self):
        if self.team == 1:
            self.image = self.image_option1
        elif self.team == 2:
            self.image = self.image_option2

    def draw(self):
        # Check if piece has been removed from the board
        if self.occupied_tile is None:
            return None

        self.window.blit(self.image, (self.x, self.y))

    def occupy_tile(self, tile):
        tile.occupy(self, self.team)
        self.occupied_tile = tile
        self.x = tile.x
        self.y = tile.y

    def unoccupy_tile(self):
        self.occupied_tile.unoccupy()
        self.occupied_tile = None
        self.x = None
        self.y = None