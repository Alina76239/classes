width=800
height=600
left_score = 0
right_score = 0
left_y = 40
right_y = 260
ball_x = 390
ball_y = 290
ball_dy = -3
ball_dx = -3
left_key = ""
right_key = ""
mode = "instruction-screen"
def reset_game():
    global left_score, right_score, left_y, right_y, ball_x, ball_y, ball_dy, ball_dx
    left_score = 0
    right_score = 0
    left_y = 40
    right_y = 260
    ball_x = 390
    ball_y = 290
    ball_dy = -3
    ball_dx = -3
    mode = "instruction-screen"

def ball_reset():
    global ball_x, ball_y 
    ball_x = 390
    ball_y = 290 
def setup():
    size(width,height) 
    
def draw():
    global ball_x, ball_y, ball_dy, ball_dx, left_score, right_score, mode  
    global left_y, right_y
    background(200)
    if mode == "instruction-screen":
        text ("To start the game press one of the buttons:w,s,i,k",width/3,height/4)
    
    elif mode == "game-over":
        if right_score > left_score:
            text("right player wins", 300,300)
        else:
            text("left player wins", 300,300)
                 
    elif mode == "game-on":
        if left_key == "w":
            left_y += -2
        elif left_key == "s":
            left_y += 2 
        elif right_key == "i":
            right_y += -2
        elif right_key == "k":
            right_y += 2    
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy
    
        if ball_y > 580 or ball_y < 0 :
            ball_dy =  ball_dy * - 1
    

        if ball_x > 780:
            left_score += 1
            ball_reset()    
        elif  ball_x < 0 :
            right_score += 1 
            ball_reset() 
        if right_score > 0 or left_score > 0:
            mode = "game-over"

        if ball_x < 50 and ball_y > left_y and ball_y < (left_y + 80) :
            ball_dx = ball_dx * -1  
   
        if ball_x > 740 and ball_y > right_y and ball_y < (right_y + 80) :
            ball_dx = ball_dx * -1  
    if mode == "game-on" or mode == "game-over":              
        text ("PONG", 350 , 40)
        text (left_score, 40, 40)
        text (right_score, 760, 40)
    
        rect(30,left_y,20,80)
        rect(750,right_y,20,80)
    
        rect(ball_x,ball_y,20,20)
    
def keyReleased():
    global left_key, right_key
    if key == "w":
        left_key = ""
    elif key == "s":
        left_key = "" 
    elif key == "i":
        right_key = ""
    elif key == "k":
        right_key == ""    
             
def keyPressed():
    global left_y, right_y, mode, left_key, right_key

    if mode == "instruction-screen":
        mode = "game-on"
    
    if mode == "game-over":
        print ("resent game")
        mode = "game-on"  
        reset_game()          
        
    if key == "w":
        left_key = "w"           

    elif key == "s":
        left_key = "s" 
    
    if key == "i":
        right_key = "i"
        
    elif key == "k":
        right_key = "k"
        
