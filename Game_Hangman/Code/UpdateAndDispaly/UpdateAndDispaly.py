from tkinter import *

def updatePendingGuess(PendingGuess, PendingGuess_Label):
    PendingGuess_Label.config(text=f"Pending Guess : {PendingGuess}")

def updateClue(CountryForClue, CountryClue_Label):
    CountryClue_Label.config(text=f"Country : {CountryForClue}")

def updateGuessStatus(GuessIsCorrect, AplphabetGuessStatus_Label):
    if GuessIsCorrect:
        AplphabetGuessStatus_Label.config(text="Correct Guess", fg="green")
    else:
        AplphabetGuessStatus_Label.config(text="Wrong Guess", fg="red")

def updateWinningMessage(Player_Won, WinningMessage_Label):
    if Player_Won:
        WinningMessage_Label.config(text="You Won !", fg="green")
    else:
        WinningMessage_Label.config(text="You Loose !", fg="red")

def updateWordList(PlayerGuessedCorrectAlphabet_List, Frame_5):
    col = 0

    for alphabet in PlayerGuessedCorrectAlphabet_List:
        if alphabet != None:
            if alphabet == " ":
                Label(Frame_5, text=" ", padx=10, font="Verdana 8 bold").grid(row=0, column=col)
                Label(Frame_5, text=" ", padx=10, font="Verdana 8 bold").grid(row=1, column=col)
            else:
                Label(Frame_5, text=alphabet, padx=10, font="Verdana 8 bold").grid(row=0, column=col)
                Label(Frame_5, text="_", padx=10, font="Verdana 8 bold").grid(row=1, column=col)
        else:
            Label(Frame_5, text=" ", padx=10, font="Verdana 8 bold").grid(row=0, column=col)
            Label(Frame_5, text="_", padx=10, font="Verdana 8 bold").grid(row=1, column=col)
        col += 1
