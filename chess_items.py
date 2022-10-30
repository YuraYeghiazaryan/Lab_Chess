from pieces import *
import board_data
pg.init()
fnt_obj = pg.font.Font(pg.font.get_default_font(), fnt_size)


class Chessboard:
    def __init__(self, parent_surface: pg.Surface):
        self.__screen = parent_surface
        self.__table = board_data.board
        self.__cells = cells
        self.__size = cell_size
        self.__pieces_types = PIECES_TYPES
        self.__pressed_cell = None
        self.__picked_piece = None
        self.__all_cells = pg.sprite.Group()
        self.__all_pieces = pg.sprite.Group()
        self.__prepare_screen()
        self.__draw_playboard()
        self.__draw_all_pieces()
        pg.display.update()

    '''  background image   '''

    def __prepare_screen(self):

        back_img = pg.image.load(IMG_PATH)
        back_img = pg.transform.scale(back_img, win_size)
        self.__screen.blit(back_img, (0, 0))

    def __draw_playboard(self):
        total_width = self.__cells * self.__size
        num_fields = self.__create_num_fields()
        self.__all_cells = self.__create_all_cells()
        num_fields_depth = num_fields[0].get_width()
        playboard_view = pg.Surface((
            2 * num_fields_depth + total_width,
            2 * num_fields_depth + total_width
        ))

        playboard_view.blit(num_fields[0],
                            (0, num_fields_depth))
        playboard_view.blit(num_fields[0],
                            (num_fields_depth + total_width, num_fields_depth))
        playboard_view.blit(num_fields[1],
                            (num_fields_depth, 0))
        playboard_view.blit(num_fields[1],
                            (num_fields_depth, num_fields_depth + total_width))
        playboard_rect = playboard_view.get_rect()
        playboard_rect.x += (self.__screen.get_width() - playboard_rect.width) // 2
        playboard_rect.y += (self.__screen.get_height() - playboard_rect.height) // 2
        self.__screen.blit(playboard_view, playboard_rect)
        cells_offset = (
            playboard_rect.x + num_fields_depth,
            playboard_rect.y + num_fields_depth,
        )
        print(cells_offset)
        self.__draw_cells_on_playbord(cells_offset)

    '''numbering/indexing cells'''

    def __create_num_fields(self):
        n_lines = pg.Surface((self.__cells * self.__size, self.__size // 3))
        n_rows = pg.Surface((self.__size // 3, self.__cells * self.__size))
        for i in range(self.__cells):
            letter = fnt_obj.render(chr(65 + i), True, (255, 255, 255))
            number = fnt_obj.render(str(cells - i), True, (255, 255, 255))
            n_lines.blit(letter, (
                i * cell_size + (cell_size - letter.get_rect().width) // 2,
                (n_lines.get_height() - letter.get_rect().height) // 2
            ))
            n_rows.blit(number, (
                (n_rows.get_width() - letter.get_rect().width) // 2,
                i * cell_size + (cell_size - number.get_rect().height) // 2
            ))
        return n_rows, n_lines

    '''creating cells based on color'''

    def __create_all_cells(self):
        group = pg.sprite.Group()
        cell_color_index = 0
        for y in range(self.__cells):
            for x in range(self.__cells):
                cell = Cell(
                    cell_color_index,
                    self.__size,
                    (x, y),
                    LTRS[x] + str(self.__cells - y)
                )

                group.add(cell)
                cell_color_index ^= True
            cell_color_index ^= True
        return group

    '''def create_cells_and_name(self):
        cells_and_name = {}
        for cell in self.__all_cells:
            cells_and_name['cell.field_name'] = cell
        return cells_and_name'''

    '''rendering of created cells'''

    def __draw_cells_on_playbord(self, offset):
        for cell in self.__all_cells:
            cell.rect.x += offset[0]
            cell.rect.y += offset[1]
        self.__all_cells.draw(self.__screen)

    '''rendering of created pieces'''

    def __draw_all_pieces(self):
        self.__setup_board()
        self.__all_pieces.draw(self.__screen)

    def __setup_board(self):
        for j, row in enumerate(self.__table):
            for i, field_value in enumerate(row):
                if field_value != 0:
                    piece = self.__create_piece(field_value, (j, i))  # anvan arajin tary u matricum ira dirqy
                    #piece.allowed_steps.add(piece.right_steps(piece.rect.x, piece.rect.y))
                    self.__all_pieces.add(piece)
        for piece in self.__all_pieces:
            for cell in self.__all_cells:
                if piece.field_name == cell.field_name:
                    piece.rect = cell.rect
                    #piece.right_steps(cell.field_name)

    '''def get_allowed_cells_for_steps(self):
        for piece in self.__all_pieces:
            for cell in self.__all_cells:
                if piece.right_steps(cell.field_name, cell.rect.x, cell.rect.y):'''

    def __create_piece(self, piece_symbol: str, table_coord: tuple):
        field_name = self.__to_field_name(table_coord)
        piece_tuple = self.__pieces_types[piece_symbol]     # veragrvuma ed figuri anuny u guyni arajin tary
        classname = globals()[piece_tuple[0]]
        return classname(self.__size, piece_tuple[1], field_name)

    '''deriving cell names by matrix coordinates'''

    def __to_field_name(self, table_coord: tuple):
        return LTRS[table_coord[1]] + str(self.__cells - table_coord[0])

    '''mouse click and picking cell'''

    def btn_down(self, button_type: int, position: tuple):
        self.__pressed_cell = self.__get_cell(position)

    def btn_up(self, button_type: int, position: tuple):
        released_cell = self.__get_cell(position)
        #released_piece = self.__get_piece(position)
        #print(released_cell.rect.x, released_cell.rect.y)
        if (released_cell is not None) and (released_cell == self.__pressed_cell):
            if button_type == 1:
                #if released_piece in right_steps(released_cell.rect.x, released_cell.rect.y):
                self.__pick_cell(released_cell)
            else:
                pass
        self.__grand_update()

    '''def __get_piece(self, position: tuple):
        for piece in self.__all_pieces:
            if piece.rect.collidepoint(position):
                return piece
        return None'''

    def __get_cell(self, position: tuple):
        for cell in self.__all_cells:
            if cell.rect.collidepoint(position):
                return cell
        return None

    def __pick_cell(self, cell):
        if self.__picked_piece is None:
            for piece in self.__all_pieces:
                if piece.field_name == cell.field_name:
                    self.__picked_piece = piece
                    piece.color_picked_piece = piece.color
                    break
        else:
            for piece in self.__all_pieces:
                if piece.field_name == cell.field_name and self.__picked_piece != piece:
                    if self.__picked_piece.color_picked_piece != piece.color:
                        #if piece in Pieces.allowed_cells_for_steps:
                            piece.kill()

                    else:
                        self.__picked_piece = None
                        break
            else:
                #if cell in piece.allowed_steps:  ###########
                self.__picked_piece.rect = cell.rect
                self.__picked_piece.field_name = cell.field_name
                self.__picked_piece = None

    def __grand_update(self):
        self.__all_cells.draw(self.__screen)
        self.__all_pieces.draw(self.__screen)
        pg.display.update()


class Cell(pg.sprite.Sprite):
    def __init__(self, color_index: int, size: int, coords: tuple, name: str):
        super().__init__()
        x, y = coords
        # self.__picked = False
        self.color = color_index
        self.field_name = name
        self.image = pg.image.load(COLORS_FOR_BOARD[color_index])
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = pg.Rect(x * size, y * size, size, size)


from pieces import *
from config import *
import pygame as pg

pg.init()
fnt_obj = pg.font.Font(pg.font.get_default_font(), fnt_size)
screen = pg.display.set_mode(win_size)
fnt_for_check = pg.font.Font(pg.font.get_default_font(), 60)
check = fnt_for_check.render('Check !', True, (0, 0, 0))


class Chessboard:
    def __init__(self, parent_surface: pg.Surface):
        self.__index_for_step = 0
        self.__next_step = next_step[self.__index_for_step]
        self.cells_and_name = {}
        self.pieces_and_name = {}
        self.__screen = parent_surface
        self.__table = board
        self.__cells = cells
        self.__size = cell_size
        self.__pieces_types = PIECES_TYPES
        self.__pressed_cell = None
        self.__picked_piece = None
        self.__rect_for_cancel = None
        self.__field_name_for_cancel = None
        self.__all_cells = pg.sprite.Group()
        self.__all_pieces = pg.sprite.Group()
        self.__all_areas = pg.sprite.Group()
        self.__cells_and_pieces = []
        self.__prepare_screen()
        self.__draw_playboard()
        self.__draw_all_pieces()
        self.__king_field_name = {'w': 'E1', 'b': 'E8'}
        pg.display.update()

    '''  background image   '''

    def __prepare_screen(self):

        back_img = pg.image.load(IMG_PATH)
        back_img = pg.transform.scale(back_img, win_size)
        self.__screen.blit(back_img, (0, 0))

    def __draw_playboard(self):
        total_width = self.__cells * self.__size
        num_fields = self.__create_num_fields()
        self.__all_cells = self.__create_all_cells()
        num_fields_depth = num_fields[0].get_width()
        playboard_view = pg.Surface((
            2 * num_fields_depth + total_width,
            2 * num_fields_depth + total_width
        ))

        playboard_view.blit(num_fields[0],
                            (0, num_fields_depth))
        playboard_view.blit(num_fields[0],
                            (num_fields_depth + total_width, num_fields_depth))
        playboard_view.blit(num_fields[1],
                            (num_fields_depth, 0))
        playboard_view.blit(num_fields[1],
                            (num_fields_depth, num_fields_depth + total_width))
        playboard_rect = playboard_view.get_rect()
        playboard_rect.x += (self.__screen.get_width() - playboard_rect.width) // 2
        playboard_rect.y += (self.__screen.get_height() - playboard_rect.height) // 2
        self.__screen.blit(playboard_view, playboard_rect)
        cells_offset = (
            playboard_rect.x + num_fields_depth,
            playboard_rect.y + num_fields_depth,
        )
        self.__draw_cells_on_playbord(cells_offset)

    '''numbering/indexing cells'''

    def __create_num_fields(self):
        n_lines = pg.Surface((self.__cells * self.__size, self.__size // 3))
        n_rows = pg.Surface((self.__size // 3, self.__cells * self.__size))
        for i in range(self.__cells):
            letter = fnt_obj.render(chr(65 + i), True, (255, 255, 255))
            number = fnt_obj.render(str(cells - i), True, (255, 255, 255))
            n_lines.blit(letter, (
                i * cell_size + (cell_size - letter.get_rect().width) // 2,
                (n_lines.get_height() - letter.get_rect().height) // 2
            ))
            n_rows.blit(number, (
                (n_rows.get_width() - letter.get_rect().width) // 2,
                i * cell_size + (cell_size - number.get_rect().height) // 2
            ))
        return n_rows, n_lines

    '''creating cells based on color'''

    def __create_all_cells(self):
        group = pg.sprite.Group()
        cell_color_index = 0
        for y in range(self.__cells):
            for x in range(self.__cells):
                cell = Cell(
                    cell_color_index,
                    self.__size,
                    (x, y),
                    LTRS[x] + str(self.__cells - y)
                )
                self.cells_and_name[LTRS[x] + str(self.__cells - y)] = cell
                group.add(cell)
                cell_color_index ^= True
            cell_color_index ^= True
        return group

    def __draw_cells_on_playbord(self, offset):
        for cell in self.__all_cells:
            cell.rect.x += offset[0]
            cell.rect.y += offset[1]
        self.__all_cells.draw(self.__screen)

    '''rendering of created pieces'''

    def __draw_all_pieces(self):
        self.__setup_board()
        self.__all_pieces.draw(self.__screen)
        self.__cells_and_pieces = self.__create_cells_and_pieces()

    def __setup_board(self):
        for j, row in enumerate(self.__table):
            for i, field_value in enumerate(row):
                if field_value != 0:
                    piece = self.__create_piece(field_value, (j, i))
                    self.__all_pieces.add(piece)
        self.__cells_and_pieces = self.__create_cells_and_pieces()
        for piece in self.__all_pieces:
            for cell in self.__all_cells:
                if piece.field_name == cell.field_name:
                    piece.rect = cell.rect

    def __create_piece(self, piece_symbol: str, table_coord: tuple):
        field_name = self.__to_field_name(table_coord)
        piece_tuple = self.__pieces_types[piece_symbol]
        name = piece_tuple[0]
        classname = globals()[name]
        return classname(self.__size, piece_tuple[1], field_name, name)

    def __create_piece_double(self, field_name, color, name):
        classname = globals()[name]
        return classname(self.__size, color, field_name)

    '''deriving cell names by matrix coordinates'''

    def __to_field_name(self, table_coord: tuple):
        return LTRS[table_coord[1]] + str(self.__cells - table_coord[0])

    '''mouse click and picking cell'''

    def btn_down(self, position: tuple):
        self.__pressed_cell = self.__get_cell(position)

    def btn_up(self, button_type: int, position: tuple):
        released_cell = self.__get_cell(position)
        if (released_cell is not None) and (released_cell == self.__pressed_cell):
            if button_type == 1:
                self.__pick_cell(released_cell)
            else:
                pass
        self.__grand_update()

    def __get_cell(self, position: tuple):
        for cell in self.__all_cells:
            if cell.rect.collidepoint(position):
                return cell
        return None

    def __pick_cell(self, cell):
        self.__all_areas.empty()
        if self.__picked_piece is None:
            for piece in self.__all_pieces:
                if piece.field_name == cell.field_name:
                    pick = Area(cell)
                    self.__all_areas.add(pick)
                    self.__picked_piece = piece
                    piece.color_picked_piece = piece.color
                    break
            if self.__picked_piece is not None:
                self.__create_allowed_cells_for_steps()
        else:
            self.__grand_update()
            if self.__picked_piece.color_picked_piece == self.__next_step:
                if cell in self.__picked_piece.allowed_cells_for_steps[self.__picked_piece.color_picked_piece]:
                    if self.__picked_piece.field_name == self.__king_field_name[self.__picked_piece.color_picked_piece]:
                        if self.__is_check_moving_the_king(self.__picked_piece.color_picked_piece, cell):
                            self.__picked_piece = None
                            return
                        else:
                            self.__king_field_name[self.__picked_piece.color_picked_piece] = cell.field_name
                            self.__index_for_step ^= True
                            self.__next_step = next_step[self.__index_for_step]
                    for piece in self.__all_pieces:
                        if piece.field_name == cell.field_name:
                            if self.__picked_piece != piece and self.__picked_piece.color_picked_piece != piece.color:
                                self.__move_piece(cell)
                                step = True
                                """այս ֆունկցիան նրա համար է որ շախ հայտարարած ֆիգուռին կարողանանք ուտել"""
                                if self.__during_check_kill(cell, self.__picked_piece.color_picked_piece):
                                    self.__cancel_move_piece()
                                    step = False
                                    self.__picked_piece = None
                                    break
                                piece.kill()
                                if self.__picked_piece.field_name == \
                                        self.__king_field_name[self.__picked_piece.color_picked_piece]:
                                    self.__picked_piece = None
                                    return
                                if step:
                                    self.__index_for_step ^= True
                                    self.__next_step = next_step[self.__index_for_step]
                                self.__picked_piece = None
                                return
                            else:
                                self.__picked_piece = None
                                break
                    else:
                        if self.__picked_piece.name == 'Pawn':
                            if not self.__move_pawn(cell):
                                self.__picked_piece = None
                                return
                        self.__move_piece(cell)
                        step = True
                        if self.__is_check(
                                self.__picked_piece.color_picked_piece):
                            self.__cancel_move_piece()
                            step = False
                        self.__picked_piece = None
                        if step:
                            self.__index_for_step ^= True
                            self.__next_step = next_step[self.__index_for_step]
                else:
                    self.__picked_piece = None
                    self.__create_allowed_cells_for_steps()
            else:
                self.__picked_piece = None

    def __move_pawn(self, cell):
        if self.__picked_piece.color_picked_piece == 'w':
            if cell.field_name == LTRS[LTRS.index(self.__picked_piece.field_name[0]) - 1] + str(
                    int(self.__picked_piece.field_name[1]) + 1):
                for piece in self.__all_pieces:
                    if piece.color != 'w' and piece.field_name == cell.field_name:
                        self.__move_piece(cell)
                        piece.kill()
                        return True
                return False

            if cell.field_name == chr(ord(self.__picked_piece.field_name[0]) + 1) + str(
                    int(self.__picked_piece.field_name[1]) + 1):
                for piece in self.__all_pieces:
                    if piece.color != 'w' and piece.field_name == cell.field_name:
                        self.__move_piece(cell)
                        piece.kill()
                        return True
                return False

        if self.__picked_piece.color_picked_piece == 'b':
            if cell.field_name == LTRS[LTRS.index(self.__picked_piece.field_name[0]) - 1] + str(
                    int(self.__picked_piece.field_name[1]) - 1):
                for piece in self.__all_pieces:
                    if piece.color != 'b' and piece.field_name == cell.field_name:
                        self.__move_piece(cell)
                        piece.kill()
                        return True
                return False

            if cell.field_name == chr(ord(self.__picked_piece.field_name[0]) + 1) + str(
                    int(self.__picked_piece.field_name[1]) - 1):
                for piece in self.__all_pieces:
                    if piece.color != 'b' and piece.field_name == cell.field_name:
                        self.__move_piece(cell)
                        piece.kill()
                        return True
                return False
        return True

    def __move_king(self, cell):
        self.__grand_update()
        if self.__picked_piece.field_name == self.__king_field_name[self.__picked_piece.color_picked_piece]:
            if self.__is_check_moving_the_king(self.__picked_piece.color_picked_piece, cell):
                self.__picked_piece = None
                return True
        return False

    def __move_piece(self, cell):
        self.__rect_for_cancel = self.__picked_piece.rect
        self.__field_name_for_cancel = self.__picked_piece.field_name
        self.__picked_piece.rect = cell.rect
        self.__picked_piece.field_name = cell.field_name
        self.__create_allowed_cells_for_steps()

    def __cancel_move_piece(self):
        self.__picked_piece.rect = self.__rect_for_cancel
        self.__picked_piece.field_name = self.__field_name_for_cancel

    def __during_check_kill(self, cell, color_moving_cell):
        self.__grand_update()
        checks = []
        if color_moving_cell == 'w':
            opponent_color = 'b'
        else:
            opponent_color = 'w'
        for piece in self.__all_pieces:
            if piece.color == opponent_color:
                for allowed_cell in piece.allowed_cells_for_steps[opponent_color]:
                    if allowed_cell.field_name == self.__king_field_name[color_moving_cell]:
                        checks.append(piece.field_name)
        if cell.field_name in checks:
            checks.remove(cell.field_name)
        if len(checks) > 0:
            return True
        return False

    def __is_check(self, movable_piece_color):
        self.__grand_update()
        self.__create_allowed_cells_for_steps()
        if movable_piece_color == 'w':
            opponent_color = 'b'
        else:
            opponent_color = 'w'
        for piece in self.__all_pieces:
            if piece.color == opponent_color:
                for allowed_cell in piece.allowed_cells_for_steps[opponent_color]:
                    if allowed_cell.field_name == self.__king_field_name[movable_piece_color]:
                        return True
        return False

    def __is_check_moving_the_king(self, color_of_king, cell):
        self.__grand_update()
        self.__create_allowed_cells_for_steps()
        if color_of_king == 'w':
            opponent_color = 'b'
        else:
            opponent_color = 'w'
        for piece in self.__all_pieces:
            if piece.color == opponent_color:
                for allowed_cell in piece.allowed_cells_for_steps[opponent_color]:
                    if allowed_cell.field_name == cell.field_name:
                        return True
        return False

    def __create_allowed_cells_for_steps(self):
        self.__grand_update()
        for piece in self.__all_pieces:
            piece.allowed_cells_for_steps['w'] = []
            piece.allowed_cells_for_steps['b'] = []
            piece.right_steps(piece.field_name, self.cells_and_name, self.__all_pieces, piece.color,
                              self.__cells_and_pieces)

    def __create_cells_and_pieces(self):
        lst = []
        for cell in self.__all_cells:
            for piece in self.__all_pieces:
                if cell.field_name == piece.field_name:
                    lst.append(cell.field_name)
        return lst

    def __grand_update(self):
        self.__all_cells.draw(self.__screen)
        self.__all_pieces.draw(self.__screen)
        self.__cells_and_pieces = self.__create_cells_and_pieces()
        self.__all_areas.draw(self.__screen)
        pg.display.update()


class Cell(pg.sprite.Sprite):
    def __init__(self, color_index: int, size: int, coords: tuple, name: str):
        super().__init__()
        x, y = coords
        self.color = color_index
        self.field_name = name
        self.image = pg.image.load(COLORS_FOR_BOARD[color_index])
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = pg.Rect(x * size, y * size, size, size)


class Area(pg.sprite.Sprite):
    def __init__(self, cell: Cell):
        super().__init__()
        coords = (cell.rect.x, cell.rect.y)
        area_size = (cell.rect.width, cell.rect.height)
        self.image = pg.Surface(area_size).convert_alpha()
        self.image.fill(ACTIVE_COLOR)
        self.rect = pg.Rect(coords, area_size)
        self.field_name = cell.field_name
