import turtle
from random import randint
a=turtle.Turtle()
t=turtle.Turtle()
z=turtle.Screen()
window = turtle.Screen()
window.colormode(255)
a.speed(0)
t.speed(0)
z.bgcolor(255,255,255)

def spiral_b(acc):
    while acc<=1000:
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        if acc<=100:
            for i in range (100):
                t.color(r,g,b)
                t.forward(i*acc)
                t.left(1000)
            acc=acc+1


    
def art(s):
    spiral_b()

def squarecenter(s):
    turtle.speed(0)
    n=int(input('Please enter in how many times you want to loop:  '))
    for i in range (s,0 ,-10):
        r=randint(0,255)
        g=randint(0,255)
        b=randint(0,255)
        turtle.pu()
        turtle.setpos
        (-i/2,i/2)
        turtle.pd()
        turtle.color(r,g,b)
        turtle.begin_fill()
        for x in range (4):
            turtle.forward(i)
            turtle.right(90)
        turtle.left(90)
        for x in range (4):
            turtle.forward(i)
            turtle.right(90)
        
        turtle.end_fill()

def art2(acc):
        for i in range (100):
            a.forward(10)
            a.right(365)
        

art2(0)

#spiral_b(0)
#squarecenter(230)
