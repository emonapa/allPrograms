import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(10,10))
plt.rcParams['keymap.save'].remove('s')
plt.xlim(0,20)
plt.ylim(0,20)
place = True
k = 1/2
speed = 1/2

minula_krychle = []
cary_krychle = []

class Krychle:
  
  def __init__(self, x1, y1, x2, y2):
      self.x1 = x1
      self.y1 = y1
      self.x2 = x2
      self.y2 = y2

  def krychle(self):
      global minula_krychle
      global cary_krychle
      global place

      print('[' + str(self.x1)+ ', '+str(self.y1)+ '] ['+str(self.x2)+ ', '+str(self.y2) + ']')

      width, height = self.x2 - self.x1, self.y2 - self.y1
      rect1 = Rectangle((self.x1, self.y1), width, height, fill=False, color='red')
      rect2 = Rectangle((self.x1+k, self.y1+k), width, height, fill=False, color='red')

#vypocet lajn
      A = [self.x1, self.x1+k]
      B = [self.y2, self.y2+k]

      A1 = [self.x2, self.x2+k]
      B1 = [self.y2, self.y2+k]

      K = [self.x1, self.x1+k]
      L = [self.y1, self.y1+k]

      K1 = [self.x2, self.x2+k]
      L1 = [self.y1, self.y1+k]
      
#krychle 
      minula_krychle = cary_krychle.copy()

      cary_krychle = [
      plt.plot(A, B, color = 'red'),
      plt.plot(A1, B1, color = 'red'),
      plt.plot(K, L, color = 'red'),
      plt.plot(K1, L1, color = 'red'),
      ax.add_patch(rect1),
      ax.add_patch(rect2)
      ]   
      
      if (len(minula_krychle) != 0) and (place):
          for i in range(4):
              l = minula_krychle[i].pop()
              l.remove()
          minula_krychle[4].remove()
          minula_krychle[5].remove()

      place = True

p1 = Krychle(1,1,2,2)
p1.krychle()

#eventy
def nahoru(event):
    global speed
    if (event.key == 'w'):
        global OMEGA  
        global p1 
        p1.y1 += speed
        p1.y2 += speed 
        p1.krychle()
        plt.draw()
        
def dolu(event):
    global speed
    if (event.key == 's'):
        global p1
        p1.y1 -= speed
        p1.y2 -= speed 
        p1.krychle()       
        plt.draw()
       
def doleva(event):
    global speed
    if (event.key == 'a'):
        global p1
        p1.x1 -= speed
        p1.x2 -= speed 
        p1.krychle()       
        plt.draw()
        
def doprava(event):
    global speed
    if (event.key == 'd'):
        global p1  
        p1.x1 += speed
        p1.x2 += speed  
        p1.krychle()       
        plt.draw()

def ynahoru(event):
    global speed
    if (event.key == '8'):
        global p1 
        p1.y2 += speed
        p1.krychle()       
        plt.draw()

def ydolu(event):
    global speed
    if (event.key == '2'):
        global p1 
        p1.y2 -= speed
        p1.krychle()       
        plt.draw()

def xdoleva(event):
    global speed
    if (event.key == '4'):
        global p1 
        p1.x2 -= speed
        p1.krychle()       
        plt.draw()

def xdoprava(event):
    global speed
    if (event.key == '6'):
        global p1 
        p1.x2 += speed
        p1.krychle()       
        plt.draw()

def plus(event):
    global k
    if (event.key == '+'):
        global p1 
        k += 1/2
        p1.krychle()       
        plt.draw()

def minus(event):
    global k
    if (event.key == '-'):
        global p1 
        k -= 1/2
        p1.krychle()       
        plt.draw()

def enter(event):
    global k
    global place
    if (event.key == '0'):
        global p1 
        place = False       
        plt.draw()
        
cid1 = fig.canvas.mpl_connect('key_press_event', nahoru)
cid2 = fig.canvas.mpl_connect('key_press_event', dolu)
cid3 = fig.canvas.mpl_connect('key_press_event', doleva)
cid4 = fig.canvas.mpl_connect('key_press_event', doprava)

cid5 = fig.canvas.mpl_connect('key_press_event', ynahoru)
cid6 = fig.canvas.mpl_connect('key_press_event', ydolu)
cid7 = fig.canvas.mpl_connect('key_press_event', xdoleva)
cid8 = fig.canvas.mpl_connect('key_press_event', xdoprava)

cid9 = fig.canvas.mpl_connect('key_press_event', plus)
cid10 = fig.canvas.mpl_connect('key_press_event', minus)

cid11 = fig.canvas.mpl_connect('key_press_event', enter)

plt.show()

