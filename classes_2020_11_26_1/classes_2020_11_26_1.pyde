def setup(): 
    size(512,512) 

def draw(): 
     background(0,2,2) 
     rectMode(CORNER) 
     fill(255,255,0) 
     noStroke() 
     rect(0,256,512,512) 
     rectMode(CENTER) 
     fill(256,0,0) 
     stroke(2,0,245) 
     ellipse(mouseX,mouseY-30,60,60) 
