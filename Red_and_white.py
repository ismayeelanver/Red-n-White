import pygame
import random

pygame.init()

height = 800
width = 800
screen = pygame.display.set_mode((width, height))

title = pygame.display.set_caption("Red 'n White")
icon = pygame.display.set_icon(pygame.image.load("icon.png"))

snake_speed = 1
dot = pygame.Rect(400, 400, 40, 40)
apple = pygame.Rect(random.randint(0, 800), random.randint(0, 800), 40, 40)
score = 0
font = pygame.font.SysFont(None, 30)

def controls():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        dot.y -= snake_speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        dot.y += snake_speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        dot.x -= snake_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        dot.x += snake_speed

def run():
    controls()
running = True
while running:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), dot)
    pygame.draw.rect(screen, (255, 0, 0), apple)
    if dot.colliderect(apple):
        apple.x = random.randint(0, 800)
        apple.y = random.randint(0, 800)
        score += 1
    if dot.y == height:
        dot.y = 400
        score = 0
    if dot.x == width:
        dot.x = 400
        score = 0
    if dot.y == 0:
        dot.y = 400
        score = 0
    if dot.x == 0:
        score = 0
        dot.x = 400
    text = font.render("Score: " + str(score), True, (255, 255, 255))

    screen.blit(text, (10, 10))
    run()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()