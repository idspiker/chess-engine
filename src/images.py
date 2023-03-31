import pygame
import os


from specs import TILE_SIZE


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