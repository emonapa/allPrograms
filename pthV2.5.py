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

fig, (ax1, ax2) = plt.subplots(ncols=2, gridspec_kw={'width_ratios': [2, 1]})
fig.canvas.set_window_title('Clear Plotting')
fig.set_size_inches(8, 5.32)
fig.subplots_adjust(wspace=0)

ax1.set_aspect('equal')
ax1.autoscale(False)
#ax1.spines['left'].set_position(('data', 0))
#ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['top'].set_visible(False) 
ax1.spines['right'].set_visible(False)
ax1.set_xlim(-2,2)
ax1.set_ylim(-2,2)

ax2.axis('off')

"""TADY ZAČÍNÁ KÓD"""

def SetXYLim():
    ax1.set_xlim(-2,2)
    ax1.set_ylim(-2,2)
    ax2.set_xlim(-5,5)
    ax2.set_ylim(-10,10)

ktext = fig.add_axes([0.8, 0.8, 0.1, 0.075])
text_box1 = TextBox(ktext, '', initial='')
def handle_ktext_submit(text):
    global l
    global m
    UnitVector(int(text), l, m)
text_box1.on_submit(handle_ktext_submit)
text_box1.set_active(True)

ltext = fig.add_axes([0.8, 0.7, 0.1, 0.075])
text_box2 = TextBox(ltext, '', initial='')
def handle_ltext_submit(text):
    global k
    global m
    UnitVector(k, int(text), m)
text_box2.on_submit(handle_ltext_submit)
text_box2.set_active(True)

mtext = fig.add_axes([0.8, 0.6, 0.1, 0.075])
text_box3 = TextBox(mtext, '', initial='')
def handle_mtext_submit(text):
    global k
    global l
    UnitVector(k, l, int(text))
text_box3.on_submit(handle_mtext_submit)
text_box3.set_active(True)

def UnitVector(a,b,c):
    global k
    global l
    global m
    if a != "" and b != "" and c != "" and (a+b+c)!=0:
        vector = [a, b, c]
        k,l,m = vector / np.linalg.norm(vector)



SetXYLim()
"""KONSTANTY"""
anglex = 0
angley = 0
anglez = 0
angle = 0
distance = 80
xmouse = 0
ymouse = 0

k,l,m = 0,0,0

x = np.linspace(-10, 10, 1000)
y3 = np.cos(x)

ax1.plot(x, y3)

class Cube:
    def __init__(self, x1 = -0.5, y1 = -0.5, z1 = -0.5, x2 = 0.5, y2 = -0.5, z2 = -0.5, x3 = 0.5, y3 = 0.5, z3 = -0.5, 
                x4 = -0.5, y4 = 0.5, z4 = -0.5, x5 = -0.5, y5 = -0.5, z5 = 0.5, x6 = 0.5, y6 = -0.5, z6 = 0.5, 
                x7 = 0.5, y7 = 0.5, z7 = 0.5, x8 = -0.5, y8 = 0.5, z8 = 0.5):      
        
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2
        self.x3 = x3
        self.y3 = y3
        self.z3 = z3
        self.x4 = x4
        self.y4 = y4
        self.z4 = z4
        self.x5 = x5
        self.y5 = y5
        self.z5 = z5
        self.x6 = x6
        self.y6 = y6
        self.z6 = z6
        self.x7 = x7
        self.y7 = y7
        self.z7 = z7
        self.x8 = x8
        self.y8 = y8
        self.z8 = z8

        self.points = [
            [self.x1, self.y1, self.z1],
            [self.x2, self.y2, self.z2],
            [self.x3, self.y3, self.z3],
            [self.x4, self.y4, self.z4],
            [self.x5, self.y5, self.z5],
            [self.x6, self.y6, self.z6],
            [self.x7, self.y7, self.z7],
            [self.x8, self.y8, self.z8]
        ]
        
        self.xPoints = [None, None, None, None, None, None, None, None, None, None, None, None]
        self.yPoints = [None, None, None, None, None, None, None, None, None, None, None, None]
        self.previousPoints = [None, None, None, None, None, None, None, None]
        self.previousLines = [None, None, None, None, None, None, None, None, None, None, None, None]

    def DrawLine(self, index1, index2, k):
        x = [self.xPoints[index1-1], self.xPoints[index2-1]]
        y = [self.yPoints[index1-1], self.yPoints[index2-1]]
        self.previousLines[k] = ax1.plot(x,y)

    def DrawLines(self):
        self.DrawLine(1,2,0)
        self.DrawLine(2,3,1)
        self.DrawLine(3,4,2)
        self.DrawLine(4,1,3)
        self.DrawLine(5,6,4)
        self.DrawLine(6,7,5)
        self.DrawLine(7,8,6)
        self.DrawLine(8,5,7)
        self.DrawLine(1,5,8)
        self.DrawLine(2,6,9)
        self.DrawLine(3,7,10)
        self.DrawLine(4,8,11)

    def DeletePoints(self):
        for i in cube.previousPoints:
            rm = i.pop()
            rm.remove()        
        fig.canvas.draw_idle()

    def DeleteLines(self):
        for i in cube.previousLines:
            rm = i.pop()
            rm.remove()        
        fig.canvas.draw_idle()

    def AlfaTransform(self, point):
        global angle
        global k
        global l
        global m
        alfa = point[0]*np.cos(angle) + (l*point[2]-m*point[1])*np.sin(angle) + k*(k*point[0] + l*point[1] + m*point[2])*(1-np.cos(angle))
        return alfa
    
    def BetaTransform(self, point):
        global angle
        global k
        global l
        global m
        beta = point[1]*np.cos(angle) + (m*point[0]-k*point[2])*np.sin(angle) + l*(k*point[0] + l*point[1] + m*point[2])*(1-np.cos(angle))
        return beta
    
    def GamaTransform(self, point):
        global angle
        global k
        global l
        global m
        gama = point[2]*np.cos(angle) + (k*point[1]-l*point[0])*np.sin(angle) + m*(k*point[0] + l*point[1] + m*point[2])*(1-np.cos(angle))
        return gama
         
    def DrawCube(self):
        global angle
        global distance
        k = 0
        for pointP in self.points:
            x = (distance* self.AlfaTransform(pointP))/(distance - self.GamaTransform(pointP))
            y = (distance* self.BetaTransform(pointP))/(distance - self.GamaTransform(pointP))
            self.xPoints[k] = x
            self.yPoints[k] = y
            cube.previousPoints[k] = ax1.plot(x, y, 'o', color = 'r', markersize=13 )
            k+=1
        self.DrawLines()  
         
cube = Cube()
cube.DrawCube()

def pressKeyAny(event):
    global anglex
    global angley
    match event.key:
        case 'a':
            pass
        case 'd':
            pass       
        case '8':
            anglex -= 0.1
        case '6':
            angley -= 0.1
        case '2':
            anglex += 0.1           
        case '4':
            angley += 0.1
    fig.canvas.draw_idle() 
fig.canvas.mpl_connect('key_press_event', pressKeyAny)

def zoom(event):
    ax1 = event.inaxes
    global angle
    if event.key == 'control' and event.button == 'down':
        x_start, x_end = ax1.get_xlim()
        y_start, y_end = ax1.get_ylim()
        ax1.set_xlim((x_start*1.1, x_end*1.1))
        ax1.set_ylim((y_start*1.1, y_end*1.1))
    elif event.key == 'control' and event.button == 'up':
        x_start, x_end = ax1.get_xlim()
        y_start, y_end = ax1.get_ylim()
        ax1.set_xlim((x_start*0.9, x_end*0.9))
        ax1.set_ylim((y_start*0.9, y_end*0.9))
    elif event.button == 'up':
        angle += +0.1
        cube.DeleteLines()
        cube.DeletePoints()
        cube.DrawCube()
    elif event.button == 'down':
        angle += -0.1
        cube.DeleteLines()
        cube.DeletePoints()
        cube.DrawCube()
    fig.canvas.draw_idle()  
fig.canvas.mpl_connect('scroll_event', zoom)

def on_move(event):
    global ymouse
    global xmouse
    global angle 
    global k
    global l
    global m
    secondm = 0
    if event.key == 'alt' and event.button == 1:
        ax1.start_pan(0, 0, 1)
        ax1.drag_pan(1, "shift", event.x-xmouse, event.y-ymouse)
        xmouse = event.x
        ymouse = event.y
        fig.canvas.draw()
    elif event.button == 1:
        if np.abs(event.y-ymouse - event.x-xmouse) < 2:
            secondm = (event.y-ymouse + event.x-xmouse)/2
        UnitVector(-(event.y-ymouse)/10 , (event.x-xmouse)/10, secondm) 
        print("[ " + str(event.x-xmouse) + ", " + str(event.y-ymouse) + " ]")
        print() 
        angle += 0.1
        cube.DeleteLines()
        cube.DeletePoints()
        cube.DrawCube()
        xmouse = event.x
        ymouse = event.y

    else:
        xmouse= event.x
        ymouse = event.y
fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()

