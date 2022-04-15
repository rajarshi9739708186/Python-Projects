from tkinter import *
import tkinter.messagebox as tmsg
import random

from Player_Information import Player_Information
from Game_Decision_Making import Game_Decision_Making
from Computer_Movement import Computer_Movement

root = Tk()
root.geometry("400x400")
root.title("Tic Tac Toe")
root.resizable(0,0)

OpponentIsHuman = True
PlayerDetails = {1:{}, 2:{}}
Current_Active_Player = 0
TicTacToePad_ButtonList = []
Current_player_Won = False
Game_is_not_Over = True
Game_Total_Turn = 0

def clearWindow():
    widget_list = root.grid_slaves()
    for widget in widget_list:
        widget.destroy()

def Home_Page():
    clearWindow()
    global OpponentIsHuman
    global PlayerDetails
    global Current_Active_Player
    global TicTacToePad_ButtonList
    global Current_player_Won
    global Game_is_not_Over
    global Game_Total_Turn

    # Reset all Data
    OpponentIsHuman = True
    PlayerDetails = {1: {}, 2: {}}
    Current_Active_Player = 0
    TicTacToePad_ButtonList = []
    Current_player_Won = False
    Game_is_not_Over = True
    Game_Total_Turn = 0

    Frame_1 = Frame()
    Frame_1.grid(row=0, column=0)
    Frame_2 = Frame()
    Frame_2.grid(row=1, column=0)

    Label(Frame_1, text="Tic Tac Toe", padx=100, pady=25, fg="red", font="Verdana 20 bold").grid(row=0, column=0)
    Button(Frame_2, text="vs Human", padx=20, bg="cyan", font="Verdana 10 bold", command=lambda: askUserName_Page(True)).grid(padx=30, row=0, column=0)
    Button(Frame_2, text="vs Computer", padx=20, bg="cyan", font="Verdana 10 bold", command=lambda: askUserName_Page(False)).grid(padx=30, row=0, column=1)

def askUserName_Page(HumanVsHuman):
    clearWindow()
    global OpponentIsHuman
    OpponentIsHuman = HumanVsHuman

    Frame_1 = Frame()
    Frame_1.grid(row=0, column=0)
    Frame_2 = Frame()
    Frame_2.grid(row=1, column=0)

    if OpponentIsHuman:
        Label(Frame_1, text="First Player Name", padx=5, pady=10, font="Verdana 10 bold").grid(row=0, column=0)
        Player_1 = StringVar()
        Entry(Frame_1, width=25, textvariable=Player_1).grid(row=0, column=1)

        Label(Frame_1, text="Second Player Name", padx=5, pady=10, font="Verdana 10 bold").grid(row=1, column=0)
        Player_2 = StringVar()
        Entry(Frame_1, width=25, textvariable=Player_2).grid(row=1, column=1)

        Button(Frame_2, text="Start Game", padx=20, bg="cyan", font="Verdana 10 bold", command=lambda: validatePlayer(Player_1.get(), Player_2.get())).grid(padx=30, row=0, column=0)
    else:
        Label(Frame_1, text="Player Name", padx=5, pady=10, font="Verdana 10 bold").grid(row=0, column=0)
        Player_1 = StringVar()
        Entry(Frame_1, width=25, textvariable=Player_1).grid(row=0, column=1)

        Button(Frame_2, text="Start Game", padx=20, bg="cyan", font="Verdana 10 bold", command=lambda: validatePlayer(Player_1.get(), "Computer")).grid(padx=30, row=0, column=0)

def validatePlayer(Player_1, Player_2):
    global PlayerDetails

    if Player_1 == "":
        tmsg.showinfo("Error", "Please enter Player 1 name")

    if Player_2 == "":
        tmsg.showinfo("Error", "Please enter Player 2 name")

    if len(Player_1) > 10:
        Player_1 = Player_1[0:10]
    if len(Player_2) > 10:
        Player_2 = Player_2[0:10]

    # Initially set Information of Players
    PlayerDetails = Player_Information.setPlayerDetails(PlayerDetails, Player_1, Player_2)
    GamePage()

def GamePage():
    clearWindow()
    global PlayerDetails
    global Current_Active_Player
    global OpponentIsHuman

    Frame_1 = Frame()
    Frame_1.grid(row=0, column=0)
    Frame_2 = Frame()
    Frame_2.grid(row=1, column=0)
    Frame_3 = Frame()
    Frame_3.grid(row=2, column=0)
    Frame_4 = Frame()
    Frame_4.grid(row=3, column=0)

    # Display which player have which symbol
    for list_index, player in enumerate(list(PlayerDetails.keys())):
        Label(Frame_1, text="                               ").grid(row=list_index, column=0)
        Label(Frame_1, text=f"{PlayerDetails[player]['Name']} : {PlayerDetails[player]['Symbol']}", padx=10, pady=5, font="Verdana 10 bold").grid(row=list_index, column=1)

    # Select a Random Player who will start the game
    Current_Active_Player = random.randint(1,2)
    Label(Frame_2, text="                               ").grid(row=0, column=0)
    Current_Active_Player_Display_Label = Label(Frame_2, text=f"{PlayerDetails[Current_Active_Player]['Name']}'s turn", bg="cyan", padx=10, pady=5, font="Verdana 10 bold")
    Current_Active_Player_Display_Label.grid(pady=10, row=0, column=1)

    # Draw Tic Tac Toe Pad
    drawTicTacToePad(Frame_3, Current_Active_Player_Display_Label, Frame_4)

    # If First Turn for Computer
    if OpponentIsHuman == False:
        if PlayerDetails[Current_Active_Player]['Name'] == "Computer":
            Computer_Selected_Position = Computer_Movement.MakeDecision(PlayerDetails, Current_Active_Player)
            updateGame(Computer_Selected_Position, Current_Active_Player_Display_Label, Frame_4)

def drawTicTacToePad(Frame_3, Current_Active_Player_Display_Label, Frame_4):
    global TicTacToePad_ButtonList
    Label(Frame_3, text="                               ").grid(row=0, column=0)

    Pad_1 = Button(Frame_3, text=" ", bg="yellow", fg="black", width=3, height=1, font=('Helvetica', '20'),command=lambda: updateGame(1, Current_Active_Player_Display_Label, Frame_4))
    Pad_1.grid(row=0, column=1)
    Pad_2 = Button(Frame_3, text=" ", bg="yellow", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: updateGame(2, Current_Active_Player_Display_Label, Frame_4))
    Pad_2.grid(row=0, column=2)
    Pad_3 = Button(Frame_3, text=" ", bg="yellow", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: updateGame(3, Current_Active_Player_Display_Label, Frame_4))
    Pad_3.grid(row=0, column=3)

    Pad_4 = Button(Frame_3, text=" ", bg="yellow", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: updateGame(4, Current_Active_Player_Display_Label, Frame_4))
    Pad_4.grid(row=1, column=1)
    Pad_5 = Button(Frame_3, text=" ", bg="yellow", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: updateGame(5, Current_Active_Player_Display_Label, Frame_4))
    Pad_5.grid(row=1, column=2)
    Pad_6 = Button(Frame_3, text=" ", bg="yellow", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: updateGame(6, Current_Active_Player_Display_Label, Frame_4))
    Pad_6.grid(row=1, column=3)

    Pad_7 = Button(Frame_3, text=" ", bg="yellow", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: updateGame(7, Current_Active_Player_Display_Label, Frame_4))
    Pad_7.grid(row=2, column=1)
    Pad_8 = Button(Frame_3, text=" ", bg="yellow", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: updateGame(8, Current_Active_Player_Display_Label, Frame_4))
    Pad_8.grid(row=2, column=2)
    Pad_9 = Button(Frame_3, text=" ", bg="yellow", fg="black", width=3, height=1, font=('Helvetica', '20'), command=lambda: updateGame(9, Current_Active_Player_Display_Label, Frame_4))
    Pad_9.grid(row=2, column=3)

    TicTacToePad_ButtonList = [Pad_1, Pad_2, Pad_3, Pad_4, Pad_5, Pad_6, Pad_7, Pad_8, Pad_9]

def updateGame(This_Pad_Clicked, Current_Active_Player_Display_Label, Frame_4):
    global PlayerDetails
    global Current_Active_Player
    global TicTacToePad_ButtonList
    global Current_player_Won
    global Game_is_not_Over
    global Game_Total_Turn
    global OpponentIsHuman

    # validate that, whichever pad selected that was already selected or not
    # If selected, no need to change any state
    wrong_move = PlayerDetails[1]["Allocation"][This_Pad_Clicked-1] or PlayerDetails[2]["Allocation"][This_Pad_Clicked-1]

    if not wrong_move:
        # Until Game is Active
        if Game_is_not_Over:
            # Increment Game Turn
            Game_Total_Turn += 1

            # Mark symbol on the pad
            TicTacToePad_ButtonList[This_Pad_Clicked-1]["text"] = PlayerDetails[Current_Active_Player]["Symbol"]

            # Update the position for current played. Which one player selected
            PlayerDetails = Player_Information.updatePlayerAllocation(PlayerDetails, Current_Active_Player, This_Pad_Clicked)

            # If Players Turn greater than or equal to 3
            # We can start checking if Player has won
            if PlayerDetails[Current_Active_Player]["Turn"] >= 3:
                Current_player_Won = Game_Decision_Making.ifPlayerWon(PlayerDetails[Current_Active_Player]["Allocation"])

            if Current_player_Won:
                # Finish the game
                Game_is_not_Over = False
                Current_Active_Player_Display_Label.config(text=f"Congratulations. {PlayerDetails[Current_Active_Player]['Name']} won", bg="green")
                Label(Frame_4, text="                               ").grid(row=0, column=0)
                Button(Frame_4, text="Play Again", padx=20, bg="cyan", font="Verdana 10 bold", command=lambda: Home_Page()).grid(pady=10, row=0, column=1)
            else:
                # Check If Total turn Reaches 9
                # And Nobody Won
                # Finish the Game
                if Game_Total_Turn==9 and Game_is_not_Over:
                    Game_is_not_Over = False
                    Current_Active_Player_Display_Label.config(text=f"Nobody won", bg="red")
                    Label(Frame_4, text="                               ").grid(row=0, column=0)
                    Button(Frame_4, text="Play Again", padx=20, bg="cyan", font="Verdana 10 bold", command=lambda: Home_Page()).grid(pady=10, row=0, column=1)
                else:
                    # Alter Active player for Next turn
                    if Current_Active_Player == 1:
                        Current_Active_Player = 2
                    else:
                        Current_Active_Player = 1

                    # Set the information regarding whose turn
                    Current_Active_Player_Display_Label["text"] = f"{PlayerDetails[Current_Active_Player]['Name']}'s turn"

                    # If Computer's Turn
                    if OpponentIsHuman == False:
                        if PlayerDetails[Current_Active_Player]['Name'] == "Computer":
                            Computer_Selected_Position = Computer_Movement.MakeDecision(PlayerDetails, Current_Active_Player)
                            updateGame(Computer_Selected_Position, Current_Active_Player_Display_Label, Frame_4)


Home_Page()
root.mainloop()