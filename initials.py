import pygame

pygame.init()

display=pygame.display.set_mode((600,600))
pygame.display.set_caption("Initials")

running =True
while running:
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running=False

    display.fill("blue")
    
    pygame.draw.rect(display,("lime"),(250,250,10,200))
    pygame.draw.rect(display,("lime"),(250,250,100,10))
    pygame.draw.rect(display,("lime"),(350,250,10,100))
    pygame.draw.rect(display,("lime"),(350,250,100,10))
    pygame.draw.rect(display,("lime"),(450,250,10,200))
    pygame.display.flip()


#1.imports pygame= import pygame
#2.Initalizes pygame=pygame.init()
#3.create a game window of a specific size = display=pygame.display.set_mode((600,600))
#4.set the windows title = pygame.display.set_caption("Basic Pygame Windows")
#5.Fills in the color = display.fill("blue")
#6.Update the entire screen =  pygame.display.flip()