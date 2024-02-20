import pygame.transform
import pygame


# from main import width, height

class Player(object):
    def __init__(self, x, y, lives_count, direction, player_speed, maze):
        self.x = x
        self.y = y
        self.lives_count = lives_count
        self.direction = direction
        self.player_speed = player_speed
        self.player_images = []
        self.hitbox = pygame.Rect(self.x, self.y, 45, 45)
        self.maze = maze
        for i in range(1, 5):
            self.player_images.append(pygame.transform.scale(pygame.image.load(f'images/player/{i}.png'), (45, 45)))

    def hit(self):
        '''
        This function is called when the player is hit by the ghost
        :return:
        '''

        self.x = 450
        self.y = 663
        for i in range(len(self.maze.ghosts)):
            self.maze.ghosts[i].hit()
        self.lives_count -= 1

        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 301
                    pygame.quit()
