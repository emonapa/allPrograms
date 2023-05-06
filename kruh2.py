import matplotlib.pyplot as plt
import numpy as np
import time 


fig, ax = plt.subplots(figsize=(6,6))

x = []
y = []
x2 = []
y2 = []
poprve = True
linear = 0.9

def zmensi(event):
    global linear
    if (event.key == 'x'):
        linear -= 0.05
        zmensi(linear) 

cid = fig.canvas.mpl_connect('key_press_event', zmensi)

#def help_release(event): 
     #global linear
     #plt.clf()
     #linear = 1.05

#cid2 = fig.canvas.mpl_connect('key_release_event', help_release)

def zmensi(k):
    global poprve
    global x
    global y 
    global x2 
    global y2 
    if (poprve):
        x2 = x
        y2 = y
        poprve = False

    x2= [ i*0.9 for i in x2 ]
    y2= [ p*0.9 for p in y2 ]

    plt.plot(x,y2, color = 'green') 
    plt.plot(x2,y, color = 'green')

    update()

#plt.xlim(-1.5, 1.5)
#plt.ylim(-1.5, 1.5)


def update():
    plt.draw() 

p = 0.01
t = np.arange(0, 2*np.pi, p)

#body kruhu
for i in t:
    x.append(np.sin(i))
    y.append(np.cos(i))
    
plt.plot(x,y, color='green')



plt.show()

