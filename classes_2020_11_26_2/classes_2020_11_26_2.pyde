x,y = 600,600 
dim=112 
x1=x/2 
y1=y-dim/2 
dy=0 
speed=1900000

def setup(): 
    global x,y 
    size(x,y) 
    background(0) 
def keyPressed(): 
    global x1,speed 
    if key == 'a': 
        x1=x1-speed 
    if key == 'd': 
        x1=x1+speed 

def keyReleased(): 
    global dy 
    if key == ' ': 
        dy=dy-19 

def draw(): 
    background(170,50,50) 
    global dim,y1,x1,dy 
    dy=dy+0.3 
    if y1+dy > height-dim/2+1: 
        dy=-0.5*dy 
        y1=y1+dy 
    if x1<-dim/2: 
        x1=width-dim/2 
    if x1>width+dim/2: 
        x1=dim/2 
    ellipse(x1,y1,dim,dim) 
    fill(0,0,0)
