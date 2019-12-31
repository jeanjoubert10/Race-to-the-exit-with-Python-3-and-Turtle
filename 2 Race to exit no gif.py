# Simple racet to the exit game J Joubert 28 November 2019
# This is the last game in the book Python for Kids by Jason R Briggs
# Tkinter is used in the book

# I think this version in Python 3 and Turtle may be a bit easier
# (But not as elegant)
# Play around with the jump settings for height and distance

import turtle
# import time # and time.sleep(0.017) windows??


win = turtle.Screen()
win.title('Race to exit')
win.bgcolor('lightblue')
win.setup(500,500)
win.tracer(0)
win.listen()

   
# Place the platforms    
platforms = []

class Platform(turtle.Turtle):
    def __init__(self, xpos, ypos):
        super().__init__(shape='square')
        self.shapesize(0.5,4)
        self.color('red')
        self.up()
        self.xpos = xpos
        self.ypos = ypos
        self.goto(self.xpos, self.ypos)

# Create and place the platforms
x_list = [-200, -50, 110, -50, -200, -50, 50, 130, -20, -180]
y_list = [-220, -180, -150, -100, -50, -10, 40, 100, 140, 170]

for i in range(10):
        platform = Platform(x_list[i],y_list[i])
        platforms.append(platform)


class Door(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.up()
        self.goto(-220,190)
        self.color('purple')


class Player(turtle.Turtle):
    def __init__(self, platforms):
        super().__init__(shape='circle')
        self.up()
        self.color('blue')
        self.goto(100, -220)
        self.platforms = platforms
        self.dx = 0
        self.dy = 0
        self.gravity = 0.2
         

    def move(self):
        # Move left/right or up/down depending on dy and dx
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

        # Effect of gravity (dy starts at 0 and then decreases with gravity every loop)
        self.dy -= self.gravity

        # Don't drop off the bottom of the screen
        if self.ycor()<=-220:
            self.goto(self.xcor(), -220)
            self.gravity = 0
            self.dy = 0
            

        # Stop at the edges of screen
        if self.xcor()>230 or self.xcor()<-230:
            self.dx *= 0  

        
        for i in platforms:     
            # Landing/falling on platform working only if moving down (dy < 0)
            if within_platform(player, i) and player.dy<0:
                self.sety(i.ycor()+20)
                self.gravity = 0
                self.dy = 0


            # fall off platform
            if not within_platform_x(self,i) and self.ycor() == i.ycor()+20:
                self.gravity = 0.2
                
                
            # Stop at the side of the platform
            if within_platform(player, i) and i.ycor()-5 <= player.ycor()<= i.ycor()+5:
                self.dx =0


            # Jumping up into a platform stops upward motion
            if within_platform(self,i) and self.dy>0 and self.ycor()<i.ycor()+10:
                self.sety(i.ycor()-20) # prevents landing on the platform
                self.gravity = 0.2
                self.dy = 0

                                         
    def move_right(self):
        self.dx = 1.5
     


    def move_left(self):
        self.dx = -1.5
    

    def jump_up(self):
        if self.dy == 0:
            self.dy = 6
            self.gravity = 0.2
        else:
            print('You cannot jump in the air or when falling off a platform')


# Collision checks:
def within_platform(player, platform): 
    if platform.xcor()-45 <= player.xcor() <= platform.xcor()+45: # Within x
        if platform.ycor()-10 <= player.ycor() <= platform.ycor()+10: # Within y
            return True

def within_platform_x(player,platform):
    if platform.xcor()-45 <= player.xcor() <= platform.xcor()+45: # Only within x
        return True
                    

player = Player(platforms)
door = Door()

win.onkey(player.move_right, 'Right')
win.onkey(player.move_left, 'Left')
win.onkey(player.jump_up, 'space')

game_over = False


while not game_over:
    #time.sleep(0.017) # windows??
    win.update()
    player.move()

    if player.distance(door)<20:
        game_over = True

win.bgcolor('yellow')
win.update()







