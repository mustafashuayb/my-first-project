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
        self.canvas.move(self.id, 245, 100)
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

# Main game loop
while True: 
    ball.draw() 
    tk.update_idletasks() 
    tk.update() 
    time.sleep(0.01)