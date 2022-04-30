import pygame
import os

DRAW_SCALE = 5
TILE_SIZE = 16 * DRAW_SCALE

WIDTH, HEIGHT = (TILE_SIZE * 10), (TILE_SIZE * 10)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Engine')

FPS = 60

DARK_TILE_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'ChessTileDark.png')),
    (TILE_SIZE, TILE_SIZE)
)
LIGHT_TILE_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'ChessTileLight.png')),
    (TILE_SIZE, TILE_SIZE)
)
TILE_OVERLAY_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'ChessTileOverlay.png')),
    (TILE_SIZE, TILE_SIZE)
)
SELECTED_TILE_OVERLAY_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'ChessTileOverlaySelected.png')),
    (TILE_SIZE, TILE_SIZE)
)
NO_MOVE_TILE_OVERLAY_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'ChessTileOverlayNoMove.png')),
    (TILE_SIZE, TILE_SIZE)
)
DARK_PAWN_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'DarkPawn.png')),
    (TILE_SIZE, TILE_SIZE)
)
LIGHT_PAWN_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'LightPawn.png')),
    (TILE_SIZE, TILE_SIZE)
)
DARK_ROOK_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'DarkRook.png')),
    (TILE_SIZE, TILE_SIZE)
)
LIGHT_ROOK_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'LightRook.png')),
    (TILE_SIZE, TILE_SIZE)
)
DARK_KNIGHT_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'DarkKnight.png')),
    (TILE_SIZE, TILE_SIZE)
)
LIGHT_KNIGHT_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'LightKnight.png')),
    (TILE_SIZE, TILE_SIZE)
)
DARK_BISHOP_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'DarkBishop.png')),
    (TILE_SIZE, TILE_SIZE)
)
LIGHT_BISHOP_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'LightBishop.png')),
    (TILE_SIZE, TILE_SIZE)
)
DARK_QUEEN_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'DarkQueen.png')),
    (TILE_SIZE, TILE_SIZE)
)
LIGHT_QUEEN_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'LightQueen.png')),
    (TILE_SIZE, TILE_SIZE)
)
DARK_KING_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'DarkKing.png')),
    (TILE_SIZE, TILE_SIZE)
)
LIGHT_KING_IMAGE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'LightKing.png')),
    (TILE_SIZE, TILE_SIZE)
)

TURNS = 0

# TODO TODO TODO TODO TODO
# BROKEN:
# Fix pieces moving when not selected

# IMPLEMENT:
# Castling
# King movement
# Checkmate


def main():
    board = Board()

    # Create players
    p1 = Player(1, 2, board)
    p2 = Player(2, 1, board)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # Test
        p1.get_available_moves()
        p2.get_available_moves()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if board.active_player == 1:
                    for piece in p1.player_pieces:
                        piece_selected = p1.get_piece_moves(piece)
                        if piece_selected == True:
                            break
                    
                    for tile in board.tiles:
                        piece_moved = p1.move_piece(tile)
                        if piece_moved == True:
                            break
                            
                elif board.active_player == 2:
                    for piece in p2.player_pieces:
                        piece_selected = p2.get_piece_moves(piece)
                        if piece_selected == True:
                            break

                    for tile in board.tiles:
                        piece_moved = p2.move_piece(tile)
                        if piece_moved == True:
                            break
        
        for tile in board.tiles:
            tile.draw()

        for piece in p1.player_pieces:
            piece.draw()

        for piece in p2.player_pieces:
            piece.draw()

        pygame.display.update()

    pygame.quit()


class Player:
    def __init__(self, player_id, rival_id, board):
        self.player_id = player_id
        self.rival_id = rival_id
        self.player_pieces = []
        self.board = board
        self.focused_piece = None
        self.available_moves = {}

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
                Pawn(piece_id, self.player_id, self.board.tiles[initial_tile])
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
            Rook(8, self.player_id, self.board.tiles[initial_tile])
        )
        self.player_pieces.append(
            Rook(9, self.player_id, self.board.tiles[initial_tile + 7])
        )

    def setup_knights(self):
        initial_tile = None
        
        if self.player_id == 1:
            initial_tile = 57
        elif self.player_id == 2:
            initial_tile = 1

        self.player_pieces.append(
            Knight(10, self.player_id, self.board.tiles[initial_tile])
        )
        self.player_pieces.append(
            Knight(11, self.player_id, self.board.tiles[initial_tile + 5])
        )

    def setup_bishops(self):
        initial_tile = None

        if self.player_id == 1:
            initial_tile = 58
        elif self.player_id == 2:
            initial_tile = 2

        self.player_pieces.append(
            Bishop(12, self.player_id, self.board.tiles[initial_tile])
        )
        self.player_pieces.append(
            Bishop(13, self.player_id, self.board.tiles[initial_tile + 3])
        )

    def setup_royal_pieces(self):
        initial_tile = None

        if self.player_id == 1:
            initial_tile = 59
        elif self.player_id == 2:
            initial_tile = 3

        self.player_pieces.append(
            Queen(14, self.player_id, self.board.tiles[initial_tile])
        )
        self.player_pieces.append(
            King(15, self.player_id, self.board.tiles[initial_tile + 1])
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
            

class Board:
    def __init__(self):
        self.tiles = []
        self.active_player = 1

        self.load_tiles()
    
    def load_tiles(self):
        x = 0
        y = 0
        for i in range(64):
            self.tiles.append(Tile(i, x, y))
            if x == 7:
                x = 0
                y += 1
            else:
                x += 1


class Tile:
    def __init__(self, tile_id, grid_x, grid_y):
        self.tile_id = tile_id
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.x = (grid_x * TILE_SIZE) + TILE_SIZE
        self.y = (grid_y * TILE_SIZE) + TILE_SIZE
        self.image = None

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
            WIN.blit(LIGHT_TILE_IMAGE, (self.x, self.y))
        elif self.image == 1:
            WIN.blit(DARK_TILE_IMAGE, (self.x, self.y))

        if self.highlighted == True:
            WIN.blit(
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


class Piece:
    def __init__(self, piece_id, team):
        self.piece_id = piece_id
        self.team = team
        self.is_alive = True
        self.occupied_tile = None
        self.image = None
        self.x = None
        self.y = None
        self.image_option1 = None
        self.image_option2 = None

    def pick_image(self):
        if self.team == 1:
            self.image = self.image_option1
        elif self.team == 2:
            self.image = self.image_option2

    def draw(self):
        # Check if piece has been removed from the board
        if self.occupied_tile is None:
            return None

        WIN.blit(self.image, (self.x, self.y))

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


class Pawn(Piece):
    def __init__(self, piece_id, team, initial_tile):
        super().__init__(piece_id, team)

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


class Rook(Piece):
    def __init__(self, piece_id, team, initial_tile):
        super().__init__(piece_id, team)

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


class Knight(Piece):
    def __init__(self, piece_id, team, initial_tile):
        super().__init__(piece_id, team)

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


class Bishop(Piece):
    def __init__(self, piece_id, team, initial_tile):
        super().__init__(piece_id, team)

        self.image_option1 = LIGHT_BISHOP_IMAGE
        self.image_option2 = DARK_BISHOP_IMAGE
        
        self.pick_image()

        self.occupy_tile(initial_tile)

    def get_moves(self, board):
        # Check if piece has been removed from the board
        if self.occupied_tile is None:
            return []

        possible_moves = []

        frontier = [
            self.occupied_tile.tile_above_left,
            self.occupied_tile.tile_above_right,
            self.occupied_tile.tile_below_right,
            self.occupied_tile.tile_below_left,
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
                    frontier[index] = board.tiles[value].tile_above_left
                elif index == 1: 
                    frontier[index] = board.tiles[value].tile_above_right
                elif index == 2:
                    frontier[index] = board.tiles[value].tile_below_right
                elif index == 3:
                    frontier[index] = board.tiles[value].tile_below_left

        return possible_moves


class Queen(Piece):
    def __init__(self, piece_id, team, initial_tile):
        super().__init__(piece_id, team)

        self.image_option1 = LIGHT_QUEEN_IMAGE
        self.image_option2 = DARK_QUEEN_IMAGE

        self.pick_image()
        
        self.occupy_tile(initial_tile)

    def get_moves(self, board):
        # Check if piece has been removed from the board
        if self.occupied_tile is None:
            return []

        possible_moves = []

        frontier = [
            self.occupied_tile.tile_above,
            self.occupied_tile.tile_above_right,
            self.occupied_tile.tile_right,
            self.occupied_tile.tile_below_right,
            self.occupied_tile.tile_below,
            self.occupied_tile.tile_below_left,
            self.occupied_tile.tile_left,
            self.occupied_tile.tile_above_left,
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

                # Set tile to next tile
                if index == 0:
                    frontier[index] = board.tiles[value].tile_above
                elif index == 1:
                    frontier[index] = board.tiles[value].tile_above_right
                elif index == 2:
                    frontier[index] = board.tiles[value].tile_right
                elif index == 3:
                    frontier[index] = board.tiles[value].tile_below_right
                elif index == 4:
                    frontier[index] = board.tiles[value].tile_below
                elif index == 5:
                    frontier[index] = board.tiles[value].tile_below_left
                elif index == 6:
                    frontier[index] = board.tiles[value].tile_left
                elif index == 7:
                    frontier[index] = board.tiles[value].tile_above_left

        return possible_moves


class King(Piece):
    def __init__(self, piece_id, team, initial_tile):
        super().__init__(piece_id, team)

        self.image_option1 = LIGHT_KING_IMAGE
        self.image_option2 = DARK_KING_IMAGE

        self.pick_image()

        self.occupy_tile(initial_tile)

    def get_moves(self, board):
        # Check if piece has been removed from the board
        if self.occupied_tile is None:
            return []

        return []


if __name__ == '__main__':
    main()