import pygame
class Joe(pygame.sprite.Sprite):
    STARTING_POSITION = (300, 450)
    SIZE = (10, 5)
    SCREEN_DIM = (600, 500)
    MOVE_DIST = 10
    IMAGE = pygame.image.load('Piskel Stuff/Joe 60-60.png')

    def __init__(self):
        super().__init__()
        self.lives = 3
        self.image = Joe.IMAGE
        self.rect = pygame.Rect((0, 0), Joe.SIZE)
        self.rect.center = Joe.STARTING_POSITION

    def ResetPosition(self):
        self.rect.center = Joe.STARTING_POSITION
        self.lives -= 1

    def move_up(self):
        if self.rect.top >= 20:
            self.rect.centery -= Joe.MOVE_DIST

    def move_down(self):
        if self.rect.bottom <= Joe.SCREEN_DIM[1] - 20:
            self.rect.centery += Joe.MOVE_DIST

    def move_left(self):
        if self.rect.left >= 20:
            self.rect.centerx -= Joe.MOVE_DIST

    def move_right(self):
        if self.rect.right <= Joe.SCREEN_DIM[0] - 20:
            self.rect.centerx += Joe.MOVE_DIST