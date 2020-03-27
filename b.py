import pygame
import random
pygame.init()
background = pygame.image.load("background.jpg")
screen = pygame.display.set_mode((612,612))
done = False
x = 200
y = 500
enemyx = random.randint(0,736)
enemyy = random.randint(20,50)
enemydx = 5
enemydy = 50
playerImage = pygame.image.load("player.png")
enemyImage = pygame.image.load("enemy.png")

def player(x,y):
    screen.blit(playerImage,(x,y))
def enemy(x,y):
    screen.blit(enemyImage,(x,y))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    xchange = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            xchange -= 5
        if event.key == pygame.K_RIGHT:
            xchange += 5
    if event.type == pygame.KEYUP:
        xchange = 0

    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    x+=xchange
    enemyx += enemydx
    if enemyx<0 or enemyx>736:
        enemydx = -enemydx
        enemyy += enemydy
    enemy(enemyx,enemyy)
    player(x,y)
    enemy(enemyx,enemyy)
    #pygame.draw.rect(screen, (0,128,255),pygame.Rect(x,y,60,60))
    pygame.display.flip() 