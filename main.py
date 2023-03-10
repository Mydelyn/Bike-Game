import pygame
import os

pygame.init()
WIDTH, HEIGHT = 1700, 700  # Window Width and Height.
BIKE_WIDTH, BIKE_HEIGHT = 330, 230
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
FPS = 15
VEL_X = 12
VEL_Y = 12
Y_GRAVITY = 2.3
JUMP_HEIGHT = 25

jump_speed = 25

pygame.display.set_caption("FirstDraftRemake")

FOREST = pygame.transform.scale(pygame.image.load(os.path.join('BikeAssets', 'bikebackround.png')), (WIDTH, HEIGHT))
BIKE_FLAT_LIST = [pygame.image.load(os.path.join('SpriteListBike', 'BikeSpriteL1.png')),
                  pygame.image.load(os.path.join('SpriteListBike', 'BikeSpriteL2.png')),
                  pygame.image.load(os.path.join('SpriteListBike', 'BikeSpriteL3.png')),
                  pygame.image.load(os.path.join('SpriteListBike', 'BikeSpriteL4.png')),
                  pygame.image.load(os.path.join('SpriteListBike', 'BikeSpriteL5.png')),
                  pygame.image.load(os.path.join('SpriteListBike', 'BikeSpriteL6.png')),
                  pygame.image.load(os.path.join('SpriteListBike', 'BikeSpriteL7.png')),
                  pygame.image.load(os.path.join('SpriteListBike', 'BikeSpriteL8.png')),
                  pygame.image.load(os.path.join('SpriteListBike', 'BikeSpriteL9.png'))]


def draw_window(BIKE_FLAT, bike):  # Draws things onto the background window
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
    value = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                os._exit(0)

        if value >= len(BIKE_FLAT_LIST):
            value = 0

        BIKE_FLAT = BIKE_FLAT_LIST[value]

        BIKE_FLAT = pygame.transform.scale(BIKE_FLAT, (BIKE_WIDTH, BIKE_HEIGHT))

        pygame.display.update()

        value += 1

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
            print("Y VEL", Y_VELOCITY)
            print("Jumping height", JUMP_HEIGHT)
            print("Bike.y", bike.y)
            bike.y = bike.y + 20
            bike.y = bike.y + 7
        draw_window(BIKE_FLAT, bike)

    main()


if __name__ == "__main__":
    main()
