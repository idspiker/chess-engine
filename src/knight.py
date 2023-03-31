from piece import Piece
from images import LIGHT_KNIGHT_IMAGE, DARK_KNIGHT_IMAGE


class Knight(Piece):
    def __init__(self, piece_id, team, window, initial_tile):
        super().__init__(piece_id, team, window)

        self.image_option1 = LIGHT_KNIGHT_IMAGE
        self.image_option2 = DARK_KNIGHT_IMAGE
        
        self.pick_image()

        self.occupy_tile(initial_tile)

    def get_moves(self, board):
        # Check if piece has been removed from the board
        if self.occupied_tile is None:
            return []

        possible_moves = []

        # Store initial tile options in frontier
        frontier = [
            self.occupied_tile.tile_above,
            self.occupied_tile.tile_right,
            self.occupied_tile.tile_below,
            self.occupied_tile.tile_left,
        ]

        # Iterate through the frontier, setting the values to the next 
        # tile in the path
        for index, value in enumerate(frontier):
            if value is None:
                continue
            
            if index == 0:
                frontier[index] = board.tiles[value].tile_above
            elif index == 1: 
                frontier[index] = board.tiles[value].tile_right
            elif index == 2:
                frontier[index] = board.tiles[value].tile_below
            elif index == 3:
                frontier[index] = board.tiles[value].tile_left

        # Go over the tiles again, setting each element to a tuple of 
        # its branch tiles
        for index, value in enumerate(frontier):
            if value is None:
                continue

            # If tile above or below origin
            if index % 2 == 0:
                frontier[index] = (
                    board.tiles[value].tile_left,
                    board.tiles[value].tile_right
                )
            # If tile to the right or left of origin
            else:
                frontier[index] = (
                    board.tiles[value].tile_above,
                    board.tiles[value].tile_below
                )

        # Iterate all tuples in the frontier, testing both tiles in each
        # to see if they are valid moves
        for index, value in enumerate(frontier):
            if value is None:
                continue

            for tile_num in value:
                if tile_num is None:
                    continue

                # Tile object to test
                tile = board.tiles[tile_num]

                if tile.occupied == False or tile.occupant_team != self.team:
                    possible_moves.append(tile_num)

        return possible_moves
