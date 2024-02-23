import pygame
from Player import Player
from ghosts.Ghost import Ghost

class Pinky(Ghost):
    def __init__(self, player):
        super().__init__(440, 390, 2, 'images/ghosts/pinky.png', player, Player(800, 950, 0, 0, 0, None))

    def hit(self):
        super().hit()
        self.x = 440
        self.y = 338

    def move(self):
        player = self.choose_target()

        if self.direction == 0:
            self.move_towards_player(player, self.x + self.speed, self.y, self.turns[0], 1, 2, 3)

        elif self.direction == 1:
            self.move_towards_player(player, self.x - self.speed, self.y, self.turns[1], 0, 2, 3)

        elif self.direction == 2:
            self.move_towards_player(player, self.x, self.y - self.speed, self.turns[2], 0, 1, 3)

        elif self.direction == 3:
            self.move_towards_player(player, self.x, self.y + self.speed, self.turns[3], 0, 1, 2)

        if self.x < -30:
            self.x = 900
        elif self.x > 900:
            self.x = 30

    def move_towards_player(self, player, new_x, new_y, turn, dir1, dir2, dir3):
        if turn:
            self.x = new_x
            self.y = new_y
            return

        if player.x > self.x and self.turns[dir1]:
            self.direction = dir1
        elif player.x < self.x and self.turns[dir2]:
            self.direction = dir2
        elif self.turns[dir3]:
            self.direction = dir3

        if self.direction == dir1:
            self.x += self.speed
        elif self.direction == dir2:
            self.x -= self.speed
        elif self.direction == dir3:
            self.y += self.speed
