def checkIfCorrectGuess(alphabet_choosen, CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List):
    # Get all the Pending set of Alphabets
    pending_alphabets = set(CityToGuess_Keyword_List) - set(list(filter((True).__ne__, PlayerGuessedCorrectAlphabet_List)))

    if alphabet_choosen in pending_alphabets:
        return True
    else:
        return False

def CheckIfGameIsOver(PendingGuess, CityToGuess_Keyword_List, PlayerGuessedCorrectAlphabet_List):
    if CityToGuess_Keyword_List == PlayerGuessedCorrectAlphabet_List:
        # Player Won and Game Over
        return False, True
    else:
        if PendingGuess == 0:
            # Player Loose and Game Over
            return False, False
        else:
            # Game is still active
            return True, False