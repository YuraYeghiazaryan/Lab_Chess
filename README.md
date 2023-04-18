# Lab_Chess

Welcome to my GitHub repository for the Chess project! 
This project allows users to play a game of chess in a graphical interface.

To run the project, simply execute the exe.py file. 
The game window will open and the game will always start
with the white pieces at the bottom and white making the first move. 
Each player must make their moves in order, with one color playing at a time.
When a piece is selected, its field turns red and the player must then select 
a square to move the piece to. If the selected square does not correspond to 
the rules of the chess moves, the selected piece is canceled.

The pieces in the game are implemented as classes in the pieces.py file, 
with each piece having its own logic to move correctly. 
The config.py file contains all the necessary data for the optimal operation of the program, 
while the chess_items.py file coordinates the work of the entire project.

