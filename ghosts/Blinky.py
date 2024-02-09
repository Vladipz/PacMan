import pygame.image
from ghosts.Ghost import Ghost


class Blinky(Ghost):
    def __init__(self, player):
        image = pygame.transform.scale(pygame.image.load('images/ghosts/blinky.png'),
                                       (40, 40))
        super().__init__(56, 40, 0, image, player)
