from tkinter import *
import tkinter.messagebox as tmsg
import random
import os
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x300")
root.title("Rock Paper Scissors")
root.resizable(0,0)

Player_Name = ""
Player_Image = ""
Computer_Image = ""
Player_Point = 0
Computer_Point = 0
GameIsNotOver = True
Image_List = [os.path.join(os.getcwd(),"Supporting_Images\\Rock.png"), os.path.join(os.getcwd(),"Supporting_Images\\Paper.png"), os.path.join(os.getcwd(),"Supporting_Images\\Scissor.png")]

def clearWindow():
    widget_list = root.grid_slaves()
    for widget in widget_list:
        widget.destroy()

def Home_Page():
    clearWindow()

    global Player_Name
    global Player_Point
    global Computer_Point
    global GameIsNotOver

    Frame_1 = Frame()
    Frame_1.grid(row=0, column=0)
    Frame_2 = Frame()
    Frame_2.grid(row=1, column=0)

    # Reset Values for Each Game
    Player_Name = ""
    Player_Point = 0
    Computer_Point = 0
    GameIsNotOver = True

    # Capture Player Name
    Label(Frame_1, text="Player Name", padx=5, pady=10, font="Verdana 10 bold").grid(row=0, column=0)
    Player = StringVar()
    Entry(Frame_1, width=25, textvariable=Player).grid(row=0, column=1)

    Button(Frame_2, text="Start Game", padx=20, bg="cyan", font="Verdana 10 bold",command=lambda: validatePlayerAndSupportingFiles(Player.get())).grid(padx=30, row=0, column=0)

def validatePlayerAndSupportingFiles(Player):
    global Player_Name

    # Must need to provide Player Name
    if Player == "":
        tmsg.showinfo("Error", "Please enter Player 1 name")
    else:
        # Supporting_Images folder must need to be present
        if not os.path.exists(os.path.join(os.getcwd(), "Supporting_Images")):
            tmsg.showinfo("Error", "Please place Supporting_Images folder at the same location")
        else:
            # All 3 Image file need to be inside Supporting_Images folder
            if (not os.path.exists(os.path.join(os.getcwd(),"Supporting_Images\\Rock.png"))) or (not os.path.exists(os.path.join(os.getcwd(),"Supporting_Images\\Paper.png"))) or (not os.path.exists(os.path.join(os.getcwd(),"Supporting_Images\\Scissor.png"))):
                tmsg.showinfo("Error", "All 3 images are not placed in Supporting_Images folder")
            else:
                # Capture only First 10 Letter from Player Name if it is more than 10 Characters
                Player_Name = Player[0:10]

                Game_page()

def Game_page():
    clearWindow()

    Frame_1 = Frame()
    Frame_1.grid(row=0, column=0)
    Frame_2 = Frame()
    Frame_2.grid(row=1, column=0)
    Frame_2_1 = Frame(Frame_2)
    Frame_2_1.grid(padx=50, row=0, column=0)
    Frame_2_2 = Frame(Frame_2)
    Frame_2_2.grid(padx=50, row=0, column=1)
    Frame_3 = Frame()
    Frame_3.grid(row=2, column=0)
    Frame_4 = Frame()
    Frame_4.grid(row=3, column=0)

    # Display Player Information
    Player_Information_Label = Label(Frame_2_1, text=f"{Player_Name} : {Player_Point}", font="Verdana 8 bold")
    Player_Information_Label.grid(pady=10, row=0, column=0)

    Computer_Information_Label = Label(Frame_2_2, text=f"Computer : {Computer_Point}", font="Verdana 8 bold")
    Computer_Information_Label.grid(pady=10, row=0, column=0)

    MessageForThisRound_Label = Label(Frame_3, text=f"", fg="green", font="Verdana 10 bold")
    MessageForThisRound_Label.grid(pady=10, row=0, column=0)

    Button(Frame_1, text="Rock Paper Scissor", padx=20, bg="cyan", font="Verdana 10 bold",command=lambda: generateChoice(Frame_2_1, Frame_2_2, MessageForThisRound_Label, Player_Information_Label, Computer_Information_Label, Frame_4)).grid(pady=10, padx=10, row=0, column=0)

def generateChoice(Frame_2_1, Frame_2_2, MessageForThisRound_Label, Player_Information_Label, Computer_Information_Label, Frame_4):
    global Player_Point
    global Computer_Point
    global GameIsNotOver

    if GameIsNotOver:
        # Generate Random Choice for Player and Computer
        # 0 : Rock
        # 1 : Paper
        # 2 : Scissor
        Player_Choice = random.randint(0,2)
        Computer_Choice = random.randint(0, 2)

        # Display their choices
        displayImage(Player_Choice, Frame_2_1, Computer_Choice, Frame_2_2)

        # Game decision and points for this round
        decision_index = decisionForThisRound(Player_Choice, Computer_Choice)

        # Based on Decision for this round display messages and calculate point
        Player_Point, Computer_Point = updateMessageForThisRound(decision_index, MessageForThisRound_Label, Player_Information_Label, Computer_Information_Label, Player_Point, Computer_Point)

        # Check if Game is Over
        # While Player Point + Computer Point = 5
        # Game is over
        GameIsNotOver, Winner = checkIfGameIsOver(Player_Point, Computer_Point)

        if GameIsNotOver == False:
            # Game is Over
            # Display Winner
            MessageForThisRound_Label.config(text=f"{Winner} Win the Game", fg="red", font="Verdana 12 bold")
            Button(Frame_4, text="Play AGain", padx=20, bg="cyan", font="Verdana 10 bold", command=lambda: Home_Page()).grid(padx=30, row=0, column=0)

def displayImage(Player_Choice, Frame_2_1, Computer_Choice, Frame_2_2):
    global Player_Image
    global Computer_Image

    Player_Image = ImageTk.PhotoImage(Image.open(Image_List[Player_Choice]))
    Computer_Image = ImageTk.PhotoImage(Image.open(Image_List[Computer_Choice]))

    Label(Frame_2_1, image=Player_Image).grid(row=1, column=0)
    Label(Frame_2_2, image=Computer_Image).grid(row=1, column=0)

def decisionForThisRound(Player_Choice, Computer_Choice):
    if Player_Choice == Computer_Choice:
        return 3 # Draw for this round
    else:
        Choices = [Player_Choice, Computer_Choice]

        # Rock beats Scissor
        if 0 in Choices and 2 in Choices:
            # 0 Wins
            if Player_Choice == 0:
                return 1 # Player Wins
            else:
                return 2 # Computer Wins
        # Scissor beats Paper
        elif 2 in Choices and 1 in Choices:
            # 2 Wins
            if Player_Choice == 2:
                return 1 # Player Wins
            else:
                return 2 # Computer Wins
        # Paper beats rock
        else:
            # 1 Wins
            if Player_Choice == 1:
                return 1 # Player Wins
            else:
                return 2 # Computer Wins

def updateMessageForThisRound(decision_index, MessageForThisRound_Label, Player_Information_Label, Computer_Information_Label, Player_Point, Computer_Point):
    # This round is Draw
    if decision_index == 3:
        MessageForThisRound_Label.config(text="Nobody won in this Round")

    # Player won for this Round
    if decision_index == 1:
        MessageForThisRound_Label.config(text=f"{Player_Name} won in this Round")
        Player_Point += 1
        Player_Information_Label.config(text=f"{Player_Name} : {Player_Point}")

    # Computer won for this Round
    if decision_index == 2:
        MessageForThisRound_Label.config(text=f"Computer won in this Round")
        Computer_Point += 1
        Computer_Information_Label.config(text=f"Computer : {Computer_Point}")

    return Player_Point, Computer_Point

def checkIfGameIsOver(Player_Point, Computer_Point):
    if Player_Point+Computer_Point == 5:
        if Player_Point > Computer_Point:
            Winner = Player_Name # Player is Winner
        else:
            Winner = "Computer" # Computer is Winner

        return False, Winner
    else:
        return True, "" # Game is still Active

Home_Page()
root.mainloop()