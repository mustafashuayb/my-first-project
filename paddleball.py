from tkinter import * 
import random 
import time
from turtle import pos

 # Ball Class
class Ball: 
    # Creating Canvas, Color and Ball (and now paddle)
    def __init__(self, canvas, paddle, color): 
        self.canvas = canvas 
        self.paddle = paddle

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) 
        ## Randomly Choosing the Starting X and Y Position of the Ball
        start_x = random.randrange(50, 450)
        start_y = random.randrange(50, 200)
        self.canvas.move(self.id, start_x, start_y)

        # Randomly Choosing the Starting X Direction of the Ball
        starts = [-3, -2, -1, 1, 2, 3] 
        self.x = random.choice(starts)
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
    
    def hit_paddle(self, pos): 
        paddle_pos = self.canvas.coords(self.paddle.id) 
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]: 
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]: 
                return True 
        return False
        
    def draw(self):
        # Moving the Ball in the X and Y Direction 
        self.canvas.move(self.id, self.x, self.y) 
        pos = self.canvas.coords(self.id)

        # Bouncing the Ball if it Hits the Top of the Canvas
        if pos[1] <= 0: 
            self.y = 1
        # Bouncing the Ball if it Hits the Bottom of the Canvas      
        if pos[3] >= self.canvas_height: 
            self.hit_bottom = True
            
        # Bouncing the Ball if it Hits the Left or Right of the Canvas    
        if pos[0] <= 0 or pos[2] >= self.canvas_width: 
            self.x = self.x * -1
        
        # Bouncing the Ball if it Hits the Paddle
        if self.hit_paddle(pos) == True:
            self.y *= -1

    ## Changes the fill color of the ball to the color passed in the parameter
    def change_color(self, color):
        self.canvas.itemconfig(self.id, fill=color)

# Paddle Class
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        # Creating the Paddle and Placing it at the Bottom of the Canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        ## Variable to Check if the Game has Started Yet
        self.game_started = False

        # Binding the Left and Right Arrow Keys to the turn_left and turn_right Methods
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

        ## Binding the Left Mouse Button to the start_game Method
        self.canvas.bind_all('<Button-1>', self.start_game)

    ## When the Left Mouse Button is Clicked, the Game Starts
    def start_game(self, evt):
        self.game_started = True

    # When the Left Arrow Key is Pressed, the turn_left Method is Called and the X Direction of the Paddle is Set to -2   
    def turn_left(self, evt): 
        self.x = -2

    # When the Right Arrow Key is Pressed, the turn_right Method is Called and the X Direction of the Paddle is Set to 2 
    def turn_right(self, evt): 
        self.x = 2
    # Moving the Paddle in the X Direction and Bouncing it if it Hits the Left or Right of the Canvas
    def draw(self): 
            self.canvas.move(self.id, self.x, 0) 
            pos = self.canvas.coords(self.id) 
            if pos[0] <= 0 or pos[2] >= self.canvas_width: 
                self.x = 0

# Tkinter Window 
tk = Tk()
tk.configure(bg="Black")
tk.title('Bounce Game') 
tk.resizable(0, 0) 
tk.wm_attributes('-topmost', 1)

## Added bg="Black" to make the background of the window black instead of white.
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0, bg="Black")

canvas.pack() 
tk.update() 


# Creating the Paddle
paddle = Paddle(canvas, 'white')

# Creating the Ball 
## Changed Ball color from red to blue
ball = Ball(canvas, paddle, 'blue') 

## List of Colors to Change the Ball to:
colors = [
    "indianred", "lightcoral", "salmon", "darksalmon", "lightsalmon",
    "crimson", "red", "firebrick", "darkred", "pink", "lightpink",
    "hotpink", "deeppink", "mediumvioletred", "palevioletred",

    "coral", "tomato", "orangered", "darkorange", "orange",

    "gold", "yellow", "lightyellow", "lemonchiffon",
    "lightgoldenrodyellow", "papayawhip", "moccasin", "peachpuff",
    "palegoldenrod", "khaki", "darkkhaki",

    "green", "lawngreen", "chartreuse", "lime", "limegreen",
    "palegreen", "lightgreen", "mediumspringgreen", "springgreen",
    "mediumseagreen", "seagreen", "forestgreen", "darkgreen",
    "yellowgreen", "olivedrab", "olive", "darkolivegreen",
    "mediumaquamarine", "darkseagreen", "lightseagreen", "darkcyan",
    "teal",

    "aqua", "cyan", "lightcyan", "paleturquoise", "aquamarine",
    "turquoise", "mediumturquoise", "darkturquoise", "cadetblue",
    "steelblue", "lightsteelblue", "powderblue", "lightblue",
    "skyblue", "lightskyblue", "deepskyblue", "dodgerblue",
    "cornflowerblue", "royalblue", "blue", "mediumblue",
    "darkblue", "navy", "midnightblue",

    "lavender", "thistle", "plum", "violet", "orchid",
    "fuchsia", "magenta", "mediumorchid", "mediumpurple",
    "blueviolet", "darkviolet", "darkorchid", "darkmagenta",
    "purple", "indigo", "slateblue", "darkslateblue",
    "mediumslateblue",

    "white", "snow", "honeydew", "mintcream", "azure",
    "aliceblue", "ghostwhite", "whitesmoke", "seashell",
    "beige", "oldlace", "floralwhite", "ivory", "antiquewhite",
    "linen", "lavenderblush", "mistyrose", "gainsboro",
    "lightgray", "silver", "darkgray", "gray", "dimgray",
    "black",

    "cornsilk", "bisque", "blanchedalmond", "navajowhite",
    "wheat", "burlywood", "tan", "rosybrown", "sandybrown",
    "goldenrod", "darkgoldenrod", "peru", "chocolate",
    "saddlebrown", "sienna", "brown", "maroon"
]
# The colors list contains a wide variety of color options for the ball.

## Game Over Text
game_over_text = canvas.create_text(250, 200, text="Game Over", fill="white", font=("Arial", 30))

## Keeps the text hidden until the game is actually over
canvas.itemconfig(game_over_text, state='hidden')

# Game Over Delay
game_over_delay = 0

# Main game loop
while True:
    ## If the Game has Started and the Ball has not Hit the Bottom of the Canvas,
    ## Draw the Paddle and the Ball, and Randomly Change the Color of the Ball
    if paddle.game_started == True and ball.hit_bottom == False:
        paddle.draw() 
        ball.draw()

        # Change the color of the ball every 2 milliseconds to a random color from the colors list (line 119-161)
        if random.randint(1, 2) == 1:
            ball.change_color(random.choice(colors))

    # If the ball hits the bottom it should start adding one every loop to the game_over_delay variable.
    if ball.hit_bottom == True:
        game_over_delay += 1

    # Once the game_over_delay variable reaches 100 (around 1 second),
    # the "Game Over" text should be displayed on the canvas.
    if game_over_delay >= 100:
        canvas.itemconfig(game_over_text, state='normal')

    tk.update_idletasks() 
    tk.update() 
    time.sleep(0.01)