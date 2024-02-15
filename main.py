import pygame
from board import boards
import math
import Player
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
turns_allowed = [False, False, False, False]
direction_command = 0
score = 0
power = False
power_counter = 0
eaten_ghosts = [False, False, False, False]
moving = False
startup_counter = 0
run = True
player = Player.Player(450, 663, 3, 0, 2)

maze = Maze("blue", width, height, screen, player)

while run:
    timer.tick(fps)

    if counter < 19:
        counter += 1
        if counter > 3:
            maze.flicker = False
    else:
        counter = 0
        maze.flicker = True
    if power and power_counter <600:
        power_counter+=1
    elif power and power_counter >= 600:
        power_counter=0
        power=False
        eaten_ghosts = [False, False, False, False]
    if startup_counter<180:
        moving=False
        startup_counter+=1
    else:
        moving=True
    # # Перевірка колізій між гравцем та привидами
    # if pygame.sprite.spritecollide(maze.player, maze.ghosts, False):
    #     player.hit()

    for ghost in maze.ghosts:
        if maze.player.hitbox.colliderect(ghost.hitbox):
            maze.player.hit(screen)
            break

    screen.fill("black")
    maze.draw_board()
    maze.draw_ghosts()
    maze.draw_player(counter)
    player_x = maze.player.x
    player_y = maze.player.y
    center_x = player_x + 23
    center_y = player_y + 24
    turns_allowed = maze.check_position(center_x, center_y)
    if moving:
        player_x, player_y = maze.move_player(turns_allowed)
    score, power, power_counter, eaten_ghosts = maze.check_collisions(score, center_x=center_x, center_y=center_y, power=power, power_count=power_counter,
                                  eaten_ghosts=eaten_ghosts)
    maze.draw_misc(score, power=power)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction_command = 0
            if event.key == pygame.K_LEFT:
                direction_command = 1
            if event.key == pygame.K_UP:
                direction_command = 2
            if event.key == pygame.K_DOWN:
                direction_command = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and direction_command == 0:
                direction_command = maze.player.direction
            if event.key == pygame.K_LEFT and direction_command == 1:
                direction_command = maze.player.direction
            if event.key == pygame.K_UP and direction_command == 2:
                direction_command = maze.player.direction
            if event.key == pygame.K_DOWN and direction_command == 3:
                direction_command = maze.player.direction

    for i in range(4):
        if direction_command == i and turns_allowed[i]:
            maze.player.direction = i

    if maze.player.x > 900:
        maze.player.x = -47
    elif maze.player.x < -50:
        maze.player.x = 897

    if maze.player.direction == 0 and turns_allowed[0]:
        maze.player.direction = 0
    if maze.player.direction == 1 and turns_allowed[1]:
        maze.player.direction = 1
    if maze.player.direction == 2 and turns_allowed[2]:
        maze.player.direction = 2
    if maze.player.direction == 3 and turns_allowed[3]:
        maze.player.direction = 3

    pygame.display.flip()

pygame.quit()
