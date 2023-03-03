import pygame
import os

pygame.init()
WIDTH, HEIGHT = 1700, 700  # Window Width and Height.
BIKE_WIDTH, BIKE_HEIGHT = 330, 230
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
FPS = (60)
VEL_X = 6
VEL_Y = 6
Y_GRAVITY = 1
JUMP_HEIGHT = 20
jumping = False

jump_speed = 4
Y_VELOCITY = JUMP_HEIGHT

pygame.display.set_caption("FirstDraftRemake")

FOREST = pygame.transform.scale(pygame.image.load(os.path.join('BikeAssets', 'bikebackround.png')), (WIDTH, HEIGHT))
BIKE_FLAT_IMAGE = pygame.image.load(os.path.join('BikeAssets', 'Bike.png'))

BIKE_FLAT = pygame.transform.scale(BIKE_FLAT_IMAGE, (BIKE_WIDTH, BIKE_HEIGHT))

jumping = False


def draw_window(bike):  # Draws things onto the background window
    WIN.blit(FOREST, (0, 0))


