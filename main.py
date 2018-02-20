import app
import time


# check the new position whether is valid.
def checking(x, y, size, deep):
	global _flag_x, _flag_1, _flag_2

	# has and only has one Queen at each row.
	if y != deep: return False
	
	# check bounding.
	if x < 0 or x >= size or y < 0 or y >= size: return False
	
	# check horizontal line and two cross line.
	if _flag_x[x] or _flag_1[x + y] or _flag_2[x + (size - 1 - y)]: return False
	
	# pass all checking.
	return True


# get the next position.
def nextPosition(x, y, size, deep):

	# has and only has one Queen at each row.
	if y != deep: return None
	
	# calculate the next position by index.
	index = y * size + x + 1
	if index >= size * size: return None
	return {'x': index % size, 'y': index // size}


def setQueen(board, x, y, deep):
	global _counting_solutions, _flag_x, _flag_1, _flag_2

	# find the next valid position to prepare setting a Queen.
	pos = {'x': x, 'y': y}
	while pos != None and checking(pos['x'], pos['y'], board.row, deep) == False:
		pos = nextPosition(pos['x'], pos['y'], board.row, deep)

	# if not found, do nothing.
	if pos == None: return

	# set a Queen.
	piece = app.Piece(pos['x'], pos['y'], app.PieceType.QUEEN)
	board.pieces.append(piece)
	_flag_x[piece.x] = True
	_flag_1[piece.x + piece.y] = True
	_flag_2[piece.x + board.row - 1 - piece.y] = True

	# if the Queen is the last one, found a solution.
	if deep == board.row - 1:
		_counting_solutions += 1
		#print('Solution ' + str(_counting_solutions) + str(board))
	# else set the next one.
	else:
		setQueen(board, 0, pos['y'] + 1, deep + 1)

	# if found solution or no solution, pick up the last Queen.
	prev = board.pieces.pop()
	_flag_x[prev.x] = False
	_flag_1[prev.x + prev.y] = False
	_flag_2[prev.x + board.row - 1 - prev.y] = False

	# set the Queen to next position to try another solutions.
	pos = nextPosition(prev.x, prev.y, board.row, deep)
	if pos == None: return
	setQueen(board, pos['x'], pos['y'], deep)


_size = 13
_counting_solutions = 0
_flag_x = [False] * _size
_flag_1 = [False] * (_size * 2 - 1)
_flag_2 = [False] * (_size * 2 - 1)

if __name__ == '__main__':
	ts = time.time()

	setQueen(app.Board(_size), 0, 0, 0)

	te = time.time()
	print('Solutions: ' + str(_counting_solutions))
	print('Cost: ' + str(round(te - ts, 2)) + ' sec')
