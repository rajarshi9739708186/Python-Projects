from tkinter import *
import random

root = Tk()
root.geometry("200x200")
root.resizable(0, 0)
root.title("Dice Roll")

def generateNumber():
    # One Random Number will be generated in between 1 to 6
    random_number = random.randint(1, 6)
    print(random_number)
    drawCircle(random_number)

frame_1 = Frame()
frame_1.grid(row=0, column=0)
frame_2 = Frame()
frame_2.grid(row=1, column=0)

# Create Button to Press
Button(frame_1, text='Roll', bg="cyan", padx=30, font="verdana 10 bold", command=generateNumber).grid(pady=10)

# Create a canvas area
Frame_Canvas = Canvas(frame_2, width=200, height=100)
Frame_Canvas.grid()

def drawRectangle():
    Frame_Canvas.delete(ALL) # Delete everything if anything is in Canvas Area
    Frame_Canvas.create_rectangle(70, 20, 130, 80, fill="green", outline = 'green') # Create Rectangle over Canvas

def drawCircle(number):
    drawRectangle()

    if number ==1:
        Frame_Canvas.create_text(100, 50, text="o")
    if number ==2:
        Frame_Canvas.create_text(80, 50, text="o")
        Frame_Canvas.create_text(120, 50, text="o")
    if number ==3:
        Frame_Canvas.create_text(80, 30, text="o")
        Frame_Canvas.create_text(100, 50, text="o")
        Frame_Canvas.create_text(120, 70, text="o")
    if number ==4:
        Frame_Canvas.create_text(80, 30, text="o")
        Frame_Canvas.create_text(120, 30, text="o")
        Frame_Canvas.create_text(80, 70, text="o")
        Frame_Canvas.create_text(120, 70, text="o")
    if number ==5:
        Frame_Canvas.create_text(80, 30, text="o")
        Frame_Canvas.create_text(120, 30, text="o")
        Frame_Canvas.create_text(100, 50, text="o")
        Frame_Canvas.create_text(80, 70, text="o")
        Frame_Canvas.create_text(120, 70, text="o")
    if number ==6:
        Frame_Canvas.create_text(80, 30, text="o")
        Frame_Canvas.create_text(120, 30, text="o")
        Frame_Canvas.create_text(80, 50, text="o")
        Frame_Canvas.create_text(120, 50, text="o")
        Frame_Canvas.create_text(80, 70, text="o")
        Frame_Canvas.create_text(120, 70, text="o")


drawRectangle()
root.mainloop()