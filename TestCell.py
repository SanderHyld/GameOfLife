def TestNeighbours(xx, yy, prevBoard) -> bool:
    # Checks neighbours at a specic coordinate and returns a bool based on the GoL rules
    """
    Board details
    (xx-1, yy-1)  (xx, yy-1)  (xx+1, yy-1)
    (xx-1, yy)    (xx, yy)    (xx+1, yy)
    (xx-1, yy+1)  (xx, yy+1)  (xx+1, yy+1)
    """
    neighbour = 0

    if yy != 0 and yy != len(prevBoard) and xx != 0 and xx != len(prevBoard[0]):
        # xx and yy are not on the edges / corners
        for i in range(-1,2):
            for j in range(-1, 2):
                if i != 0 and j != 0:
                    if prevBoard[xx+i][yy+j]:
                        neighbour += 1
    
    elif xx == 0:
        # xx is on left edge
        if yy == 0:
            # yy is on top
            # top left corner
            if prevBoard[xx+1][yy]:
                neighbour += 1
            if prevBoard[xx][yy+1]:
                neighbour += 1
            if prevBoard[xx+1][yy+1]:
                neighbour += 1
        elif yy == len(prevBoard)-1:
            # yy is on bottom
            # bottom left corner
            if prevBoard[xx][yy-1]:
                neighbour += 1
            if prevBoard[xx+1][yy-1]:
                neighbour += 1
            if prevBoard[xx+1][yy]:
                neighbour += 1
        else:
            # xx is along the left edge and not in corner
            if prevBoard[xx][yy-1]:
                neighbour += 1
            if prevBoard[xx+1][yy-1]:
                neighbour += 1
            if prevBoard[xx+1][yy]:
                neighbour += 1
            if prevBoard[xx][yy+1]:
                neighbour += 1
            if prevBoard[xx+1][yy+1]:
                neighbour += 1
    
    elif xx == len(prevBoard[0])-1:
        # xx is on right edge
        if yy == 0:
            # yy is on top
            # top right corner
            if prevBoard[xx-1][yy]:
                neighbour += 1
            if prevBoard[xx-1][yy+1]:
                neighbour += 1
            if prevBoard[xx][yy+1]:
                neighbour += 1
        elif yy == len(prevBoard)-1:
            # yy is on bottom
            # bottom right corner
            if prevBoard[xx-1][yy-1]:
                neighbour += 1
            if prevBoard[xx][yy-1]:
                neighbour += 1
            if prevBoard[xx-1][yy]:
                neighbour += 1
        else:
            # xx is along the right edge and not in corner
            if prevBoard[xx-1][yy-1]:
                neighbour += 1
            if prevBoard[xx][yy-1]:
                neighbour += 1
            if prevBoard[xx-1][yy]:
                neighbour += 1
            if prevBoard[xx-1][yy+1]:
                neighbour += 1
            if prevBoard[xx][yy+1]:
                neighbour += 1
    elif yy == 0:
        # yy is on top edge
        if prevBoard[xx-1][yy]:
            neighbour += 1
        if prevBoard[xx+1][yy]:
            neighbour += 1
        if prevBoard[xx-1][yy+1]:
            neighbour += 1
        if prevBoard[xx][yy+1]:
            neighbour += 1
        if prevBoard[xx+1][yy+1]:
            neighbour += 1
    elif yy == len(prevBoard)-1:
        ## yy is on bottom edge
        if prevBoard[xx-1][yy-11]:
            neighbour += 1
        if prevBoard[xx][yy-1]:
            neighbour += 1
        if prevBoard[xx+1][yy-1]:
            neighbour += 1
        if prevBoard[xx-1][yy]:
            neighbour += 1
        if prevBoard[xx+1][yy]:
            neighbour += 1

    if prevBoard[xx][yy]:
        # rule 1 states that living cell with 2-3 neighbours survive
        if 2 <= neighbour <= 3:
           return True

    if not prevBoard[xx][yy]:
        # rule 2 states that dead cell with 3 neighbours come to life
        if neighbour == 3:
            return True
        
    # rule 3 states that all other living cells will die
    return False