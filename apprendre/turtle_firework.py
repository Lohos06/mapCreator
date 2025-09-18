from turtle import *
import random

speed(0)

for steps in range(250) :
    for color in ("red","indigo","purple") :
        pencolor(color)

        distance = random.randint(200, 500)
        tracer(False)
        for i in range(2) :
            forward(distance)
            right(179)
        update()

done()
