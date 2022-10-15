import pygame as pg
from config import *


class Pieces(pg.sprite.Sprite):
    def __init__(self, size_of_cell: int, color: str, field_name: str, file_posfix: str):
        super().__init__()
        picture = pg.image.load(PIECE_PATH + color + file_posfix)
        self.image = pg.transform.scale(picture, (cell_size, cell_size))
        self.rect = self.image.get_rect()  # 0 0 70 70
        self.color = color
        self.field_name = field_name
        self.color_picked_piece = None
        self.allowed_cells_for_steps = pg.sprite.Group()
        #self.cells_and_name = self.create_cells_and_name()
        #self.__right_steps(self)


class King(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str):
        super().__init__(size_of_cell, color, field, '_king.png')

    def right_steps(self, cell_field_name):
     #if abs(x - self.rect.x) <= cell_size and abs(y - self.rect.y) <= cell_size:
        if cell_field_name[0] != LTRS[0]:
            self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[LTRS.index(cell_field_name[0])-1] + cell_field_name[1]]) #dzax
            if cell_field_name[1] != str(cells):
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[LTRS.index(cell_field_name[0]) - 1] + str(
                    int(cell_field_name[1]) + 1)])  # verev dzax ankyunagic
            if cell_field_name[1] != '1':
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[LTRS.index(cell_field_name[0]) - 1] + str(
                    int(cell_field_name[1]) - 1)])  # nerqev dzax

        if cell_field_name[0] != LTRS[-1]:
            self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[LTRS.index(cell_field_name[0])+1] + cell_field_name[1]]) #aj
            if cell_field_name[1] != str(cells):
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[LTRS.index(cell_field_name[0]) + 1] + str(
                    int(cell_field_name[1]) + 1)])  # verev aj
            if cell_field_name[1] != '1':
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[LTRS.index(cell_field_name[0]) + 1] + str(
                    int(cell_field_name[1]) - 1)])  # nerqev aj

        if cell_field_name[1] != 1:
            self.allowed_cells_for_steps.add(self.cells_and_name[cell_field_name[0] + str(int(cell_field_name[1]) - 1)]) #nerqev

        if cell_field_name[1] != cells:
            self.allowed_cells_for_steps.add(self.cells_and_name[cell_field_name[0] + str(int(cell_field_name[1]) + 1)]) #verev




class Queen(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str):
        super().__init__(size_of_cell, color, field, '_queen.png')

    '''def right_steps(self, cell_field_name):
        for i in range(LTRS.index(cell_field_name[0] + 1), 0, -1):     #dzax verev ankyunagic
            for j in range(int(cell_field_name[1] + 1), cells + 1):
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i]+'j'])
                if self.cells_and_name[LTRS[i]+'j'] in self.__all_pieces:
                    break
        for i in range(LTRS.index(cell_field_name[0]) + 1, cells):     #aj nerqev ankyunagic
            for j in range(int(cell_field_name[1]) + 1, 0, -1):
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i] + 'j'])
                if self.cells_and_name[LTRS[i]+'j'] in self.__all_pieces:
                    break
        for i in range(LTRS.index(cell_field_name[0]) +1, cells):     # aj verev ankyunagic
            for j in range(int(cell_field_name[1]) + 1, cells + 1):
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i]+'j'])
                if self.cells_and_name[LTRS[i]+'j'] in self.__all_pieces:
                    break
        for i in range(LTRS.index(cell_field_name[0]) + 1, 0, -1):   #dzax nerqev ankyunagic
            for j in range(int(cell_field_name[1]) + 1, 0, -1):
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i] + 'j'])
                if self.cells_and_name[LTRS[i]+'j'] in self.__all_pieces:
                    break
        for i in range(int(cell_field_name[1]), cells + 1):           #verev
            self.allowed_cells_for_steps.add(self.cells_and_name[cell_field_name[0] + 'i'])
            if self.cells_and_name[cell_field_name[0] + 'i'] in self.__all_pieces:
                break
        for i in range(int(cell_field_name[1]), 0, -1):               #nerqev
            self.allowed_cells_for_steps.add(self.cells_and_name[cell_field_name[0] + 'i'])
            if self.cells_and_name[cell_field_name[0] + 'i'] in self.__all_pieces:
                break
        for i in range(int(cell_field_name[0]), 0, -1):               #dzax
            self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i] + cell_field_name[1]])
            if self.cells_and_name[cell_field_name[0] + 'i'] in self.__all_pieces:
                break
        for i in range(int(cell_field_name[1]), cells + 1):           #aj
            self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i] + cell_field_name[1]])
            if self.cells_and_name[cell_field_name[0] + 'i'] in self.__all_pieces:
                break'''


class Rook(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str):
        super().__init__(size_of_cell, color, field, '_rook.png')

    '''def right_steps(self, cell_field_name):
        for i in range(int(cell_field_name[1]), cells + 1):           #verev
            self.allowed_cells_for_steps.add(self.cells_and_name[cell_field_name[0] + 'i'])
            if self.cells_and_name[cell_field_name[0] + 'i'] in self.__all_pieces:
                break
        for i in range(int(cell_field_name[1]), 0, -1):               #nerqev
            self.allowed_cells_for_steps.add(self.cells_and_name[cell_field_name[0] + 'i'])
            if self.cells_and_name[cell_field_name[0] + 'i'] in self.__all_pieces:
                break
        for i in range(int(cell_field_name[0]), 0, -1):               #dzax
            self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i] + cell_field_name[1]])
            if self.cells_and_name[cell_field_name[0] + 'i'] in self.__all_pieces:
                break
        for i in range(int(cell_field_name[1]), cells + 1):           #aj
            self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i] + cell_field_name[1]])
            if self.cells_and_name[cell_field_name[0] + 'i'] in self.__all_pieces:
                break'''


class Knight(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str):
        super().__init__(size_of_cell, color, field, '_knight.png')

    def right_steps(self, cell_field_name):
        pass


class Bishop(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str):
        super().__init__(size_of_cell, color, field, '_bishop.png')

    '''def right_steps(self, cell_field_name):
        for i in range(LTRS.index(cell_field_name[0] + 1), 0, -1):     #dzax verev ankyunagic
            for j in range(int(cell_field_name[1] + 1), cells + 1):
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i]+'j'])
                if self.cells_and_name[LTRS[i]+'j'] in self.__all_pieces:
                    break
        for i in range(LTRS.index(cell_field_name[0]) + 1, cells):     #aj nerqev ankyunagic
            for j in range(int(cell_field_name[1]) + 1, 0, -1):
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i] + 'j'])
                if self.cells_and_name[LTRS[i]+'j'] in self.__all_pieces:
                    break
        for i in range(LTRS.index(cell_field_name[0]) +1, cells):     # aj verev ankyunagic
            for j in range(int(cell_field_name[1]) + 1, cells + 1):
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i]+'j'])
                if self.cells_and_name[LTRS[i]+'j'] in self.__all_pieces:
                    break
        for i in range(LTRS.index(cell_field_name[0]) + 1, 0, -1):   #dzax nerqev ankyunagic
            for j in range(int(cell_field_name[1]) + 1, 0, -1):
                self.allowed_cells_for_steps.add(self.cells_and_name[LTRS[i] + 'j'])
                if self.cells_and_name[LTRS[i]+'j'] in self.__all_pieces:
                    break'''


class Pawn(Pieces):
    def __init__(self, size_of_cell: int, color: str, field: str):
        super().__init__(size_of_cell, color, field, '_pawn.png')

    '''def right_steps(self, cell_field_name):
        if cell_field_name[1] != cells:
            self.allowed_cells_for_steps.add(self.cells_and_name[cell_field_name[0] + str(int(cell_field_name[1]) + 1)])'''
