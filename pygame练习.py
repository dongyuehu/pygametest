import pygame,sys

pygame.init()
size=w,h=640,480
speed=[1,1]
black=0,0,0


screen=pygame.display.set_mode(size)
pygame.display.set_caption("pygame游戏之旅-壁球")

ball = pygame.image.load("PYG02-ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]


    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.displlay.update()


'''
# 天气不错

'''
