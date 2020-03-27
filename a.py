import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
done = False
x = 30
y = 30

'''playerImage = pygame.image.load("player.png")
def player():
    screen.blit(playerImage,(x,y))'''


color1 = (12,198,252)
color2 = (25,3,1)
is_color1 = True
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #color    
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_color1 = not is_color1
    #move    
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            y-=3
        if event.key == pygame.K_DOWN:
            y+=3
        if event.key == pygame.K_RIGHT:
            x+=3
        if event.key == pygame.K_LEFT:
            x-=3   
    '''pressed = pygame.key.get_pressed()
    if pressed(pygame.K_UP): y-=3
    if pressed(pygame.K_DOWN):y+=3
    if pressed(pygame.RIGHT):x+=3
    if pressed(pygame.K_LEFT):x-=3'''
    if is_color1:
        color = color1
    else:
        color = color2
    
    screen.fill((0,0,0))
    #player(x,y)
    pygame.draw.rect(screen, (0,128,255),pygame.Rect(x,y,60,60))
    pygame.display.flip() 