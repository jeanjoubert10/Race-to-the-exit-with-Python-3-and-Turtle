# Simple racet to the exit game J Joubert 28 November 2019
# This is the last game in the book Python for Kids by Jason R Briggs
# Tkinter is used in the book
# I think this version in Python 3 and Turtle may be a bit easier
# (But not as elegant)

import turtle


win = turtle.Screen()
win.title('Race to exit')
win.setup(500,500)
win.tracer(0)
win.listen()

shape_list = ['door1.gif', 'door2.gif', 'stick-L1.gif', 'stick-L2.gif', 'stick-L3.gif', 'stick-R1.gif', 'stick-R2.gif', 'stick-R3.gif',
              'platform1.gif', 'platform2.gif', 'platform3.gif', 'background.gif', 'stick-flat.gif']

# Register gif files as shapes
for i in  shape_list:
    win.register_shape(i)
    

# Place background gif 5 in a row in x and y
bg_x = [-200,-100,0,100,200]
bg_y = [-200,-100,0,100,200]

for i in bg_x:
    for j in bg_y:
        background = turtle.Turtle()
        background.up()
        background.shape('background.gif')
        background.goto(i,j)
   

# Place the platforms    
platforms = []
# y, x, gif (from bottom to top)
pf = [
    [-220,-200, 'platform1.gif'],
    [-180,-80, 'platform1.gif'],
    [-150,100, 'platform1.gif'],
    [-100,-50, 'platform2.gif'],
    [-50,-200, 'platform2.gif'],
    [-10,-80, 'platform3.gif'],
    [40,20, 'platform3.gif'],
    [80,130, 'platform1.gif'],
    [140,-40, 'platform2.gif'],
    [170, -200, 'platform2.gif']
    ]

for i in pf:
    platform = turtle.Turtle()
    platform.up()
    platform.goto(i[1], i[0])
    platform.shape(i[2])
    if i[2] == 'platform1.gif':
        platform.width = 50
        platform.height = 10
    elif i[2] == 'platform2.gif':
        platform.width = 33
        platform.height = 10
    elif i[2] == 'platform3.gif':
        platform.width = 16
        platform.height = 10
    platforms.append(platform)


class Door(turtle.Turtle):
    def __init__(self):
        super().__init__(shape='door1.gif')
        self.up()
        self.goto(-220,190)
        self.color('red')


class Player(turtle.Turtle):
    def __init__(self, platforms):
        super().__init__(shape='square')
        self.up()
        self.color('blue')
        self.s = 'stick-R1.gif'
        self.shape(self.s)
        self.goto(100, -220)
        self.platforms = platforms
        self.dx = 0
        self.dy = -6
        self.jump = 'stop'
        self.counter = 0
        self.flat = False # use to stop when lying flat after hitting head

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
            

        # After pressing spacebar - jump - working!!!!
        if self.jump == 'up':
            self.dy = 5
           
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

            # Jumping up into a platform bumping head
            if within_platform(self,i) and self.dy>0 and self.ycor()<i.ycor()+10:
                self.sety(i.ycor()-20)
                self.jump='down'
                self.dy = -6
                self.flat = True
                self.shape('stick-flat.gif')

                                         
    def move_right(self):
        if self.flat != True:
            self.dx = 1
            self.s = 'stick-R1.gif'


    def move_left(self):
        if self.flat != True:
            self.dx = -1
            self.s = 'stick-L1.gif'


    def jump_up(self):
        if self.jump == 'stop' and self.flat != True:
            self.jump = 'up'


    def animate(self):
        
        if player.dx<0:
            if self.s == 'stick-L1.gif' and counter%10 == 0:
                self.s = 'stick-L2.gif'
                self.shape(self.s)
            elif player.s == 'stick-L2.gif' and counter%10 == 0:
                self.s = 'stick-L3.gif'
                self.shape(self.s)
            elif self.s == 'stick-L3.gif' and counter%10 == 0:
                self.s = 'stick-L1.gif'
                self.shape(self.s)

        elif player.dx > 0:
            if self.s == 'stick-R1.gif' and counter%10 == 0:
                self.s = 'stick-R2.gif'
                self.shape(self.s)
            elif self.s == 'stick-R2.gif' and counter%10 == 0:
                self.s = 'stick-R3.gif'
                self.shape(self.s)
            elif self.s == 'stick-R3.gif' and counter%10 == 0:
                self.s = 'stick-R1.gif'
                self.shape(self.s)

        if self.flat == True:
           
            if counter%130 == 0:
                self.flat = False
                self.shape('stick-L1.gif')
                
             

def within_platform(player, platform): 
    if platform.xcor()-platform.width <= player.xcor() <= platform.xcor()+platform.width:
        if platform.ycor()-10 <= player.ycor() <= platform.ycor()+10:
            return True

def within_platform_x(player,platform):
    if platform.xcor()-platform.width <= player.xcor() <= platform.xcor()+platform.width:
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
    player.animate()
    if player.distance(door)<30:
        door.shape('door2.gif')
        game_over = True


win.update()

