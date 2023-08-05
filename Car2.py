import pygame
class Car2(pygame.sprite.Sprite):
    RIGHT_IMAGE = pygame.image.load('Piskel Stuff/Car 2.png')
    STARTING_POSITION = (300, 225)
    SIZE = (60, 30)
    SCREEN_DIM = (600, 500)
    MOVE_DIST = 2
    def __init__(self, StartingPosition: tuple, direction: str):
        super().__init__()
        self.image = Car2.RIGHT_IMAGE if direction == 'Right' else Car2.RIGHT_IMAGE
        self.rect = pygame.Rect((0,0), Car2.SIZE)
        self.rect.center = Car2.STARTING_POSITION
        self.direction = direction
    def move(self):
        self.rect.centerx -= Car2.MOVE_DIST
        if self.rect.right <= 0:
            self.rect.centerx = Car2.SCREEN_DIM[0] + (Car2.SIZE[0] / 2)
