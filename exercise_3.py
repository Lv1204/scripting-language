from math import *
from pylab import figure,plot,title,xlabel,ylabel ,show
global g
g = 9.8

def simulateTra(v0, a, fre):
    x = []
    y = []
    total = v0 * sin(a) / g
    times = total * 2 / fre
    for i in range(0, int(times)):
        x.append(v0 * fre * i * cos(a))
        y.append(v0 * fre * i * sin(a) - 0.5 * g * (i * fre)**2)
    return [x,y]

def plotPoint(x,y):
    figure()
    plot(x,y)
    title('Projectile motion')
    xlabel('Distance(m)')
    ylabel('Height(m)')
    show()

plotPoint(simulateTra(100, pi/3, 0.01)[0],simulateTra(100, pi/3, 0.01)[1])