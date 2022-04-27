# Game of life

# Create board x*y matrix
def XYBoard(x: int, y: int) -> list:
    gameBoard = []
    for Y in range(0,y):
        xDirection = []
        for X in range(0,x):
            xDirection.append(False)
        gameBoard.append(xDirection)
    return gameBoard


def CleanPrint(theList):
    # Debugging function, delete later
    for i in range(0, len(theList)):
        print(theList[i])


# test for neighbours and create next iteration / I'll do this in two functions
    # rule 1 states that living cell with 2-3 neighbours survive
    # rule 2 states that dead cell with 3 neighbours come to life
    # rule 3 states that all other living cells will die
def NextIteration(board) -> list:
    def testNeighbours(xx, yy, prevBoard) -> bool:
        """
        Board details
        (xx-1, yy-1)  (xx, yy-1)  (xx+1, yy-1)
        (xx-1, yy)    (xx, yy)    (xx+1, yy)
        (xx-1, yy+1)  (xx, yy+1)  (xx+1, yy+1)
        """
        neighbour = 0
        for i in range(-1,2):
            for j in range(-1, 2):
                if i != 0 and j != 0:
                    

        if prevBoard[xx][yy]:
            #Living cell survives, rule 1
            if 2 <= neighbour <= 3:
               return True
        
        elif not prevBoard[xx][yy]:
            #Dead cell comes to life
            if neighbour == 3:
                return True
        
        else:
            return False

    nextBoard = []
    x = len(board[0])
    y = len(board)
    for X in range (0, x):
        




# plot the result