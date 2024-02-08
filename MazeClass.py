#from Player import Player
from board import boards

import pygame
import math



PI = math.pi
class Maze(object):
    def __init__(self, color,width, height, screen):
        self.level = boards
        #self.player = Player(0,0,3)
        self.width = width
        self.height = height
        self.screen = screen
        #TODO add ghost class
        #self.ghosts


        self.isNormalMode = True
        self.color = color
    def draw_board(self):
        num1 = ((self.height - 50) // 32)
        num2 = (self.width // 30)
        for y in range(len(self.level)):  # висота num1
            for x in range(len(self.level[1])):  # ширина num2
                if self.level[y][x] == 1:
                    pygame.draw.circle(self.screen, "white", (x * num2 + 0.5 * num2, y * num1 + 0.5 * num1), 2)
                if self.level[y][x] == 2:
                    pygame.draw.circle(self.screen, "white", (x * num2 + 0.5 * num2, y * num1 + 0.5 * num1), 6)
                if self.level[y][x] == 3:
                    pygame.draw.line(self.screen, self.color, (x * num2 + (0.5 * num2), y * num1),
                                     (x * num2 + (0.5 * num2), y * num1 + num1), 2)
                if self.level[y][x] == 4:
                    pygame.draw.line(self.screen, self.color, (x * num2, y * num1 + (0.5 * num1)),
                                     (x * num2 + num2, y * num1 + (0.5 * num1)), 2)
                if self.level[y][x] == 5:
                    pygame.draw.arc(self.screen, self.color, [(x * num2 - (num2 * 0.5)), (y * num1 + (num1 * 0.5)), num2, num1],
                                    0, PI / 2, 2)

                if self.level[y][x] == 6:
                    pygame.draw.arc(self.screen, self.color, [(x * num2 + (num2 * 0.5)), (y * num1 + (num1 * 0.5)), num2, num1],
                                    PI / 2, PI, 2)
                if self.level[y][x] == 7:
                    pygame.draw.arc(self.screen, self.color, [(x * num2 + (num2 * 0.5)), (y * num1 - (num1 * 0.4)), num2, num1],
                                    PI, 3 * PI / 2, 2)
                if self.level[y][x] == 8:
                    pygame.draw.arc(self.screen, self.color,
                                    [(x * num2 - (num2 * 0.4) - 2), (y * num1 - (num1 * 0.4)), num2, num1],
                                    3 * PI / 2, 2 * PI, 2)
                if self.level[y][x] == 9:
                    pygame.draw.line(self.screen, "white", (x * num2, y * num1 + (0.5 * num1)),
                                     (x * num2 + num2, y * num1 + (0.5 * num1)), 3)



