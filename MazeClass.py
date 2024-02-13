from Player import Player
from board import boards
from ghosts.Blinky import Blinky
from ghosts.Clyde import Clyde
from ghosts.Inky import Inky
from ghosts.Pinky import Pinky
import pygame
import math

PI = math.pi


class Maze(object):
    def __init__(self, color, width, height, screen, player):
        self.level = boards
        self.player = player
        self.width = width
        self.height = height
        self.screen = screen
        self.ghosts = [
            Blinky(self.player), Clyde(self.player), Inky(self.player), Pinky(self.player)
        ]
        self.flicker = bool

        self.isNormalMode = True
        self.color = color

    def draw_board(self):
        num1 = ((self.height - 50) // 32)
        num2 = (self.width // 30)
        for y in range(len(self.level)):  # висота num1
            for x in range(len(self.level[1])):  # ширина num2
                # if self.level[y][x] == 0
                if self.level[y][x] == 1:
                    pygame.draw.circle(self.screen, "white", (x * num2 + 0.5 * num2, y * num1 + 0.5 * num1), 2)
                if self.level[y][x] == 2 and not self.flicker:
                    pygame.draw.circle(self.screen, "white", (x * num2 + 0.5 * num2, y * num1 + 0.5 * num1), 6)
                if self.level[y][x] == 3:
                    pygame.draw.line(self.screen, self.color, (x * num2 + (0.5 * num2), y * num1),
                                     (x * num2 + (0.5 * num2), y * num1 + num1), 2)
                if self.level[y][x] == 4:
                    pygame.draw.line(self.screen, self.color, (x * num2, y * num1 + (0.5 * num1)),
                                     (x * num2 + num2, y * num1 + (0.5 * num1)), 2)
                if self.level[y][x] == 5:
                    pygame.draw.arc(self.screen, self.color,
                                    [(x * num2 - (num2 * 0.5)), (y * num1 + (num1 * 0.5)), num2, num1],
                                    0, PI / 2, 2)

                if self.level[y][x] == 6:
                    pygame.draw.arc(self.screen, self.color,
                                    [(x * num2 + (num2 * 0.5)), (y * num1 + (num1 * 0.5)), num2, num1],
                                    PI / 2, PI, 2)
                if self.level[y][x] == 7:
                    pygame.draw.arc(self.screen, self.color,
                                    [(x * num2 + (num2 * 0.5)), (y * num1 - (num1 * 0.4)), num2, num1],
                                    PI, 3 * PI / 2, 2)
                if self.level[y][x] == 8:
                    pygame.draw.arc(self.screen, self.color,
                                    [(x * num2 - (num2 * 0.4) - 2), (y * num1 - (num1 * 0.4)), num2, num1],
                                    3 * PI / 2, 2 * PI, 2)
                if self.level[y][x] == 9:
                    pygame.draw.line(self.screen, "white", (x * num2, y * num1 + (0.5 * num1)),
                                     (x * num2 + num2, y * num1 + (0.5 * num1)), 3)

    def draw_ghosts(self):
        for i in range(len(self.ghosts)):
            self.ghosts[i].draw(self.screen)
            self.ghosts[i].can_move(self.width, self.height)
            self.ghosts[i].move()

    def draw_player(self, counter):
        # 0-RIGHT, 1-LEFT, 2-UP, 3-DOWN
        direction = self.player.direction
        player_images = self.player.player_images
        player_x = self.player.x
        player_y = self.player.y

        if direction == 0:
            self.screen.blit(player_images[counter % len(player_images)], (player_x, player_y))
        elif direction == 1:
            self.screen.blit(pygame.transform.flip(player_images[counter % len(player_images)], True, False),
                             (player_x, player_y))
        elif direction == 2:
            self.screen.blit(pygame.transform.rotate(player_images[counter % len(player_images)], 90),
                             (player_x, player_y))
        elif direction == 3:
            self.screen.blit(pygame.transform.rotate(player_images[counter % len(player_images)], 270),
                             (player_x, player_y))
        pygame.draw.rect(self.screen, (255, 0, 0), self.player.hitbox, 2)
    def check_position(self, center_x, center_y):
        turns = [False, False, False, False]
        num1 = (self.height - 50) // 32
        num2 = (self.width // 30)
        num3 = 15
        # check collisions based on center x and center y of player +/- fudge number
        if center_x // 30 < 29:
            if self.player.direction == 0:
                if self.level[center_y // num1][(center_x - num3) // num2] < 3:
                    turns[1] = True
            if self.player.direction == 1:
                if self.level[center_y // num1][(center_x + num3) // num2] < 3:
                    turns[0] = True
            if self.player.direction == 2:
                if self.level[(center_y + num3) // num1][center_x // num2] < 3:
                    turns[3] = True
            if self.player.direction == 3:
                if self.level[(center_y - num3) // num1][center_x // num2] < 3:
                    turns[2] = True

            if self.player.direction == 2 or self.player.direction == 3:
                if 12 <= center_x % num2 <= 18:
                    if self.level[(center_y + num3) // num1][center_x // num2] < 3:
                        turns[3] = True
                    if self.level[(center_y - num3) // num1][center_x // num2] < 3:
                        turns[2] = True
                if 12 <= center_y % num1 <= 18:
                    if self.level[center_y // num1][(center_x - num2) // num2] < 3:
                        turns[1] = True
                    if self.level[center_y // num1][(center_x + num2) // num2] < 3:
                        turns[0] = True
            if self.player.direction == 0 or self.player.direction == 1:
                if 12 <= center_x % num2 <= 18:
                    if self.level[(center_y + num1) // num1][center_x // num2] < 3:
                        turns[3] = True
                    if self.level[(center_y - num1) // num1][center_x // num2] < 3:
                        turns[2] = True
                if 12 <= center_y % num1 <= 18:
                    if self.level[center_y // num1][(center_x - num3) // num2] < 3:
                        turns[1] = True
                    if self.level[center_y // num1][(center_x + num3) // num2] < 3:
                        turns[0] = True
        else:
            turns[0] = True
            turns[1] = True

        return turns

    def move_player(self, turns_allowed):
        player_speed = self.player.player_speed
        direction = self.player.direction

        if direction == 0 and turns_allowed[0]:
            self.player.x += player_speed
        elif direction == 1 and turns_allowed[1]:
            self.player.x -= player_speed
        if direction == 2 and turns_allowed[2]:
            self.player.y -= player_speed
        elif direction == 3 and turns_allowed[3]:
            self.player.y += player_speed
        self.player.hitbox = pygame.Rect(self.player.x, self.player.y, 45, 45)
        return self.player.x, self.player.y