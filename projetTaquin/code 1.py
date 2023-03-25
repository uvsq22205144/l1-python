import tkinter as tk
from tkinter import *
import random

# Création de la fenêtre principale
root = Tk()
root.title("Jeu du Taquin")
label = Label(root, text="Commences à jouer !")
label.pack()

# Définition du plateau de jeu
board = [[6, 7, 4, 8], [5, 15, 13, 2], [12, 14, 9, 1], [3, 11, 10, None]]

# Création du canvas
cnv = Canvas(root, width=400, height=400)
cnv.pack()

# Fonction pour créer le plateau de jeu
def create_board():
    cnv.delete(ALL) # Effacer le canvas existant
    FONT = ('Ubuntu', 27, 'bold')
    for i in range(4):
        for j in range(4):
            x, y = 100*j, 100*i
            A, B, C = (x, y), (x+100, y+100), (x+50, y+50)
            cnv.create_rectangle(A, B, fill="pink")
            if board[i][j] is not None:
                cnv.create_text(C, text=board[i][j], fill="purple", font=FONT)

# Fonction pour trouver la position de la case vide
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is None:
                return i, j
    return None

# Mélange des cases du plateau + création du bouton pour mélanger 
def shuffle_board():
    empty_row, empty_col = find_empty(board)
    moves = ["up", "down", "left", "right"]
    random.shuffle(moves)
    for move in moves:
        new_row, new_col = empty_row, empty_col
        if move == "up":
            new_row -= 1
        elif move == "down":
            new_row += 1
        elif move == "left":
            new_col -= 1
        elif move == "right":
            new_col += 1
        if new_row >= 0 and new_row < len(board) and new_col >= 0 and new_col < len(board[0]):
            board[empty_row][empty_col], board[new_row][new_col] = board[new_row][new_col], board[empty_row][empty_col]
            empty_row, empty_col = new_row, new_col
    create_board()

shuffle_button = Button(root, text="Mélanger", command=shuffle_board)
shuffle_button.pack()

create_board()
root.mainloop()

