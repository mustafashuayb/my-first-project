# Paddle Ball Game

# If you see me use "##" it means that i am doing a programming puzzle.

# Libaries
from tkinter import * 
import random 
import time

 # Ball Class
class Ball: 
    # Creating Canvas, Color and Ball
    def __init__(self, canvas, color): 
        self.canvas = canvas 
    
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) 
        ## Randomly Choosing the Starting X and Y Position of the Ball Between 50 and 450 for X and 50 and 200 for Y
        start_x = random.randrange(50, 450)
        start_y = random.randrange(50, 200)
        self.canvas.move(self.id, start_x, start_y)

        # Randomly Choosing the Starting X Direction of the Ball
        starts = [-3, -2, -1, 1, 2, 3] 
        self.x = random.choice(starts)
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        
    def draw(self):
        # Moving the Ball in the X and Y Direction 
        self.canvas.move(self.id, self.x, self.y) 
        pos = self.canvas.coords(self.id)

        # Bouncing the Ball if it Hits the Top or Bottom of the Canvas
        if pos[1] <= 0: 
            self.y = 1      
        if pos[3] >= self.canvas_height: 
            self.y = -1
            
        # Bouncing the Ball if it Hits the Left or Right of the Canvas    
        if pos[0] <= 0 or pos[2] >= self.canvas_width: 
            self.x = self.x * -1

    ## Changes the fill color of the ball to the color passed in the parameter
    def change_color(self, color):
        self.canvas.itemconfig(self.id, fill=color)


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

# Creating the Ball 
## Changed Ball color from red to blue
ball = Ball(canvas, 'blue') 

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
# umm I think i added a bit too much..

# Main game loop
while True: 
    ball.draw()
    ## Randomly Change the Color of the Ball Every 2 Frames so it Doesnt Look Crazy 
    if random.randint(1, 2) == 1:
        ball.change_color(random.choice(colors))

    tk.update_idletasks() 
    tk.update() 
    time.sleep(0.01)