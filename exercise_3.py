from math import *
from pylab import figure,plot,title,xlabel,ylabel ,show
global g
g = 9.8

def simulateTra(v0, a, fre):
    x = []
    y = []
    total = v0 * sin(a) / g
    t = total * 2 / fre
    for i in range(0, fre + 1):
        x.append(v0 * t * i * cos(a))
        y.append(v0 * t * i * sin(a) - 0.5 * g * (i * t)**2)
    return [x,y]

def plotPoint(x,y):
    figure()
    plot(x,y)
    title('Projectile motion')
    xlabel('Distance(m)')
    ylabel('Height(m)')
    show()

plotPoint(simulateTra(100, pi/3, 100)[0],simulateTra(100, pi/3, 100)[1])