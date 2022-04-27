def TestNeighbours(xx, yy, prevBoard) -> bool:
    # Checks neighbours at a specic coordinate and returns a bool based on the GoL rules
    """
    Board details
    (xx-1, yy-1)  (xx, yy-1)  (xx+1, yy-1)
    (xx-1, yy)    (xx, yy)    (xx+1, yy)
    (xx-1, yy+1)  (xx, yy+1)  (xx+1, yy+1)
    """
    neighbour = 0

    if yy != 0 and yy != len(prevBoard)-1 and xx != 0 and xx != len(prevBoard[0])-1:
        # xx and yy are not on the edges / corners
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 or j != 0):
                    if prevBoard[yy + j][xx + i]:
                        neighbour += 1

    elif xx == 0:
        # xx is on left edge
        if yy == 0:
            # yy is on top
            # top left corner
            if prevBoard[yy][xx + 1]:
                neighbour += 1
            if prevBoard[yy + 1][xx]:
                neighbour += 1
            if prevBoard[yy + 1][xx + 1]:
                neighbour += 1
        elif yy == len(prevBoard) - 1:
            # yy is on bottom
            # bottom left corner
            if prevBoard[yy - 1][xx]:
                neighbour += 1
            if prevBoard[yy - 1][xx + 1]:
                neighbour += 1
            if prevBoard[yy][xx + 1]:
                neighbour += 1
        else:
            # xx is along the left edge and not in corner
            if prevBoard[yy - 1][xx]:
                neighbour += 1
            if prevBoard[yy - 1][xx + 1]:
                neighbour += 1
            if prevBoard[yy][xx + 1]:
                neighbour += 1
            if prevBoard[yy + 1][xx]:
                neighbour += 1
            if prevBoard[yy + 1][xx + 1]:
                neighbour += 1

    elif xx == len(prevBoard[0]) - 1:
        # xx is on right edge
        if yy == 0:
            # yy is on top
            # top right corner
            if prevBoard[yy][xx - 1]:
                neighbour += 1
            if prevBoard[yy + 1][xx - 1]:
                neighbour += 1
            if prevBoard[yy + 1][xx]:
                neighbour += 1
        elif yy == len(prevBoard) - 1:
            # yy is on bottom
            # bottom right corner
            if prevBoard[yy - 1][xx - 1]:
                neighbour += 1
            if prevBoard[yy - 1][xx]:
                neighbour += 1
            if prevBoard[yy][xx - 1]:
                neighbour += 1
        else:
            # xx is along the right edge and not in corner
            if prevBoard[yy - 1][xx - 1]:
                neighbour += 1
            if prevBoard[yy - 1][xx]:
                neighbour += 1
            if prevBoard[yy][xx - 1]:
                neighbour += 1
            if prevBoard[yy + 1][xx - 1]:
                neighbour += 1
            if prevBoard[yy + 1][xx]:
                neighbour += 1
    elif yy == 0:
        # yy is on top edge
        if prevBoard[yy][xx - 1]:
            neighbour += 1
        if prevBoard[yy][xx + 1]:
            neighbour += 1
        if prevBoard[yy + 1][xx - 1]:
            neighbour += 1
        if prevBoard[yy + 1][xx]:
            neighbour += 1
        if prevBoard[yy + 1][xx + 1]:
            neighbour += 1
    elif yy == len(prevBoard) - 1:
        ## yy is on bottom edge
        if prevBoard[yy - 1][xx - 1]:
            neighbour += 1
        if prevBoard[yy - 1][xx]:
            neighbour += 1
        if prevBoard[yy - 1][xx + 1]:
            neighbour += 1
        if prevBoard[yy][xx - 1]:
            neighbour += 1
        if prevBoard[yy][xx + 1]:
            neighbour += 1

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