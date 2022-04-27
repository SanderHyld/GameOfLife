def TestNeighbours(x: int, y: int, prevBoard: list) -> bool:
    """Checks neighbours at a specic coordinate and returns a bool based on the GoL rules"""

    neighbour = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i != 0 or j != 0):
                try:
                    if (y+j != -1):
                        if (x+i != -1):
                            if prevBoard[y + j][x + i]:
                                neighbour += 1
                except:
                    pass

    if prevBoard[y][x]:
        # rule 1 states that living cell with 2-3 neighbours survive
        if neighbour in (2, 3):
            return True

    if not prevBoard[y][x]:
        # rule 2 states that dead cell with 3 neighbours come to life
        if neighbour == 3:
            return True

    # rule 3 states that all other living cells will die
    return False