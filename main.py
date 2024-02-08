import pygame
from board import boards
import math

from MazeClass import Maze

pygame.init()
width = 600  # хз який розмір ставити насправді
height = 650
screen = pygame.display.set_mode((width, height))
timer = pygame.time.Clock()
fps = 60
PI = math.pi
level = boards
color = "blue"

counter = 0


run = True
maze = Maze("blue", width, height, screen)

while run:
    timer.tick(fps)
    if counter < 19:
        counter += 1
        if counter > 3:
            maze.flicker = False
    else:
        counter = 0
        maze.flicker = True

    screen.fill("black")
    maze.draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.display.flip()

pygame.quit()
