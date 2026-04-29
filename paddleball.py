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
        
    # Moving the Ball     
    def draw(self): 
        self.canvas.move(self.id, 0, -1) 

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