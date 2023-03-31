from piece import Piece
from images import LIGHT_ROOK_IMAGE, DARK_ROOK_IMAGE

class Rook(Piece):
    def __init__(self, piece_id, team, window, initial_tile):
        super().__init__(piece_id, team, window)

        self.image_option1 = LIGHT_ROOK_IMAGE
        self.image_option2 = DARK_ROOK_IMAGE
        
        self.pick_image()

        self.occupy_tile(initial_tile)

    def get_moves(self, board):
        # Check if piece has been removed from the board
        if self.occupied_tile is None:
            return []

        possible_moves = []

        frontier = [
            self.occupied_tile.tile_above,
            self.occupied_tile.tile_right,
            self.occupied_tile.tile_below,
            self.occupied_tile.tile_left,
        ]

        found_moves = 1
        while found_moves != 0:
            found_moves = 0

            for index, value in enumerate(frontier):
                if value is None:
                    continue
                # Handle if the tile is occupied
                elif board.tiles[value].occupied == True:
                    # Handle if the occupant is not a teammate
                    if board.tiles[value].occupant_team != self.team:
                        possible_moves.append(value)
                        found_moves += 1
                        
                    frontier[index] = None
                    continue

                possible_moves.append(value)
                found_moves += 1

                # Set tile to the next tile
                if index == 0:
                    frontier[index] = board.tiles[value].tile_above
                elif index == 1: 
                    frontier[index] = board.tiles[value].tile_right
                elif index == 2:
                    frontier[index] = board.tiles[value].tile_below
                elif index == 3:
                    frontier[index] = board.tiles[value].tile_left

        return possible_moves
