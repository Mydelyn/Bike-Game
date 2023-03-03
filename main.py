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
    WIN.blit(BIKE_FLAT, (bike.x, bike.y))
    pygame.display.update()


def bike_handle_movement(keys_pressed, bike):
    if keys_pressed[pygame.K_a] and bike.x - VEL_X > 0:  # Left for Bike
        bike.x -= VEL_X
    if keys_pressed[pygame.K_d] and bike.x + VEL_X + bike.width < WIDTH:  # Right for Bike
        bike.x += VEL_X


def main():
    bike = pygame.Rect(50, 400, BIKE_WIDTH, BIKE_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    jumping = False
    Y_VELOCITY = JUMP_HEIGHT

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                os._exit(0)

        keys_pressed = pygame.key.get_pressed()

        bike_handle_movement(keys_pressed, bike)
        if keys_pressed[pygame.K_SPACE] and bike.y - VEL_Y > 0:
            jumping = True
        if jumping:
            bike.y -= Y_VELOCITY
            Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT

        draw_window(bike)

    main()


if __name__ == "__main__":
    main()

