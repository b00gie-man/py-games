import pygame
pygame.init()

WIDTH=600
HEIGHT=600

c1 = "red"
c2 = "gold"

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Basic Pygame Windows")

MIDAS_SIZE = 20
PERSON1_SIZE = 20
PERSON2_SIZE = 20
PERSON3_SIZE = 20
PERSON4_SIZE = 20

head_dx = 0
head_dy = 0

Midas=pygame.draw.rect(screen,c2,(head_dx,head_dy,MIDAS_SIZE,MIDAS_SIZE))
person1position=(500,500,PERSON1_SIZE,PERSON1_SIZE)
person1=pygame.draw.rect(screen,c1,person1position)
person2position=(0,0,PERSON2_SIZE,PERSON2_SIZE)
person2=pygame.draw.rect(screen,c1,person2position)
person3position=(500,500,PERSON3_SIZE,PERSON3_SIZE)
person3=pygame.draw.rect(screen,c1,person3position)
person4position=(-500,-500,PERSON4_SIZE,PERSON4_SIZE)
person4=pygame.draw.rect(screen,c1,person4position)

speed = 10
Midas_dx=0
Midas_dy=0

FPS=30
clock=pygame.time.Clock()

gameloop = True

while gameloop:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               gameloop = False

     if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
               Midas_dx=1*speed
               Midas_dy=0
          elif event.key == pygame.K_LEFT:
               Midas_dx=-1*speed
               Midas_dy=0
          elif event.key == pygame.K_UP:
               Midas_dx=0
               Midas_dy=-1*speed
          elif event.key == pygame.K_DOWN:
               Midas_dx=0
               Midas_dy=1*speed
     
    
     head_dx=head_dx+Midas_dx
     head_dy=head_dy+Midas_dy

       
    
     screen.fill("black")

     if Midas.colliderect(person1):
          person1=pygame.draw.rect(screen,c2,person1position)
    
     if Midas.colliderect(person2):
          person2=pygame.draw.rect(screen,c2,person2position)

     if Midas.colliderect(person3):
          person3=pygame.draw.rect(screen,c2,person3position)
     if Midas.colliderect(person4):
          person4=pygame.draw.rect(screen,c2,person4position)

     Midas=pygame.draw.rect(screen,c2,(head_dx,head_dy,MIDAS_SIZE,MIDAS_SIZE))
     person1position=(500,500,PERSON1_SIZE,PERSON1_SIZE)
     person1=pygame.draw.rect(screen,c1,person1position)
     person2position=(30,30,PERSON2_SIZE,PERSON2_SIZE)
     person2=pygame.draw.rect(screen,c1,person2position)
     person3position=(30,500,PERSON3_SIZE,PERSON3_SIZE)
     person3=pygame.draw.rect(screen,c1,person3position)
     person4position=(500,75,PERSON4_SIZE,PERSON4_SIZE)
     person4=pygame.draw.rect(screen,c1,person4position) 
    
     pygame.display.flip()
     clock.tick(FPS)

pygame.quit()