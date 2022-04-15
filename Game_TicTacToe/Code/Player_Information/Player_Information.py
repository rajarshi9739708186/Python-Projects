def setPlayerDetails(PlayerDetails, Player_1_name, Player_2_name):
    # Set Name
    PlayerDetails[1]["Name"] = Player_1_name
    PlayerDetails[2]["Name"] = Player_2_name

    # Set Tic Tac Toe Character
    PlayerDetails[1]["Symbol"] = "X"
    PlayerDetails[2]["Symbol"] = "O"

    # Allocation
    PlayerDetails[1]["Allocation"] = [False] * 9
    PlayerDetails[2]["Allocation"] = [False] * 9

    # Turn
    PlayerDetails[1]["Turn"] = 0
    PlayerDetails[2]["Turn"] = 0

    return PlayerDetails

def updatePlayerAllocation(PlayerDetails, Player, Player_pos):
    PlayerDetails[Player]["Allocation"][Player_pos-1] = True
    PlayerDetails[Player]["Turn"] += 1

    return PlayerDetails