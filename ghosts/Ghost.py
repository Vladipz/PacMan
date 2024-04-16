from abc import ABC, abstractmethod
import pygame
from board import boards
from Observer import Observer
import path

class Ghost(Observer, ABC):
    def __init__(self, x, y, direction, image, player, powerup_player):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.player = player
        self.speed = 2
        self.powerup = False
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        self.x = x
        self.y = y
        self.turns = None
        self.direction = direction
        self.powerup = False
        self.powerup_player = powerup_player
        self.normal_img = pygame.transform.scale(pygame.image.load(image),
                                                 (self.width, self.height))
        self.powerup_img = pygame.transform.scale(pygame.image.load(path.ghosts_image[4]),
                                                  (self.width, self.height))
        self.image = self.normal_img

    def can_move(self, width, height):
        num1 = ((height - 50) // 32)
        num2 = (width // 30)
        num3 = 1
        self.turns = [False, False, False, False]
        if 0 < self.x < width - self.width and 0 < self.y < height - self.height:
            if boards[(self.y - num3) // num1][(self.x + 20) // num2] == 9:
                self.turns[2] = True
            if boards[(self.y + 20) // num1][(self.x - num3) // num2] < 3:
                self.turns[1] = True
            if boards[(self.y + 20) // num1][(self.x + num3 + self.width) // num2] < 3:
                self.turns[0] = True
            if boards[(self.y + num3 + self.width) // num1][(self.x + 20) // num2] < 3:
                self.turns[3] = True
            if boards[(self.y - num3) // num1][(self.x + 20) // num2] < 3:
                self.turns[2] = True
        else:
            self.turns[0] = True
            self.turns[1] = True
        if 350 < self.x < 550 and 370 < self.y < 480:
            self.in_box = True
        else:
            self.in_box = False

    def update(self, powerup):
        self.powerup = powerup
        if self.powerup:
            self.image = self.powerup_img
        else:
            self.image = self.normal_img

    def draw(self, screen):
        '''
        Draws the ghost on the screen
            :param screen:
            :return:
        '''
        if not self.powerup:
            screen.blit(self.image, (self.x, self.y))

        else:
            screen.blit(self.powerup_img, (self.x, self.y))

        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)  # change hitbox coordinates
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

        ghost_rect = pygame.rect.Rect((self.x + 4, self.y + 4), (36, 36))
        return ghost_rect

    def choose_target(self):
        if self.powerup:
            return self.powerup_player
        else:
            return self.player

    @abstractmethod
    def hit(self):
        '''
        This function is called when the ghost is hit by the player
        :return:
        '''
        self.powerup = False
        self.image = self.normal_img

    @abstractmethod
    def move(self):
        pass
