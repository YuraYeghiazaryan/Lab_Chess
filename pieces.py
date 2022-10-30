import pygame as pg
from config import *


class Pieces(pg.sprite.Sprite):
    def __init__(self, size_of_cell: int, color: str, field_name: str, file_posfix: str, name: str):
        super().__init__()
        picture = pg.image.load(PIECE_PATH + color + file_posfix)
        self.name = name
        self.image = pg.transform.scale(picture, (cell_size, cell_size))
        self.rect = self.image.get_rect()  # 0 0 70 70
        self.color = color
        self.field_name = field_name
        self.color_picked_piece = None
        self.allowed_cells_for_steps = {'w': [], 'b': []}


class King(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str, name: str):
        super().__init__(size_of_cell, color, field, '_king.png', name)

    def right_steps(self, cell_field_name, cells_and_name, pieces, color, pieces_and_cells):
        if cell_field_name[0] != LTRS[0]:
            self.allowed_cells_for_steps[color].append(
                cells_and_name[LTRS[LTRS.index(cell_field_name[0]) - 1] + cell_field_name[1]])
            if cell_field_name[1] != str(cells):
                self.allowed_cells_for_steps[color].append(
                    cells_and_name[LTRS[LTRS.index(cell_field_name[0]) - 1] + str(int(cell_field_name[1]) + 1)])
            if cell_field_name[1] != '1':
                self.allowed_cells_for_steps[color].append(
                    cells_and_name[LTRS[LTRS.index(cell_field_name[0]) - 1] + str(int(cell_field_name[1]) - 1)])

        if cell_field_name[0] != LTRS[-1]:
            self.allowed_cells_for_steps[color].append(
                cells_and_name[LTRS[LTRS.index(cell_field_name[0]) + 1] + cell_field_name[1]])
            if cell_field_name[1] != str(cells):
                self.allowed_cells_for_steps[color].append(
                    cells_and_name[LTRS[LTRS.index(cell_field_name[0]) + 1] + str(
                        int(cell_field_name[1]) + 1)])
            if cell_field_name[1] != '1':
                self.allowed_cells_for_steps[color].append(
                    cells_and_name[LTRS[LTRS.index(cell_field_name[0]) + 1] + str(
                        int(cell_field_name[1]) - 1)])

        if cell_field_name[1] != '1':
            self.allowed_cells_for_steps[color].append(
                cells_and_name[cell_field_name[0] + str(int(cell_field_name[1]) - 1)])

        if cell_field_name[1] != str(cells):
            self.allowed_cells_for_steps[color].append(
                cells_and_name[cell_field_name[0] + str(int(cell_field_name[1]) + 1)])


class Queen(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str, name: str):
        super().__init__(size_of_cell, color, field, '_queen.png', name)

    def right_steps(self, cell_field_name, cells_and_name, pieces, color, pieces_and_cells):

        j = int(cell_field_name[1])
        for i in range(LTRS.index(cell_field_name[0]) - 1, -1, -1):
            if j + 1 > cells:
                break
            j += 1
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + str(j)])
            if LTRS[i] + str(j) in pieces_and_cells:
                break

        j = int(cell_field_name[1])
        for i in range(LTRS.index(cell_field_name[0]) + 1, cells):
            if j - 1 < 1:
                break
            j -= 1
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + str(j)])
            if LTRS[i] + str(j) in pieces_and_cells:
                break

        j = int(cell_field_name[1])
        for i in range(LTRS.index(cell_field_name[0]) + 1, cells):
            if j + 1 > cells:
                break
            j += 1
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + str(j)])
            if LTRS[i] + str(j) in pieces_and_cells:
                break

        j = int(cell_field_name[1])
        for i in range(LTRS.index(cell_field_name[0]) - 1, -1, -1):
            if j - 1 < 1:
                break
            j -= 1
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + str(j)])
            if LTRS[i] + str(j) in pieces_and_cells:
                break

        for i in range(int(cell_field_name[1]) + 1, cells + 1):
            self.allowed_cells_for_steps[color].append(cells_and_name[cell_field_name[0] + str(i)])
            if cell_field_name[0] + str(i) in pieces_and_cells:
                break
        for i in range(int(cell_field_name[1]) - 1, 0, -1):
            self.allowed_cells_for_steps[color].append(cells_and_name[cell_field_name[0] + str(i)])
            if cell_field_name[0] + str(i) in pieces_and_cells:
                break
        for i in range(LTRS.index(cell_field_name[0]) - 1, -1, -1):
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + cell_field_name[1]])
            if LTRS[i] + cell_field_name[1] in pieces_and_cells:
                break
        for i in range(LTRS.index(cell_field_name[0]) + 1, cells):
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + cell_field_name[1]])
            if LTRS[i] + cell_field_name[1] in pieces_and_cells:
                break


class Rook(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str, name: str):
        super().__init__(size_of_cell, color, field, '_rook.png', name)

    def right_steps(self, cell_field_name, cells_and_name, pieces, color, pieces_and_cells):

        for i in range(int(cell_field_name[1]) + 1, cells + 1):
            self.allowed_cells_for_steps[color].append(cells_and_name[cell_field_name[0] + str(i)])
            if cell_field_name[0] + str(i) in pieces_and_cells:
                break
        for i in range(int(cell_field_name[1]) - 1, 0, -1):
            self.allowed_cells_for_steps[color].append(cells_and_name[cell_field_name[0] + str(i)])
            if cell_field_name[0] + str(i) in pieces_and_cells:
                break
        for i in range(LTRS.index(cell_field_name[0]) - 1, -1, -1):
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + cell_field_name[1]])
            if LTRS[i] + cell_field_name[1] in pieces_and_cells:
                break
        for i in range(LTRS.index(cell_field_name[0]) + 1, cells):
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + cell_field_name[1]])
            if LTRS[i] + cell_field_name[1] in pieces_and_cells:
                break


class Knight(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str, name: str):
        super().__init__(size_of_cell, color, field, '_knight.png', name)

    def right_steps(self, cell_field_name, cells_and_name, pieces, color, pieces_and_cells):
        if LTRS.index(cell_field_name[0]) >= 1 and int(cell_field_name[1]) <= 6:
            self.allowed_cells_for_steps[color].append(
                cells_and_name[LTRS[LTRS.index(cell_field_name[0]) - 1] + str(int(cell_field_name[1]) + 2)])
        if LTRS.index(cell_field_name[0]) >= 2 and int(cell_field_name[1]) <= 7:
            self.allowed_cells_for_steps[color].append(
                cells_and_name[LTRS[LTRS.index(cell_field_name[0]) - 2] + str(int(cell_field_name[1]) + 1)])
        if LTRS.index(cell_field_name[0]) <= 6 and int(cell_field_name[1]) <= 6:
            self.allowed_cells_for_steps[color].append(
                cells_and_name[LTRS[LTRS.index(cell_field_name[0]) + 1] + str(int(cell_field_name[1]) + 2)])
        if LTRS.index(cell_field_name[0]) <= 5 and int(cell_field_name[1]) <= 7:
            self.allowed_cells_for_steps[color].append(
                cells_and_name[LTRS[LTRS.index(cell_field_name[0]) + 2] + str(int(cell_field_name[1]) + 1)])
        if LTRS.index(cell_field_name[0]) <= 5 and int(cell_field_name[1]) >= 2:
            self.allowed_cells_for_steps[color].append(
                cells_and_name[LTRS[LTRS.index(cell_field_name[0]) + 2] + str(int(cell_field_name[1]) - 1)])
        if LTRS.index(cell_field_name[0]) <= 6 and int(cell_field_name[1]) >= 3:
            self.allowed_cells_for_steps[color].append(
                cells_and_name[LTRS[LTRS.index(cell_field_name[0]) + 1] + str(int(cell_field_name[1]) - 2)])
        if LTRS.index(cell_field_name[0]) >= 1 and int(cell_field_name[1]) >= 3:
            self.allowed_cells_for_steps[color].append(
                cells_and_name[LTRS[LTRS.index(cell_field_name[0]) - 1] + str(int(cell_field_name[1]) - 2)])
        if LTRS.index(cell_field_name[0]) >= 2 and int(cell_field_name[1]) >= 2:
            self.allowed_cells_for_steps[color].append(
                cells_and_name[LTRS[LTRS.index(cell_field_name[0]) - 2] + str(int(cell_field_name[1]) - 1)])


class Bishop(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str, name: str):
        super().__init__(size_of_cell, color, field, '_bishop.png', name)

    def right_steps(self, cell_field_name, cells_and_name, pieces, color, pieces_and_cells):
        j = int(cell_field_name[1])
        for i in range(LTRS.index(cell_field_name[0]) - 1, -1, -1):
            if j + 1 > cells:
                break
            j += 1
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + str(j)])
            if LTRS[i] + str(j) in pieces_and_cells:
                break

        j = int(cell_field_name[1])
        for i in range(LTRS.index(cell_field_name[0]) + 1, cells):
            if j - 1 < 1:
                break
            j -= 1
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + str(j)])
            if LTRS[i] + str(j) in pieces_and_cells:
                break

        j = int(cell_field_name[1])
        for i in range(LTRS.index(cell_field_name[0]) + 1, cells):
            if j + 1 > cells:
                break
            j += 1
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + str(j)])
            if LTRS[i] + str(j) in pieces_and_cells:
                break

        j = int(cell_field_name[1])
        for i in range(LTRS.index(cell_field_name[0]) - 1, -1, -1):
            if j - 1 < 1:
                break
            j -= 1
            self.allowed_cells_for_steps[color].append(cells_and_name[LTRS[i] + str(j)])
            if LTRS[i] + str(j) in pieces_and_cells:
                break


class Pawn(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str, name: str):
        super().__init__(size_of_cell, color, field, '_pawn.png', name)

    def right_steps(self, cell_field_name, cells_and_name, pieces, color, pieces_and_cells):

        """ability to walk over two cells at once"""

        if color == 'w' and cell_field_name[1] == str(2):
            self.allowed_cells_for_steps[color].append(
                cells_and_name[cell_field_name[0] + str(int(cell_field_name[1]) + 2)])
        elif color == 'b' and cell_field_name[1] == str(7):
            self.allowed_cells_for_steps[color].append(
                cells_and_name[cell_field_name[0] + str(int(cell_field_name[1]) - 2)])

        """ability to walk over a single cell"""

        if color == 'w' and cell_field_name[1] != str(cells):
            if cell_field_name[0] + str(int(cell_field_name[1]) + 1) not in pieces_and_cells:
                self.allowed_cells_for_steps[color].append(
                    cells_and_name[cell_field_name[0] + str(int(cell_field_name[1]) + 1)])

            if color == 'w':
                if cell_field_name[0] != LTRS[0] and cell_field_name != str(cells):
                    self.allowed_cells_for_steps[color].append(
                        cells_and_name[LTRS[LTRS.index(cell_field_name[0]) - 1] + str(int(cell_field_name[1]) + 1)])

            if color == 'w':
                if cell_field_name[0] != LTRS[-1] and cell_field_name != str(cells):
                    self.allowed_cells_for_steps[color].append(
                        cells_and_name[LTRS[LTRS.index(cell_field_name[0]) + 1] + str(int(cell_field_name[1]) + 1)])

        """ability to walk over a single cell"""

        if color == 'b' and cell_field_name[1] != str(1):
            if cell_field_name[0] + str(int(cell_field_name[1]) - 1) not in pieces_and_cells:
                self.allowed_cells_for_steps[color].append(
                    cells_and_name[cell_field_name[0] + str(int(cell_field_name[1]) - 1)])

            if color == 'b':
                if cell_field_name[0] != LTRS[0] and cell_field_name != str(1):
                    self.allowed_cells_for_steps[color].append(
                        cells_and_name[LTRS[LTRS.index(cell_field_name[0]) - 1] + str(int(cell_field_name[1]) - 1)])

            if color == 'b':
                if cell_field_name[0] != LTRS[-1] and cell_field_name != str(1):
                    self.allowed_cells_for_steps[color].append(
                        cells_and_name[LTRS[LTRS.index(cell_field_name[0]) + 1] + str(int(cell_field_name[1]) - 1)])
