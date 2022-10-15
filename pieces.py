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




