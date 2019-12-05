# Simple racet to the exit game J Joubert 28 November 2019
# This is the last game in the book Python for Kids by Jason R Briggs
# Tkinter is used in the book

# I think this version in Python 3 and Turtle may be a bit easier
# (But not as elegant)
# Play around with the jump settings for height and distance

import turtle


win = turtle.Screen()
win.title('Race to exit')
win.bgcolor('black')
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

x_list = [-200, -80, 100, -50, -200, -80, 20, 130, -40, -200]
y_list = [-220, -180, -150, -100, -50, -10, 40, 80, 140, 170]

for i in range(10):
        platform = Platform(x_list[i],y_list[i])
        platforms.append(platform)


class Door(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.up()
        self.goto(-220,190)
        self.color('red')

class Player(turtle.Turtle):
    def __init__(self, platforms):
        super().__init__(shape='circle')
        self.up()
        self.color('blue')
        self.goto(100, -220)
        self.platforms = platforms
        self.dx = 0
        self.dy = -6
        self.jump = 'stop'
        self.counter = 0
        

    def move(self):
        # Move left and right
        self.goto(self.xcor()+self.dx, self.ycor()+self.dy)

        # Don't drop off the bottom of the screen
        if self.ycor()<=-220:
            self.goto(self.xcor(), -220)
            self.dy = 0
            

        # Stop at the edges
        if self.xcor()>230 or self.xcor()<-230:
            self.dx *= 0
            

        # After pressing spacebar - jump (probably not the best solution)
        if self.jump == 'up':
            self.dy = 5 # Adjust this for height
            
            # Ajust dx*6 for distance
            self.goto(self.xcor()+self.dx*6, self.ycor()+self.dy)
            self.counter += 1
            if self.counter == 10:
                self.jump = 'down'
                
        elif self.jump == 'down':
            self.dy = -12
            self.goto(self.xcor()+self.dx*6, self.ycor()+self.dy)
            if self.ycor() <= -220:
                player.jump = 'stop'
                self.counter = 0
                self.dy = -6
        
        for i in platforms:     
            # Landing/falling on platform working
            if within_platform(player, i) and player.dy<0:
                self.sety(i.ycor()+20)
                self.dy = 0
                player.jump = 'stop'
                self.counter = 0


            # fall off platform
            if not within_platform_x(self,i) and self.ycor() == i.ycor()+20:
                self.dy = -6
                
            # Stop at the side of the platform
            if within_platform(player, i) and i.ycor()-5 <= player.ycor()<= i.ycor()+5:
                self.dx =0

            # Jumping up into a platform
            if within_platform(self,i) and self.dy>0 and self.ycor()<i.ycor()+10:
                self.sety(i.ycor()-20)
                self.jump='down'
                self.dy = -6

                                         
    def move_right(self):
        self.dx = 1
     


    def move_left(self):
        self.dx = -1
    


    def jump_up(self):
        if self.jump == 'stop':
            self.jump = 'up'



def within_platform(player, platform): 
    if platform.xcor()-45 <= player.xcor() <= platform.xcor()+45:
        if platform.ycor()-10 <= player.ycor() <= platform.ycor()+10:
            return True

def within_platform_x(player,platform):
    if platform.xcor()-45 <= player.xcor() <= platform.xcor()+45:
        return True
                    

player = Player(platforms)
door = Door()

win.onkey(player.move_right, 'Right')
win.onkey(player.move_left, 'Left')
win.onkey(player.jump_up, 'space')

game_over = False
counter = 0
while not game_over:
    counter += 1
    win.update()
    player.move()

    if player.distance(door)<20:
      
        game_over = True

win.bgcolor('yellow')
win.update()


