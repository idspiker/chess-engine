import pygame

from player import Player
from board import Board
from specs import TILE_SIZE


WIDTH, HEIGHT = (TILE_SIZE * 10), (TILE_SIZE * 10)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Engine')

FPS = 60

# TODO TODO TODO TODO TODO
# BROKEN:
# Fix pieces moving when not selected

# IMPLEMENT:
# Castling
# King movement
# Checkmate


def main():
    board = Board(WIN)

    # Create players
    p1 = Player(1, 2, board, WIN)
    p2 = Player(2, 1, board, WIN)

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


if __name__ == '__main__':
    main()