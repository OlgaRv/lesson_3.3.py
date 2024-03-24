import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("img/Тир.jpeg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_heigth = 80
target_speed = 1
direction = "right"

target_x = random.randint(0, SCREEN_WIDTH- target_width)
target_y = random.randint(0, SCREEN_HEIGTH-target_heigth)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# счетчик попыток попадания
attempts = 0

# шрифт для отображения текста
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x<mouse_x<target_x + target_width and target_y<mouse_y<target_y + target_heigth:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGTH - target_heigth)
                attempts +=1

    if direction == "right":
        target_x += target_speed
        if target_x == SCREEN_WIDTH-target_width:
            target_x -= target_speed
            direction = "left"
    elif direction == "left":
        target_x -= target_speed
        if target_x == 0:
            target_x += target_speed
            direction = "right"

    # вывод результата попыток попадания
    text = font.render("ТАБЛО: " + str(attempts), True, (0,0, 0))
    screen.blit(text, (10, 10))

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()