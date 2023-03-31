from piece import Piece
from images import LIGHT_KING_IMAGE, DARK_KING_IMAGE


class King(Piece):
    def __init__(self, piece_id, team, window, initial_tile):
        super().__init__(piece_id, team, window)

        self.image_option1 = LIGHT_KING_IMAGE
        self.image_option2 = DARK_KING_IMAGE

        self.pick_image()

        self.occupy_tile(initial_tile)

    def get_moves(self, board):
        # Check if piece has been removed from the board
        if self.occupied_tile is None:
            return []

        return []