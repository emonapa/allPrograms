import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(6,6))
plt.xlim(0,100)
plt.ylim(0,100)

speed = 0.1
k = 0
r = 0

def rko(event):
    global r
    global k
    global speed
    if (event.key == 'w'):
        r += speed
        print('rko je: ' + str(round(r, 3)))
        f(r,k) 
 
def kcko(event):
    global k
    global r
    global speed
    if (event.key == 'd'):
        k += speed
        f(r,k)   
        print('kcko je: ' + str(round(k, 3))) 

cid1 = fig.canvas.mpl_connect('key_press_event', rko)
cid2 = fig.canvas.mpl_connect('key_press_event', kcko)

def f(radius, kacko):
    global r
    global k 
    r = (radius**3 + kacko**3)**(1/3)
    print('nove rko je: ' + str(r) )
    ctverec(r, k)
    plt.draw()
    
def ctverec(r, k):  
    ax.add_patch(Rectangle((0, 0), r, r, color = 'r'))
    ax.add_patch(Rectangle(((r-k)/2, (r-k)/2), k, k, color = 'w'))   
    plt.draw()

plt.show()


        