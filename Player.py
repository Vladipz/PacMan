import pygame.transform
import pygame
import path


class Player(object):
    def __init__(self, x, y, lives_count, direction, player_speed, maze):
        self.x = x
        self.y = y
        self.lives_count = lives_count
        self.direction = direction
        self.player_speed = player_speed
        self.player_images = []

        self.maze = maze

        for i in range(0, 4):
            self.player_images.append(pygame.transform.scale(pygame.image.load(path.player_images[i]), (45, 45)))

        self.hitbox = self.player_images[0].get_rect()
        self.hitbox.size = (30, 30)
        self.width = 30
        self.height = 30
        self.hitbox.center = self.x + 23, self.y + 24

    def hit(self, screen: pygame.Surface):
        """
        This function is called when the player is hit by the ghost
        :return:
        """
        
        self.x = 450
        self.y = 663
        for i in range(len(self.maze.ghosts)):
            self.maze.ghosts[i].hit()
        self.lives_count -= 1
        if self.lives_count < 1:
            pass
        else:
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        i = 301
                        pygame.quit()
