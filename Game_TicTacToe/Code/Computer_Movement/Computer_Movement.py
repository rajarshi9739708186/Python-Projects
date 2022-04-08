import random

def MakeDecision(PlayerDetails, Current_Active_Player):
    if Current_Active_Player == 1:
        OpponentPlayer = 2
    else:
        OpponentPlayer = 1

    # Get Current Open Positions
    current_open_positions = getCurrentOpenPositions(PlayerDetails)

    # If Computer has any Possibilty to Win
    # Select that position and win
    ComputerHasPossibilityToWin, WinningPosition = playerHasPossibilityToWin(PlayerDetails, Current_Active_Player, current_open_positions)
    if ComputerHasPossibilityToWin:
        return WinningPosition
    else:
        # If Opponent has any possibilty to win
        # Block that position
        OpponentHasPossibilityToWin, WinningPosition = playerHasPossibilityToWin(PlayerDetails, OpponentPlayer, current_open_positions)
        if OpponentHasPossibilityToWin:
            return WinningPosition
        else:
            # Take Decisions
            # Which Position computer will select

            # First check If any Corner position is opened
            cornerPositions = [1, 3, 7, 9]
            availableCornerPositions = list(set(current_open_positions).intersection(set(cornerPositions)))
            if len(availableCornerPositions) > 0:
                return random.choice(availableCornerPositions)

            # If No corner position is available
            # Check if middle position is available
            if 5 in current_open_positions:
                return 5

            # If Corner and middle position is not available
            # Return Edge position
            edgePositions = [2, 4, 6, 8]
            availableedgePositions = list(set(current_open_positions).intersection(set(edgePositions)))
            if len(availableedgePositions) > 0:
                return random.choice(availableedgePositions)

def getCurrentOpenPositions(PlayerDetails):
    Allocated_Positions = []
    All_Positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for index, value in enumerate(PlayerDetails[1]["Allocation"]):
        if value == True:
            Allocated_Positions.append(index+1)
    for index, value in enumerate(PlayerDetails[2]["Allocation"]):
        if value == True:
            Allocated_Positions.append(index+1)

    return list(set(All_Positions) - set(Allocated_Positions))

def playerHasPossibilityToWin(PlayerDetails, Player, current_open_positions):
    # If any possibilty of win at First Row
    Allocation = []
    if PlayerDetails[Player]["Allocation"][0]:
        Allocation.append(1)
    if PlayerDetails[Player]["Allocation"][1]:
        Allocation.append(2)
    if PlayerDetails[Player]["Allocation"][2]:
        Allocation.append(3)

    # If two Positions are selected
    # One Left
    # Allocate That Position
    if len(Allocation) == 2:
        WinningPosition = list(set([1, 2, 3])-set(Allocation))[0]
        if WinningPosition in current_open_positions:
            return True, WinningPosition

    # If any possibilty of win at Second Row
    Allocation = []
    if PlayerDetails[Player]["Allocation"][3]:
        Allocation.append(4)
    if PlayerDetails[Player]["Allocation"][4]:
        Allocation.append(5)
    if PlayerDetails[Player]["Allocation"][5]:
        Allocation.append(6)

    # If two Positions are selected
    # One Left
    # Allocate That Position
    if len(Allocation) == 2:
        WinningPosition = list(set([4, 5, 6]) - set(Allocation))[0]
        if WinningPosition in current_open_positions:
            return True, WinningPosition

    # If any possibilty of win at Third Row
    Allocation = []
    if PlayerDetails[Player]["Allocation"][6]:
        Allocation.append(7)
    if PlayerDetails[Player]["Allocation"][7]:
        Allocation.append(8)
    if PlayerDetails[Player]["Allocation"][8]:
        Allocation.append(9)

    # If two Positions are selected
    # One Left
    # Allocate That Position
    if len(Allocation) == 2:
        WinningPosition = list(set([7, 8, 9]) - set(Allocation))[0]
        if WinningPosition in current_open_positions:
            return True, WinningPosition

    # If any possibilty of win at First Column
    Allocation = []
    if PlayerDetails[Player]["Allocation"][0]:
        Allocation.append(1)
    if PlayerDetails[Player]["Allocation"][3]:
        Allocation.append(4)
    if PlayerDetails[Player]["Allocation"][6]:
        Allocation.append(7)

    # If two Positions are selected
    # One Left
    # Allocate That Position
    if len(Allocation) == 2:
        WinningPosition = list(set([1, 4, 7]) - set(Allocation))[0]
        if WinningPosition in current_open_positions:
            return True, WinningPosition

    # If any possibilty of win at Second Column
    Allocation = []
    if PlayerDetails[Player]["Allocation"][1]:
        Allocation.append(2)
    if PlayerDetails[Player]["Allocation"][4]:
        Allocation.append(5)
    if PlayerDetails[Player]["Allocation"][7]:
        Allocation.append(8)

    # If two Positions are selected
    # One Left
    # Allocate That Position
    if len(Allocation) == 2:
        WinningPosition = list(set([2, 5, 8]) - set(Allocation))[0]
        if WinningPosition in current_open_positions:
            return True, WinningPosition

    # If any possibilty of win at Third Column
    Allocation = []
    if PlayerDetails[Player]["Allocation"][2]:
        Allocation.append(3)
    if PlayerDetails[Player]["Allocation"][5]:
        Allocation.append(6)
    if PlayerDetails[Player]["Allocation"][8]:
        Allocation.append(9)

    # If two Positions are selected
    # One Left
    # Allocate That Position
    if len(Allocation) == 2:
        WinningPosition = list(set([3, 6, 9]) - set(Allocation))[0]
        if WinningPosition in current_open_positions:
            return True, WinningPosition

    # If any possibilty of win at First Cross
    Allocation = []
    if PlayerDetails[Player]["Allocation"][0]:
        Allocation.append(1)
    if PlayerDetails[Player]["Allocation"][4]:
        Allocation.append(5)
    if PlayerDetails[Player]["Allocation"][8]:
        Allocation.append(9)

    # If two Positions are selected
    # One Left
    # Allocate That Position
    if len(Allocation) == 2:
        WinningPosition = list(set([1, 5, 9]) - set(Allocation))[0]
        if WinningPosition in current_open_positions:
            return True, WinningPosition

    # If any possibilty of win at Second Cross
    Allocation = []
    if PlayerDetails[Player]["Allocation"][2]:
        Allocation.append(3)
    if PlayerDetails[Player]["Allocation"][4]:
        Allocation.append(5)
    if PlayerDetails[Player]["Allocation"][6]:
        Allocation.append(7)

    # If two Positions are selected
    # One Left
    # Allocate That Position
    if len(Allocation) == 2:
        WinningPosition = list(set([3, 5, 7]) - set(Allocation))[0]
        if WinningPosition in current_open_positions:
            return True, WinningPosition

    return False, ""