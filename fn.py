import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.interpolate import UnivariateSpline
from matplotlib.widgets import Slider

fig = plt.figure()
ax = fig.subplots()

n = 80
k = 1
x = 1

plt.xlim(0, n)
plt.ylim(0, n)

plt.subplots_adjust(bottom = 0.25)
ax_slide = plt.axes([0.25, 0.1, 0.65, 0.03])
s_factor = Slider(ax_slide, 'Vlna', valmin = 1, valmax = 10, valinit = 1, valstep = 0.5)

x1 = np.arange(0,n)
y1 = np.arange(0,n)
t = np.arange(0, 30, 0.1)

def oscilator(time, n):
    return (np.pi/2) * np.sin(n+time) + np.pi/2 

def update(val):
    global x
    current_v = s_factor.val
    x = current_v
    x = val
    ax.cla()
    animace()
    fig.canvas.draw()

s_factor.on_changed(update)

def angle(radian):
    u = math.cos(radian)
    v = math.sin(radian)
    return u, v

def animace():
    global n
    for i in range(n):
        for k in range(n):
            u, v = angle(oscilator(x, k))
            ax.arrow(i, k, u, v , head_width=0.5, head_length=0.5, color = 'r')

for z in range(len(t)):
    update(t[z])
    print(str(t[z]))
    plt.pause(0.0001)
            
plt.show()