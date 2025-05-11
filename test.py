import pygame 
pygame.init()


WIDTH =600
HEIGHT =600

display=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("zylaphone")

ding=pygame.mixer.Sound("note1.mp3")
dong=pygame.mixer.Sound("note2.mp3")
ping=pygame.mixer.Sound("note3.mp3")
pong=pygame.mixer.Sound("noteA.mp3")
dink=pygame.mixer.Sound("noteB.mp3")
donk=pygame.mixer.Sound("noteC.mp3")
pink=pygame.mixer.Sound("noteD.mp3")
ponk=pygame.mixer.Sound("noteE.mp3")


small_rect_x =600
small_rect_y =300

FPS=20
clock=pygame.time.Clock()

running = True
while running:

        

    display.fill("black")
    
    a=pygame.draw.rect(display,("blue"),(85,50,50,550))
    b=pygame.draw.rect(display,("red"),(132,50,50,525))
    c=pygame.draw.rect(display,("green"),(181,50,50,500))
    d=pygame.draw.rect(display,("purple"),(229,50,50,475))
    e=pygame.draw.rect(display,("orange"),(276,50,50,450))
    f=pygame.draw.rect(display,("pink"),(323,50,50,425))
    g=pygame.draw.rect(display,("violet"),(371,50,50,400))
    h=pygame.draw.rect(display,("indigo"),(419,50,50,375))

    small_rect=pygame.draw.rect(display,"white", (small_rect_x, small_rect_y, 40,40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                small_rect_x -= 20
            if event.key == pygame.K_RIGHT:
                small_rect_x += 20
            if event.key == pygame.K_UP:
                small_rect_y -= 20
            if event.key == pygame.K_DOWN:
                small_rect_y += 20



    if small_rect.colliderect (a):
        ding.play()
    
    if small_rect.colliderect (b):
        dong.play()
    
    if small_rect.colliderect (c):
        ping.play()

    if small_rect.colliderect (d):
        pong.play()

    if small_rect.colliderect (e):
        dink.play()

    if small_rect.colliderect (f):
        donk.play()

    if small_rect.colliderect (g):
        pink.play()

    if small_rect.colliderect (h):
        ponk.play()
    
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit