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
    global board
    last_element = board[-1]  # Extraire le dernier élément
    shuffled = board[:-1]  # Copier la liste sans le dernier élément
    random.shuffle(shuffled)  # Mélanger la liste sans le dernier élément
    shuffled.append(last_element)  # Insérer le dernier élément à sa place
    board = shuffled
    create_board()

shuffle_button = Button(root, text="Mélanger", command=shuffle_board)
shuffle_button.pack()

create_board()
root.mainloop()

