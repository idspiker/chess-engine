from piece import Piece
from images import LIGHT_PAWN_IMAGE, DARK_PAWN_IMAGE

class Pawn(Piece):
    def __init__(self, piece_id, team, window, initial_tile):
        super().__init__(piece_id, team, window)

        self.not_moved = True
        self.image_option1 = LIGHT_PAWN_IMAGE
        self.image_option2 = DARK_PAWN_IMAGE
        
        self.pick_image()

        self.occupy_tile(initial_tile)

    def get_moves(self, board):
        # Check if piece has been removed from the board
        if self.occupied_tile is None:
            return []
        
        possible_moves = []

        # If on light team
        if self.team == 1:
            # Handle if on the screen edge
            if self.occupied_tile.tile_above is None:
                return possible_moves

            if board.tiles[self.occupied_tile.tile_above].occupied == False:
                next_tile = self.occupied_tile.tile_above
                possible_moves.append(next_tile)

                if (self.not_moved == True
                    and board.tiles[board.tiles[next_tile].tile_above]
                    .occupied == False):
                    # Add 2nd tile if on pawn's first move
                    possible_moves.append(board.tiles[next_tile].tile_above)

            if (self.occupied_tile.tile_above_right is not None
                and board.tiles[self.occupied_tile.tile_above_right]
                .occupant_team == 2):
                # Add if there is an opponent to attack
                possible_moves.append(self.occupied_tile.tile_above_right)

            if (self.occupied_tile.tile_above_left is not None
                and board.tiles[self.occupied_tile.tile_above_left]
                .occupant_team == 2):
                # Add if there is an opponent to attack
                possible_moves.append(self.occupied_tile.tile_above_left)

        # If on dark team
        elif self.team == 2:
            # Handle if on the screen edge
            if self.occupied_tile.tile_below is None:
                return possible_moves

            if board.tiles[self.occupied_tile.tile_below].occupied == False:
                next_tile = self.occupied_tile.tile_below
                possible_moves.append(next_tile)

                if (self.not_moved == True
                    and board.tiles[board.tiles[next_tile].tile_below]
                    .occupied == False):
                    # Add 2nd tile if on pawn's first move
                    possible_moves.append(board.tiles[next_tile].tile_below)

            if (self.occupied_tile.tile_below_right is not None
                and board.tiles[self.occupied_tile.tile_below_right]
                .occupant_team == 1):
                # Add if there is an opponent to attack
                possible_moves.append(self.occupied_tile.tile_below_right)

            if (self.occupied_tile.tile_below_left is not None
                and board.tiles[self.occupied_tile.tile_below_left]
                .occupant_team == 1):
                # Add if there is an opponent to attack
                possible_moves.append(self.occupied_tile.tile_below_left)

        return possible_moves

    def unoccupy_tile(self):
        self.occupied_tile.unoccupy()
        self.occupied_tile = None

        # Indicate that piece has been moved from its origin
        self.not_moved = False
