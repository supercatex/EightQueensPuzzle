from enum import Enum


class PieceType(Enum):
    EMPTY = '◌'
    QUEEN = '●'


class Piece:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.t = PieceType.EMPTY
    
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y
    
    @property
    def t(self):
        return self.__t
    
    @t.setter
    def t(self, t):
        self.__t = t


class Board:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.pieces = []

    def __init__(self, size):
        self.row = size
        self.col = size
        self.pieces = []
    
    @property
    def row(self):
        return self.__row
    
    @row.setter
    def row(self, row):
        self.__row = row

    @property
    def col(self):
        return self.__col
    
    @col.setter
    def col(self, col):
        self.__col = col

    @property
    def pieces(self):
        return self.__pieces
    
    @pieces.setter
    def pieces(self, pieces):
        self.__pieces = pieces

    def getPiece(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return piece
        return None

    def setPiece(self, x, y, t):
        piece = self.getPiece(x, y)
        if (piece == None):
            piece = Piece(x, y)
            self.pieces.append(piece)
        piece.t = t

    def __str__(self):
        s = '\n'
        for y in range(0, self.row):
            for x in range(0, self.col):
                piece = self.getPiece(x, y)
                if piece == None:
                    s = s + PieceType.EMPTY.value + ' '
                else:
                    s = s + piece.t.value + ' '
            s = s + '\n'
        return s
