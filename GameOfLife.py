from TestCell import TestNeighbours
import random
# Game of life


def XYBoard(x: int, y: int, rand: bool = False) -> list:
    """Create board with x and y dimensions"""
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
    """Print cleanly"""
    for i in range(0, len(theList)):
        print(theList[i])
    print("")


def NextIteration(board) -> list:
    """Calculate the next generation based on an earlier generation"""
    nextBoard = []
    x = len(board[0])
    y = len(board)
    for Y in range(0, y):
        nextBoard.append([])
        for X in range(0, x):
            nextBoard[Y].append(TestNeighbours(X, Y, board))
    return nextBoard


def DoIterations(iteration:int = 10, x: int = 5, y: int = 5):
    """Print out iterations, with x and y"""
    board = XYBoard(x,y,True)
    CleanPrint(board)
    for i in range(0,iteration):
        board = NextIteration(board)
        CleanPrint(board)


DoIterations()