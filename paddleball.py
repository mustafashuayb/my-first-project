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
        # Making The Ball Bounce
        self.x = 0 
        self.y = -1 
        self.canvas_height = self.canvas.winfo_height()
        
    # Moving/Bouncing the Ball if it Hits the Top or Bottom of the Canvas     
    def draw(self): 
        self.canvas.move(self.id, self.x, self.y) 
        pos = self.canvas.coords(self.id) 
        if pos[1] <= 0: 
            self.y = 1  
        if pos[3] >= self.canvas_height: 
            self.y = -1


# Tkinter Window 
tk = Tk() 
tk.title('Bounce Game') 
tk.resizable(0, 0) 
tk.wm_attributes('-topmost', 1) 
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0) 
canvas.pack() 
tk.update() 

# Creating the Ball 
ball = Ball(canvas, 'red') 

# Main game loop
while True: 
    ball.draw() 
    tk.update_idletasks() 
    tk.update() 
    time.sleep(0.01)