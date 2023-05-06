import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.widgets import TextBox, Button

plt.rcParams['toolbar'] = 'None'
mpl.rcParams['axes.xmargin'] = 0
mpl.rcParams['axes.ymargin'] = 0

# Nastavení vzdálenosti mezi osou grafu a okrajem okna
mpl.rcParams['figure.subplot.left'] = 0
mpl.rcParams['figure.subplot.bottom'] = 0
mpl.rcParams['figure.subplot.right'] = 1
mpl.rcParams['figure.subplot.top'] = 1

fig, ax = plt.subplots()
fig.canvas.set_window_title('Clear Plotting')
fig.set_size_inches(8, 8)

ax.autoscale(False)
#Osy x a y
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

"""TADY ZAČÍNÁ KÓD"""
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
"""KONSTANTY"""
r = 5
xmouse = 0
ymouse = 0

x = np.linspace(-10, 10, 1000)
y1 = np.sqrt(r**2 - x**2)-r
y3 = np.cos(x)

curve, = plt.plot(x, y1)
plt.plot(x, y3)

def plot_circle():
    global x
    global r
    global curve
    curve.remove()
    y1 = np.sqrt(r**2 - x**2)-r
    curve, = plt.plot(x, y1)
    fig.canvas.draw()

def zoom(event):
    ax = event.inaxes
    global r
    if event.key == 'control' and event.button == 'down':
        x_start, x_end = ax.get_xlim()
        y_start, y_end = ax.get_ylim()
        ax.set_xlim((x_start*1.1, x_end*1.1))
        ax.set_ylim((y_start*1.1, y_end*1.1))
    elif event.key == 'control' and event.button == 'up':
        x_start, x_end = ax.get_xlim()
        y_start, y_end = ax.get_ylim()
        ax.set_xlim((x_start*0.9, x_end*0.9))
        ax.set_ylim((y_start*0.9, y_end*0.9))
    elif event.button == 'down':
        r-=0.5
        plot_circle()
    elif event.button == 'up':
        r+=0.5
        plot_circle()
    fig.canvas.draw_idle()  
fig.canvas.mpl_connect('scroll_event', zoom)

def on_move(event):
    global ymouse
    global xmouse 
    if event.key == 'alt' and event.button == 1:
        ax.start_pan(0, 0, 1)
        ax.drag_pan(1, "shift", event.x-xmouse, event.y-ymouse) 
        xmouse = event.x
        ymouse = event.y
        fig.canvas.draw()
    else:
        xmouse= event.x
        ymouse = event.y
fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()

