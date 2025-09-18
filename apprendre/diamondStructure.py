from turtle import *
from math import *

speed(0)
tracer(False)
taille = 0

def hyp(a, b = None) :
     if b is None :
        b = a
     return sqrt(a**2 + b**2)

def diamond() :
        left(45)
        forward(taille)
        left(135)
        forward(hyp(taille))
        left(135)
        forward(taille)

        up()
        left(90)
        forward(taille)
        down()

        left(90)
        forward(hyp(hyp(taille)/4))
        left(45)
        forward(hyp(taille)/2)
        left(45)
        forward(hyp(hyp(taille)/4))

        up()
        right(180)
        forward(hyp(hyp(taille)/4))
        down()



        up()
        home()
        down()

componentsNumber = 1
modulesNumber = 1

for modules in range(modulesNumber) :
    taille += 60
    for steps in range(componentsNumber) :
        diamond()
        left((steps+1)*360/componentsNumber)
update()
done()