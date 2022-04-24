from tkinter import *
import random

from City_vs_Country import City_vs_Country
from UpdateAndDispaly import UpdateAndDispaly
from DecisionMaking import DecisionMaking
from DrawHangman import DrawHangman

root = Tk()
root.geometry("600x600")
root.title("Hangman")
root.resizable(0,0)

City_vs_Country_Dict = City_vs_Country.words()
City_List = list(City_vs_Country_Dict.keys())
GameIsNotOver = True
PendingGuess = 0

# To Display Pending Guess
PendingGuess_Label = ""
# To Display Key Board
Frame_3 = ""
# To Display Guess is Right or Wrong
AplphabetGuessStatus_Label = ""
# To Update Word Construction
Frame_5 = ""
# To Update Clue (Country Name)
CountryClue_Label = ""
# To Draw Hangman
HangamanCanvas = ""
# To Display Winning Message
WinningMessage_Label = ""
# To Display Play Again
Frame_9 = ""

def clearWindow():
    widget_list = root.grid_slaves()
    for widget in widget_list:
        widget.destroy()

def Home_Page():
    clearWindow()

    Label(text="HANGMAN", fg="red", padx=120, font="Verdana 20 bold").grid(pady=10, row=0, column=0)
    Label(text="Game Objective : Guess correct CITY name", padx=120, font="Verdana 10 bold").grid(pady=10, row=1, column=0)
    Button(text="Start Game", padx=5, pady=5, bg="cyan", font="Verdana 10 bold",command=lambda: Game_Page_Initializing()).grid(pady=10, row=2, column=0)

def Game_Page_Initializing():
    clearWindow()
    global GameIsNotOver
    global PendingGuess
    global PendingGuess_Label
    global CountryClue_Label
    global WinningMessage_Label
    global AplphabetGuessStatus_Label
    global HangamanCanvas
    global Frame_3
    global Frame_5
    global Frame_9

    # Initialize Frames

    # To Display Pending Guess
    Frame_1 = Frame()
    Frame_1.grid(row=0, column=0)
    PendingGuess_Label = Label(Frame_1, text="", fg="purple", font="Verdana 10 bold")
    PendingGuess_Label.grid(pady=5)

    # To display What to do
    Frame_2 = Frame()
    Frame_2.grid(row=1, column=0)
    Label(Frame_2, text="guess alphabets using below keypad", font="Verdana 10 bold").grid(pady=5)

    # To Display Key Board
    Frame_3 = Frame()
    Frame_3.grid(row=2, column=0)

    # To Display Guess is Right or Wrong
    Frame_4 = Frame()
    Frame_4.grid(row=3, column=0)
    AplphabetGuessStatus_Label = Label(Frame_4, text="", font="Verdana 10 bold")
    AplphabetGuessStatus_Label.grid(pady=5)

    # To Update Word Construction
    Frame_5 = Frame()
    Frame_5.grid(row=4, column=0)

    # To Update Clue (Country Name)
    Frame_6 = Frame()
    Frame_6.grid(row=5, column=0)
    CountryClue_Label = Label(Frame_6, text="", font="Verdana 10 bold")
    CountryClue_Label.grid(pady=5)

    # To Draw Hangman
    Frame_7 = Frame()
    Frame_7.grid(row=6, column=0)
    HangamanCanvas = Canvas(Frame_7, width=200, height=200)
    HangamanCanvas.grid(pady=5)

    # To Display Winning Message
    Frame_8 = Frame()
    Frame_8.grid(row=7, column=0)
    WinningMessage_Label = Label(Frame_8, text="", font="Verdana 10 bold")
    WinningMessage_Label.grid(pady=5)

    # To Display Play Again
    Frame_9 = Frame()
    Frame_9.grid(row=8, column=0)

    # Initialize Game Properties

    # Flag to Decide if Game is Over or Not
    GameIsNotOver = True
    # Maximum 10 Guesses are allowed
    PendingGuess = 10
    # Choose a random City
    CityToGuess_Keyword_List, CountryForClue, PlayerGuessedCorrectAlphabet_List = getRandomCity()

    updateInformationForFirstTime(CityToGuess_Keyword_List, CountryForClue, PlayerGuessedCorrectAlphabet_List)

def getRandomCity():
    global City_vs_Country_Dict
    global City_List

    # Selecy a Random City
    City = random.choice(City_List)
    print(City)
    Country = City_vs_Country_Dict[City]

    # Delete selected City from list so that in next turn this city can't be selected
    del City_List[City_List.index(City)]

    # City Keywords
    City_Keyword_list = list(City)
    # Random Alphabet Choosen for First Time
    Initial_Random_Alphabet_Choosen = random.choice(list(filter((" ").__ne__, City_Keyword_list)))

    # Alphabets guessed correctly
    # If Spaces are vavailable, That will be considered already guessed
    # Initial Random Alphabet will be considered that already Guessed
    # Rest will be Supposed to be guessed
    GuessedAlphabet_List = []
    for alphabet in City_Keyword_list:
        if alphabet == " ":
            GuessedAlphabet_List.append(" ")
        elif alphabet == Initial_Random_Alphabet_Choosen:
            GuessedAlphabet_List.append(Initial_Random_Alphabet_Choosen)
        else:
            GuessedAlphabet_List.append(None)

    return City_Keyword_list, Country, GuessedAlphabet_List

def updateInformationForFirstTime(CityToGuess_Keyword_List, CountryForClue, PlayerGuessedCorrectAlphabet_List):
    global PendingGuess
    global PendingGuess_Label
    global CountryClue_Label
    global Frame_5

    # Update Pending Guess
    UpdateAndDispaly.updatePendingGuess(PendingGuess, PendingGuess_Label)

    # Draw Keyboard
    draw_keyboard(CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)

    # Update Correct Guessed Alphabet and Blanks
    UpdateAndDispaly.updateWordList(PlayerGuessedCorrectAlphabet_List, Frame_5)

    # Update Country as Clue
    UpdateAndDispaly.updateClue(CountryForClue, CountryClue_Label)

def draw_keyboard(CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List):
    global Frame_3
    Button(Frame_3, text="a", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("a", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=0,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="b", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("b", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=1,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="c", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("c", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=2,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="d", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("d", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=3,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="e", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("e", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=4,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="f", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("f", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=5,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="g", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("g", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=6,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="h", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("h", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=7,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="i", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("i", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=8,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="j", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("j", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=9,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="k", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("k", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=10,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="l", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("l", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=11,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="m", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("m", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=0,
                                                                                                                  column=12,
                                                                                                                  padx=2,
                                                                                                                  pady=2)
    Button(Frame_3, text="n", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("n", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=0)
    Button(Frame_3, text="o", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("o", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=1)
    Button(Frame_3, text="p", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("p", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=2)
    Button(Frame_3, text="q", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("q", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=3)
    Button(Frame_3, text="r", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("r", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=4)
    Button(Frame_3, text="s", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("s", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=5)
    Button(Frame_3, text="t", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("t", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=6)
    Button(Frame_3, text="u", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("u", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=7)
    Button(Frame_3, text="v", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("v", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=8)
    Button(Frame_3, text="w", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("w", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=9)
    Button(Frame_3, text="x", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("x", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=10)
    Button(Frame_3, text="y", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("y", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=11)
    Button(Frame_3, text="z", bg="yellow", fg="Black", width=2, height=1, font=('Helvetica', '20'),
           command=lambda: guess_alphabet("z", CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)).grid(row=1,
                                                                                                                  column=12)
def guess_alphabet(alphabet_choosen, CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List):
    global GameIsNotOver
    global PendingGuess
    global AplphabetGuessStatus_Label
    global WinningMessage_Label
    global HangamanCanvas
    global Frame_5
    global Frame_9

    # Game is Active
    if GameIsNotOver:
        # Check if the guessed alphabet is from the pending alphabets
        GuessIsCorrect = DecisionMaking.checkIfCorrectGuess(alphabet_choosen, CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)

        # Display Guess Status
        UpdateAndDispaly.updateGuessStatus(GuessIsCorrect, AplphabetGuessStatus_Label)

        if GuessIsCorrect:
            # Display that Guess is Correct
            UpdateAndDispaly.updateGuessStatus(GuessIsCorrect, AplphabetGuessStatus_Label)
            # Update Player Guessed Aplhabet List
            PlayerGuessedCorrectAlphabet_List = updatePlayerGuessedCorrectAlphabet_List(alphabet_choosen, CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)
            # Update Correct Guessed Alphabet and Blanks
            UpdateAndDispaly.updateWordList(PlayerGuessedCorrectAlphabet_List, Frame_5)
        else:
            # If Guess is not correct
            # Reduce Pending Guess

            # Update and Display Pending Guess
            PendingGuess -= 1
            UpdateAndDispaly.updatePendingGuess(PendingGuess, PendingGuess_Label)
            # Display Guess Status
            UpdateAndDispaly.updateGuessStatus(GuessIsCorrect, AplphabetGuessStatus_Label)
            # Draw Hangman
            DrawHangman.Draw(PendingGuess,HangamanCanvas)

        # Check If Game is Over
        GameIsNotOver, Player_Won = DecisionMaking.CheckIfGameIsOver(PendingGuess, CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List)

        # If Game is Over
        if not GameIsNotOver:
            # Display Game Status
            UpdateAndDispaly.updateWinningMessage(Player_Won, WinningMessage_Label)
            # Ask Player If He want to Play Again
            Button(Frame_9, text="Play Again", padx=5, pady=5, bg="cyan", font="Verdana 10 bold",command=lambda: Game_Page_Initializing()).grid(pady=10)

def updatePlayerGuessedCorrectAlphabet_List(alphabet_choosen, CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List):
    # Whichever Alphabets are pending
    # Check those position
    # If those position needs choosen Alphabets
    # Update those position with Choosen alphabets
    for index, value in enumerate(CityToGuess_Keyword_List):
        if value == alphabet_choosen:
            PlayerGuessedCorrectAlphabet_List[index] = alphabet_choosen
    return PlayerGuessedCorrectAlphabet_List





Home_Page()
root.mainloop()