w = 500
h = 500

class Cube:
    def __init__(self):
        self.x = w/3
        self.size = 40
        self.y = h-(60+self.size)
        self.velocity = 0 
        self.acc = 0.5
    def draw(self):
        fill(255,255,255)
        rect(self.x,self.y,self.size,self.size)
        self.y += self.velocity
        if self.y>=h-(60+self.size):
            self.velocity = 0
        else:     
            self.velocity += self.acc
    def jump(self):
        self.velocity = -10    

class Obstacle:
    def __init__(self):
        self.x = 550
        self.size = random(30,45)
        self.y = h-(60+self.size) + int(random(0.5,1.5))*-50
    def draw(self):
        self.x -= 4  
        fill(255,10,10)
        rect(self.x,self.y,self.size,self.size)  



class Ground:
    def __init__(self):
        self.x = 0
        self.y = h -60
    def draw(self):
        fill(60,200,20)
        rect(self.x,self.y,w,60)                

player = Cube()
ground = Ground()              
obs = []
obs.append(Obstacle())
def setup():
    size(w,h)

def collision(player,obs):
    if obs.x>=player.x and obs.x<=player.x+player.size:
        if obs.y<=player.y+player.size and obs.y>=player.y:
            return True
    return False     

score = 0    
def draw():
    global obs, score
    background(510) 
    player.draw()
    ground.draw()
    for i in obs:
        i.draw() 
        if collision(player,i):
            score = 0  
    if obs[-1].x<player.x:
        obs.append(Obstacle())
        score += 1
    if len(obs)>3:
        obs = obs[-3:]
    text('Score : '+str(score),w/2,h/4)   
            
            

def mouseReleased():
    player.jump()     
