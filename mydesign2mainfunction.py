#Main Function
from myfunction2design import *
import turtle

bob=turtle.Turtle()
bob.speed(0)
turtle.colormode(255)
turtle.bgcolor("gray")#background color
bob.width(10)

def circles(t,c,distance):
    bob.color(c)
    bob.left(90)
    bob.forward(distance)
    bob.left(50)
    bob.circle(10)
    bob.end_fill()
    bob.forward(50)
    bob.circle(10)
    bob.left(90)
   
for times in range(200):
    bob.begin_fill()
    c=(times,25,60)#color
    print (c)
    circles(bob,c,times * 2)
    
jump(bob,500,200)
for times in range(200):
    bob.begin_fill()
    c=(times,30,20)#color
    circles(bob,c,times * 2)
  
jump(bob,500,-200)
for times in range(200):
    bob.begin_fill()
    c=(100,times,40)#color
    circles(bob,c,times * 2)

jump(bob,-500,200)
for times in range(200):
    bob.begin_fill()
    c=(100,30,times)#color
    circles(bob,c,times * 2)

jump(bob,-500,-200)
for times in range(200):
    bob.begin_fill()
    c=(times,30,times)#color
    circles(bob,c,times * 2)

turtle.done()





