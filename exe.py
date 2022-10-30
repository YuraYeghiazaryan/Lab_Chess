import chess_items
import pygame as pg
from config import *


clock = pg.time.Clock()
screen = pg.display.set_mode(win_size)
pg.display.set_caption("Pair to pair Chess")

chessboard = chess_items.Chessboard(screen)


run = True
while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False

        if event.type == pg.MOUSEBUTTONDOWN:
            chessboard.btn_down(event.pos)
        if event.type == pg.MOUSEBUTTONUP:
            chessboard.btn_up(event.button, event.pos)
