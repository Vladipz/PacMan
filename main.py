import  pygame
from board import boards



pygame.init()
width = 600 #хз який розмір ставити насправді
height = 650
screen = pygame.display.set_mode((width, height))
timer = pygame.time.Clock()
fps = 60

level = boards
color = "blue"
run = True

def draw_board(lvl):
    num1 = ((height - 50) // 32)
    num2 = (width // 30)
    for y in range(len(lvl)): # висота num1
        for x in range(len(lvl[y])):# ширина num2
            if level[y][x] == 1:
                pygame.draw.circle(screen, "white", (x * num2 + 0.5 * num2, y * num1 + 0.5* num1), 2)
            if level[y][x] == 2:
                pygame.draw.circle(screen, "white", (x * num2 + 0.5 * num2, y * num1 + 0.5* num1), 6)
            if level[y][x] == 3:
                pygame.draw.line(screen, color, (x * num2 + (0.5 * num2),y * num1),
                                                 (x * num2 + (0.5 * num2),y * num1+num1), 2)
            if level[y][x] == 4:
                pygame.draw.line(screen, color, (x * num2, y * num1 + (0.5 * num1)),
                                 (x * num2 + num2, y * num1 + (0.5 * num1)), 2)
            if level[y][x] == 9:
                pygame.draw.line(screen, "white", (x * num2, y * num1 + (0.5 * num1)),
                                 (x * num2 + num2, y * num1 + (0.5 * num1)), 3)



while run:
    timer.tick(fps)
    screen.fill("black")
    draw_board(level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.display.flip()

pygame.quit()