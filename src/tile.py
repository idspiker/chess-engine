from images import TILE_OVERLAY_IMAGE, SELECTED_TILE_OVERLAY_IMAGE, NO_MOVE_TILE_OVERLAY_IMAGE, LIGHT_TILE_IMAGE, DARK_TILE_IMAGE
from specs import TILE_SIZE


class Tile:
    def __init__(self, tile_id, grid_x, grid_y, window):
        self.tile_id = tile_id
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.x = (grid_x * TILE_SIZE) + TILE_SIZE
        self.y = (grid_y * TILE_SIZE) + TILE_SIZE
        self.image = None
        self.window = window

        self.highlight_images = (
            TILE_OVERLAY_IMAGE, 
            SELECTED_TILE_OVERLAY_IMAGE, 
            NO_MOVE_TILE_OVERLAY_IMAGE
        )

        self.highlighted = False
        self.highlighted_color = 0
        self.occupied = False
        self.occupant = None
        self.occupant_team = None
        self.tile_above = None
        self.tile_below = None
        self.tile_right = None
        self.tile_left = None
        self.tile_above_right = None
        self.tile_above_left = None
        self.tile_below_right = None
        self.tile_below_left = None

        self.identify_surrounding_tiles()
        self.pick_tile_asset()

    def identify_surrounding_tiles(self):
        on_top_border = False
        on_bottom_border = False
        on_right_border = False
        on_left_border = False

        # Test for left border
        if self.tile_id % 8 == 0:
            on_left_border = True
        # Test for right border
        elif (self.tile_id - 7) % 8 == 0:
            on_right_border = True

        # Test for top border
        if 0 <= self.tile_id <= 7:
            on_top_border = True
        # Test for bottom border
        elif 56 <= self.tile_id <= 63:
            on_bottom_border = True

        # Find surrounding tiles that exist
        # If on the bottom border
        if on_bottom_border == True:
            self.tile_above = self.tile_id - 8

            if on_right_border == False:
                self.tile_right = self.tile_id + 1
                self.tile_above_right = self.tile_id - 7

            if on_left_border == False:
                self.tile_left = self.tile_id - 1
                self.tile_above_left = self.tile_id - 9

        # If on the top border
        elif on_top_border == True:
            self.tile_below = self.tile_id + 8

            if on_right_border == False:
                self.tile_right = self.tile_id + 1
                self.tile_below_right = self.tile_id + 9

            if on_left_border == False:
                self.tile_left = self.tile_id - 1
                self.tile_below_left = self.tile_id + 7
                
        # If on a top or bottom border
        else:
            self.tile_above = self.tile_id - 8
            self.tile_below = self.tile_id + 8

            if on_right_border == False:
                self.tile_right = self.tile_id + 1
                self.tile_above_right = self.tile_id - 7
                self.tile_below_right = self.tile_id + 9

            if on_left_border == False:
                self.tile_left = self.tile_id - 1
                self.tile_above_left = self.tile_id - 9
                self.tile_below_left = self.tile_id + 7

    def pick_tile_asset(self):
        if (self.tile_id - self.grid_y) % 2 == 0:
            self.image = 0
        else:
            self.image = 1

    def draw(self):
        if self.image == 0:
            self.window.blit(LIGHT_TILE_IMAGE, (self.x, self.y))
        elif self.image == 1:
            self.window.blit(DARK_TILE_IMAGE, (self.x, self.y))

        if self.highlighted == True:
            self.window.blit(
                self.highlight_images[self.highlighted_color], (self.x, self.y)
            )

    def highlight_tile(self, color):
        self.highlighted = True
        self.highlighted_color = color

    def unhighlight_tile(self):
        self.highlighted = False
        self.highlighted_color = 0

    def occupy(self, piece, team):
        if self.occupant is not None:
            self.occupant.unoccupy_tile()

        self.occupant = piece
        self.occupant_team = team
        self.occupied = True

    def unoccupy(self):
        self.occupant = None
        self.occupant_team = None
        self.occupied = False
