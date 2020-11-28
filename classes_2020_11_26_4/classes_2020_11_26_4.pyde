y1=0 
x=512 
y=512 

def setup() : 
    size(x,y) 
    fill(255,0,0) 



def keyReleased(): 
    global x ,y ,x1 ,y1 
    if key == ' ': 
        x1 = random (0,x) 
        y1 = random (0,y)  
    background(22,2,5) 
    ellipse(x1,y1,100,100) 
    fill(random(0,255),random(0,255),random(0,255)) 

def draw():
    global x1 ,y1 
    background(22,2,5) 
     
