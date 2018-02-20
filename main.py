import app
import time


# check the new position whether is valid.
def checking(new, pieces, size):
    # check bounding.
    if new.x < 0 or new.y < 0 or new.x >= size or new.y >= size:
        return False

    for piece in pieces:
        # check same position.
        if new.x == piece.x and new.y == piece.y: return False
        # check x and y
        if new.x == piece.x or new.y == piece.y: return False
        # check cross
        if abs(new.x - piece.x) == abs(new.y - piece.y): return False
    
    # all pass
    return True


# get the next position.
def nextPiece(piece, size):
    # next column
    x = piece.x + 1
    y = piece.y

    # if over bounding, next row.
    if x >= size:
        x = 0
        y = y + 1

    # the end.
    if y >= size: return None

    # new piece with new position.
    return app.Piece(x, y, piece.t)


def setQueen(board, x, y, deep):
    global _counting_solutions

    # find the next valid position to prepare setting a queen.
    new = app.Piece(x, y, app.PieceType.QUEEN)
    while new != None and checking(new, board.pieces, board.row) == False:
        new = nextPiece(new, board.row)

    # if not found, do nothing.
    if new == None: return
    if new.y != deep: return # preformance optimize
    
    # set a queen.
    board.pieces.append(new)

    # if the queen is the last one, found a solution.
    if deep == board.row - 1:
        _counting_solutions += 1
        print('Solution ' + str(_counting_solutions) + str(board))
    # else set the next one.
    else:
        setQueen(board, new.x, new.y, deep + 1)

    # if found solution or no solution, pick up the last queen.
    prev = board.pieces.pop()

    # set the queen to next position to try another solutions.
    new = nextPiece(prev, board.row)
    if new == None: return
    setQueen(board, new.x, new.y, deep)
    

_counting_solutions = 0
if __name__ == '__main__':
    ts = time.time()

    setQueen(app.Board(size = 11), 0, 0, 0)

    te = time.time()
    print('Solutions: ' + str(_counting_solutions))
    print('Cost: ' + str(round(te - ts, 2)) + ' sec')