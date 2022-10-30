win_size = (1000, 700)
FPS = 10
cells = 8
cell_size = 57
# COLORS = [(239, 219, 197), (130, 69, 19)]
ACTIVE_COLOR = (250, 50, 50, 64)
COLORS_FOR_BOARD = ['images/white_for_board.png', 'images/black_for_board.png']
fnt_size = 18
IMG_PATH = 'images/back.jpeg'
LTRS = 'ABCDEFGH'
next_step = ('w', 'b')
PIECES_TYPES = {
    'k': ('King', 'b'), 'K': ('King', 'w'),
    'q': ('Queen', 'b'), 'Q': ('Queen', 'w'),
    'r': ('Rook', 'b'), 'R': ('Rook', 'w'),
    'b': ('Bishop', 'b'), 'B': ('Bishop', 'w'),
    'n': ('Knight', 'b'), 'N': ('Knight', 'w'),
    'p': ('Pawn', 'b'), 'P': ('Pawn', 'w')
}
PIECE_PATH = 'images/pieces/'
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]
