import pygame
from ghosts.Ghost import Ghost


class Pinky(Ghost):
    def __init__(self, player):
        image = pygame.transform.scale(pygame.image.load('images/ghosts/pinky.png'),
                                       (40, 40))
        super().__init__(480, 300, 2, image, player)
