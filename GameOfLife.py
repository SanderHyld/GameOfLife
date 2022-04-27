from TestCell import TestNeighbours
import random
# Game of life

def XYBoard(x: int, y: int, rand: bool = False) -> list:
    # Create board x*y matrix
    gameBoard = []
    for Y in range(0, y):
        xDirection = []
        for X in range(0, x):
            if rand:
                xDirection.append(random.choice([True,False]))
            else:
                xDirection.append(False)
        gameBoard.append(xDirection)
    return gameBoard


def CleanPrint(theList):
    # Debugging function, delete later
    for i in range(0, len(theList)):
        print(theList[i])


# test for neighbours and create next iteration / I'll do this in two functions
def NextIteration(board) -> list:
    nextBoard = []
    x = len(board[0]) - 1
    y = len(board) - 1
    for Y in range(0, x):
        nextBoard.append([])
        for X in range(0, y):
            nextBoard[Y].append(TestNeighbours(X, Y, board))
    return nextBoard


Board = XYBoard(5, 5, True)
CleanPrint(Board)

Board = NextIteration(Board)
CleanPrint(Board)

Board = NextIteration(Board)
CleanPrint(Board)



# plot the result