import pygame


from specs import TILE_SIZE
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King


class Player:
    def __init__(self, player_id, rival_id, board, window):
        self.player_id = player_id
        self.rival_id = rival_id
        self.player_pieces = []
        self.board = board
        self.focused_piece = None
        self.available_moves = {}
        self.window = window

        self.setup_pawns()
        self.setup_rooks()
        self.setup_knights()
        self.setup_bishops()
        self.setup_royal_pieces()

    def setup_pawns(self):
        piece_id = 0
        initial_tile = None

        # Set beginning tile based on team
        if self.player_id == 1:
            initial_tile = 48
        elif self.player_id == 2:
            initial_tile = 8

        # Place all pawns
        while piece_id < 8:
            self.player_pieces.append(
                Pawn(piece_id, self.player_id, self.window, self.board.tiles[initial_tile])
            )
            piece_id += 1
            initial_tile += 1

    def setup_rooks(self):
        initial_tile = None

        if self.player_id == 1:
            initial_tile = 56
        elif self.player_id == 2:
            initial_tile = 0

        self.player_pieces.append(
            Rook(8, self.player_id, self.window, self.board.tiles[initial_tile])
        )
        self.player_pieces.append(
            Rook(9, self.player_id, self.window, self.board.tiles[initial_tile + 7])
        )

    def setup_knights(self):
        initial_tile = None
        
        if self.player_id == 1:
            initial_tile = 57
        elif self.player_id == 2:
            initial_tile = 1

        self.player_pieces.append(
            Knight(10, self.player_id, self.window, self.board.tiles[initial_tile])
        )
        self.player_pieces.append(
            Knight(11, self.player_id, self.window, self.board.tiles[initial_tile + 5])
        )

    def setup_bishops(self):
        initial_tile = None

        if self.player_id == 1:
            initial_tile = 58
        elif self.player_id == 2:
            initial_tile = 2

        self.player_pieces.append(
            Bishop(12, self.player_id, self.window, self.board.tiles[initial_tile])
        )
        self.player_pieces.append(
            Bishop(13, self.player_id, self.window, self.board.tiles[initial_tile + 3])
        )

    def setup_royal_pieces(self):
        initial_tile = None

        if self.player_id == 1:
            initial_tile = 59
        elif self.player_id == 2:
            initial_tile = 3

        self.player_pieces.append(
            Queen(14, self.player_id, self.window, self.board.tiles[initial_tile])
        )
        self.player_pieces.append(
            King(15, self.player_id, self.window, self.board.tiles[initial_tile + 1])
        )

    def get_available_moves(self):
        for i in range(len(self.player_pieces)):
            self.available_moves[i] = self.player_pieces[i].get_moves(
                self.board
            )

    def get_piece_moves(self, piece):
        # Unhighlight all tiles before highlighting piece's possible 
        # moves
        for tile in self.board.tiles:
            tile.unhighlight_tile()

        # Check if piece has been removed from the board
        if piece.occupied_tile is None:
            return False

        # Check for collision with piece and mouse
        if pygame.Rect(piece.x, piece.y, TILE_SIZE, TILE_SIZE
                       ).collidepoint(pygame.mouse.get_pos()):
            self.focused_piece = piece
            moves = self.available_moves[piece.piece_id]
            if moves == []:
                piece.occupied_tile.highlight_tile(2)
            else:
                piece.occupied_tile.highlight_tile(1)
                for tile in moves:
                    self.board.tiles[tile].highlight_tile(0)

            return True
        
        return False

    def move_piece(self, tile):
        if self.focused_piece is None:
            return False
        
        # Check for collision between mouse and tile
        if pygame.Rect(tile.x, tile.y, TILE_SIZE, TILE_SIZE
                       ).collidepoint(pygame.mouse.get_pos()):
            # Check if the clicked tile is in the focused pieces
            # available moves
            piece_num = self.focused_piece.piece_id

            if tile.tile_id in self.available_moves[piece_num]:

                self.focused_piece.unoccupy_tile()
                self.focused_piece.occupy_tile(tile)
                
                self.focused_piece = None

                self.board.active_player = self.rival_id

                return True

        return False
            