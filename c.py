import pygame
import random
pygame.init()
screen = pygame.display.set_mode((612,612))

playerImage = pygame.image.load("player.png")
player_x = 306
player_y = 550

enemyImage = pygame.image.load("enemy.png")
enemy_x = random.randint(0,736)
enemy_y = random.randint(20,50)
enemy_dx = 5
enemy_dy = 50

bulletImage = pygame.image.load("bullet.png")
bullet_x = 306
bullet_y = 586

backgroundImage = pygame.image.load("background.jpg")

def player(x,y):
    screen.blit(playerImage,(x,y))

def enemy(x,y):
    screen.blit(enemyImage,(x,y))

def bullet(x,y):
    screen.blit(bulletImage,(x,y))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_x = player_x-5
            bullet_x = bullet_x-5
        if event.key == pygame.K_RIGHT:
            player_x = player_x+5
            bullet_x = bullet_x+5
        if event.key == pygame.K_SPACE:
            if bullet_y < 0:
                bullet_y += 500
            bullet_y-=5
    dist_x = bullet_x - enemy_x
    dist_y = bullet_y - enemy_y
    
    if -16 <= dist_x <= 48 and -16 <= dist_y <= 48 :
        bullet_x, bullet_y = 306, 586
        enemy_x, enemy_y = random.randint(0, 736), random.randint(20, 50)

    screen.fill((0,0,0))    
    screen.blit(backgroundImage,(0,0))
    player(player_x,player_y)
    bullet(bullet_x,bullet_y)
    enemy_x+=enemy_dx
    if enemy_x<0 or enemy_x>612:
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy
    if enemy_y > 612:
        enemy_y -=570
    enemy(enemy_x,enemy_y)
    pygame.display.flip()  
