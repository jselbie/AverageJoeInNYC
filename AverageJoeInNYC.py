from Joe import Joe
from Street import Street
import pygame, sys
import random

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption('Game')
FPS = 60
CLOCK = pygame.time.Clock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (28, 128, 28)
YELLOW = (100, 85, 0)
BROWN = (118, 92, 72)
GRAY = (175, 175, 175)
BLUE = (0, 0, 175)

joe = Joe()

streets = []
number_of_buses = 5
street_height = 400

for _ in range(2):
    streets.append(Street(street_height, 'Left', random.randint(1, number_of_buses)))
    streets.append(Street(street_height - 40, 'Right', random.randint(1, number_of_buses)))
    street_height -= 80

while True:
    CLOCK.tick(FPS)
    SCREEN.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:  # W
                    joe.move_up()
                if event.key == pygame.K_a:  # A
                    joe.move_left()
                if event.key == pygame.K_s:  # S
                    joe.move_down()
                if event.key == pygame.K_d:  # D
                    joe.move_right()

    for street in streets:
        SCREEN.fill(GRAY, street.rect)
        for bus in street.buses:
            SCREEN.blit(bus.image, bus.rect)
            bus.move()
            if joe.rect.colliderect(bus.rect):
                joe.ResetPosition()

    SCREEN.blit(joe.image, joe.rect)

    pygame.display.flip()

pygame.quit()

