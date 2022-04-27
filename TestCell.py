def TestNeighbours(xx, yy, prevBoard) -> bool:
    """Checks neighbours at a specic coordinate and returns a bool based on the GoL rules"""
    
    neighbour = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0):
                try:
                    if (yy+j != -1):
                        if (xx+i != -1):
                            if prevBoard[yy + j][xx + i]:
                                neighbour += 1
                except:
                    pass

    if prevBoard[yy][xx]:
        # rule 1 states that living cell with 2-3 neighbours survive
        if neighbour in (2, 3):
            return True

    if not prevBoard[yy][xx]:
        # rule 2 states that dead cell with 3 neighbours come to life
        if neighbour == 3:
            return True

    # rule 3 states that all other living cells will die
    return False