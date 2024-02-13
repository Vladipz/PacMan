from abc import ABC, abstractmethod
import pygame
from Movable import Movable


class Ghost(Movable):
    def __init__(self, x, y, direction, image, player):
        self.x = x
        self.y = y
        self.image = image
        self.player = player
        self.speed = 2
        self.powerup = False
        self.hitbox = (self.x, self.y, 40, 40)  # i am not sure about this
        super().__init__(x, y, False, False, direction)
        self.powerup_img = pygame.transform.scale(pygame.image.load('images/ghosts/inky.png'),
                                                  (40, 40))


    def draw(self, screen):
        '''
        Draws the ghost on the screen
            :param screen:
            :return:
        '''
        if not self.is_dead and not self.powerup:
            screen.blit(self.image, (self.x, self.y))

        elif not self.is_dead and self.powerup:
            screen.blit(self.powerup_img, (self.x, self.y))

        self.hitbox = (self.x, self.y, 40, 40)  # change hitbox coordinates
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

        ghost_rect = pygame.rect.Rect((self.x + 4, self.y + 4), (36, 36))
        return ghost_rect
    def hit(self):
        '''
        This function is called when the ghost is hit by the player
        :return:
        '''

    @abstractmethod
    def move(self):
        pass
