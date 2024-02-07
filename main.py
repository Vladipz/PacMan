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
    for i in range(len(lvl)): # висота num1
        for j in range(len(lvl[i])):# ширина num2
            if level[i][j] == 1:
                pygame.draw.circle(screen, "white", (j * num2 + 0.5 * num2, i * num1 + 0.5* num1), 2)
            if level[i][j] == 2:
                pygame.draw.circle(screen, "white", (j * num2 + 0.5 * num2, i * num1 + 0.5* num1), 6)
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2),i * num1),
                                                 (j * num2 + (0.5 * num2),i * num1+num1), 2)
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 2)



while run:
    timer.tick(fps)
    screen.fill("Red")
    draw_board(level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        pygame.display.flip()

pygame.quit()