from abc import ABC, abstractmethod
import pygame
from board import boards


class Ghost(ABC):
    def __init__(self, x, y, direction, image, player):
        self.x = x
        self.y = y
        self.image = image
        self.player = player
        self.speed = 2
        self.powerup = False
        self.hitbox = pygame.Rect(self.x, self.y, 40, 40)  # i am not sure about this
        self.x = x
        self.y = y
        self.turns = None
        self.center_x = x + 20
        self.center_y = y + 20
        self.in_box = False
        self.is_dead = False
        self.direction = direction
        self.powerup_img = pygame.transform.scale(pygame.image.load('images/ghosts/inky.png'),
                                                  (40, 40))

    def can_move(self, width, height):
        num1 = ((height - 50) // 32)
        num2 = (width // 30)
        num3 = 0
        self.turns = [False, False, False, False]
        if 0 < self.x < width - 40 and 0 < self.y < height - 40:
            if boards[(self.y - num3) // num1][(self.x + 20) // num2] == 9:
                self.turns[2] = True
            if boards[(self.y + 20) // num1][(self.x - num3) // num2] < 3 \
                    or (boards[(self.y + 20) // num1][(self.x - num3) // num2] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[1] = True
            if boards[(self.y + 20) // num1][(self.x + num3 + 40) // num2] < 3 \
                    or (boards[(self.y + 20) // num1][(self.x + num3 + 40) // num2] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[0] = True
            if boards[(self.y + num3 + 40) // num1][(self.x + 20) // num2] < 3 \
                    or (boards[(self.y + num3 + 40) // num1][(self.x + 20) // num2] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[3] = True
            if boards[(self.y - num3) // num1][(self.x + 20) // num2] < 3 \
                    or (boards[(self.y - num3) // num1][(self.x + 20) // num2] == 9 and (
                    self.in_box or self.is_dead)):
                self.turns[2] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 350 < self.x < 550 and 370 < self.y < 480:
            self.in_box = True
        else:
            self.in_box = False
        # self.turns = [True, False, False, False]

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

        self.hitbox = pygame.Rect(self.x, self.y, 40, 40)  # change hitbox coordinates
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

        ghost_rect = pygame.rect.Rect((self.x + 4, self.y + 4), (36, 36))
        return ghost_rect

    @abstractmethod
    def hit(self):
        '''
        This function is called when the ghost is hit by the player
        :return:
        '''
        pass

    @abstractmethod
    def move(self):
        pass
