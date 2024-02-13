import pygame
from board import boards
import math

from MazeClass import Maze

pygame.init()
width = 900
height = 950
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
    maze.draw_ghosts()
    maze.draw_player(counter)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                maze.player.direction = 0
            if event.key == pygame.K_LEFT:
                maze.player.direction = 1
            if event.key == pygame.K_UP:
                maze.player.direction = 2
            if event.key == pygame.K_DOWN:
                maze.player.direction = 3
    pygame.display.flip()

pygame.quit()
