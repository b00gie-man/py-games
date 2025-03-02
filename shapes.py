import pgzrun

from random import randint

WIDTH=300
HEIGHT=300

def draw():
     w=WIDTH
     h=HEIGHT-200
     for i in range(20):
        red=randint(0,255)
        green=randint(0,255)    
        blue=randint(0,255)
        r=Rect((0,0),(w,h))
        r.center=(150,150)
        screen.draw.rect(r,"teal")
        screen.draw.rect(r,(red,green,blue))

        w=w-10
        h=h+10


def draw():
     w=WIDTH
     h=HEIGHT-200
     for i in range(36):
        red=randint(0,255)
        green=randint(0,255)    
        blue=randint(0,255)
        r=Rect((0,0),(w,h))
        r.center=(150,150)
        screen.draw.rect(r,"teal")
        screen.draw.rect(r,(red,green,blue))

        w=w-21
        h=h+21


pgzrun.go()