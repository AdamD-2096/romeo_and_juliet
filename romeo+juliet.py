import turtle
import random
import sys


def main(a, r, m, wn):
    while isInScreen(a, r):
        die = random.randrange(2)
        dei = random.randrange(2)
        if die == 1: 
            r.right(random.randrange(45, 125))         
        if die == 0:
            r.left(random.randrange(45, 125))          
        if dei == 1: 
            a.left(random.randrange(45, 125))
        if dei == 0:
            a.right(random.randrange(45, 125))
            
    
        a.forward(random.randrange(30, 69, 3))
        r.forward(random.randrange(30, 69, 3))
        
    x = r.xcor() - a.xcor()    
    y = r.ycor() - a.ycor()
    a.setposition(a.xcor() + (x / 2), a.ycor() + (y / 2))
    r.setposition(r.xcor() - (x / 2), r.ycor() - (y / 2))
    m.setposition(a.xcor(), r.ycor())
    r.clear()
    a.clear()
    wn.bgcolor('aqua')
    
    if x > 0:
        a.setheading(0)
        r.setheading(180)
        r.back(16)
        a.back(16)
    else:
        a.setheading(180)
        r.setheading(0)
        a.back(16)
        r.back(16)
    d = 40
    m.right(90)
    m.forward(40)
    m.left(135)
    m.down()
    for i in range(15):
        a = d / 2
        
        m.forward(d)
        m.circle(a, 180)
        m.right(90)
        m.circle(a, 180)
        m.forward(d)
        m.up()
        d = d + 20
        m.right(45)
        m.forward(18)
        m.left(135)
        m.down()
        
        


def setStart(r, a, m):
    r.up()
    a.up()
    a.setposition(random.randrange(-100, 101), random.randrange(-100, 101))
    r.setposition(random.randrange(-100, 101), random.randrange(-100, 101))
    a.down()
    r.down()
    m.up()
    

def isInScreen(w, r):
    x = w.xcor()         
    y = w.ycor()
    a = r.xcor()
    b = r.ycor()         
    if x > 220 or x < -220 or y > 220 or y < -220:
        w.right(random.randrange(140, 220))
        w.forward(100)
        
    if a > 220 or a < -220 or b > 220 or b < -220:
        r.left(random.randrange(140, 220))
        r.forward(100)
        
    if a - x < 50 and b - y < 50 and x - a < 50 and y - b < 50:
        return False
    else:
        return True

def main1():
    m = turtle.Turtle()
    m.hideturtle()
    m.speed(0)
    m.color("blueviolet")
    m.pensize(2)
    r = turtle.Turtle()
    a = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("dimgray")
    r.color('deeppink')
    a.color('blue')
    a.shape('turtle')
    r.shape('turtle')
    r.speed(3)
    a.speed(3)



    setStart(r, a, m)
    main(a, r, m, wn)

    wn.exitonclick()


if __name__ == "__main__":
    main1()