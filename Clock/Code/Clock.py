from tkinter import *
from time import strftime

root = Tk()
root.resizable(0, 0)
root.title("Clock")

def display_time():
    current_time = strftime("%H:%M:%S %p") # Get Current System Time
    display_label.config(text=current_time) # Update Current time
    display_label.after(1000, display_time) # After 1 second call itself and update new time; 1000 ms => 1Second

display_label = Label(root, font=("ds-digital", 80), bg="black", fg="cyan")
display_label.grid()

display_time() # Call time function

root.mainloop()