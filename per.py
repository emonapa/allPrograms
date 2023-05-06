import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider, Button
import time
from threading import Thread
from matplotlib.pyplot import figure

onoff = False
poprve = True
fig = plt.figure()
fig.axes
ax = fig.add_subplot(1,1,1)


lines = []

axred = plt.axes([0.18, 0.01, 0.65, 0.03])
createred = Slider(axred, 'Red', 0.0, 80, 1)

axbutton = fig.add_axes([0.6, 0.9, 0.1, 0.075])
createbutton = Button(axbutton, 'On/Off')

axbutton1 = fig.add_axes([0.7, 0.9, 0.1, 0.075])
createbutton1 = Button(axbutton1, 'CLOSE')

plt.xlim(-4, 4)
plt.ylim(-4, 4)


radius = 1
dt = 0.01
g = 9.8
my_angle = 50
tim = 0

def toggle(val):
    global onoff
    onoff = not onoff
    if(onoff == True): Thread(target=main).start()

def toggle1(val):
    plt.close('all')

def toggle_angle(val):
    global my_angle
    my_angle = createred.val

def update_position():
    global dt
    global g
    global radius
    global my_angle
    global tim

    tim += dt
    period = 2 * np.pi * np.sqrt(radius/g)
    angle = np.radians(my_angle) * np.cos(2*np.pi / period * tim)

    x = radius * np.sin(angle)
    y = -1*(radius * np.cos(angle))

    return x,y 

def main():
    global onoff    
    global poprve
    global lines    
    while onoff: #main loop
        if poprve or len(lines) == 0: 
            lines = ax.plot([0,0], [0,0], color = 'red') 
            lines.append(ax.scatter(0,0, color = 'r'))
            poprve = False
        
        l = lines.pop(0).remove() 
        k = lines.pop(0).remove() 
        x,y = update_position()
        lines = ax.plot([0,x], [0,y], color= 'red')  
        lines.append(ax.scatter(x,y, color = 'r', s = 80))
        plt.draw()               
        time.sleep(0.00000001)                    
        plt.xlim([-4, 4])
        plt.ylim([-4, 4])

createbutton.on_clicked(toggle) 
createbutton1.on_clicked(toggle1) 
createred.on_changed(toggle_angle)
plt.show()