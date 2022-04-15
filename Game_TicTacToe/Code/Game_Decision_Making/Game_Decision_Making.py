def ifPlayerWon(Player_Allocation_List):
    if Player_Allocation_List[0] and Player_Allocation_List[1] and Player_Allocation_List[2]:
        return True
    if Player_Allocation_List[3] and Player_Allocation_List[4] and Player_Allocation_List[5]:
        return True
    if Player_Allocation_List[6] and Player_Allocation_List[7] and Player_Allocation_List[8]:
        return True
    if Player_Allocation_List[0] and Player_Allocation_List[3] and Player_Allocation_List[6]:
        return True
    if Player_Allocation_List[1] and Player_Allocation_List[4] and Player_Allocation_List[7]:
        return True
    if Player_Allocation_List[2] and Player_Allocation_List[5] and Player_Allocation_List[8]:
        return True
    if Player_Allocation_List[0] and Player_Allocation_List[4] and Player_Allocation_List[8]:
        return True
    if Player_Allocation_List[2] and Player_Allocation_List[4] and Player_Allocation_List[6]:
        return True

    return False