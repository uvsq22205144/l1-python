import tkinter as tk
import random

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu du Taquin")

# Définition du plateau de jeu
board = [[6, 7, 4, 8], [5, 15, 13, 2], [12, 14, 9, 1], [3, 11, 10, None]]

moves = 0
misplaced = 0

# Création du canvas
cnv = tk.Canvas(root, width=400, height=400)
cnv.pack()

# Fonction pour créer le plateau de jeu
def create_board():
    global misplaced
    cnv.delete(tk.ALL) # Effacer le canvas existant
    FONT = ('Arial', 27, 'bold')
    misplaced = 0
    for i in range(4):
        for j in range(4):
            x, y = 100*j, 100*i
            A, B, C = (x, y), (x+100, y+100), (x+50, y+50)
            if board[i][j] is not None:
                cnv.create_rectangle(A, B, fill="pink")
                cnv.create_text(C, text=board[i][j], fill="purple", font=FONT)
                if board[i][j] != i*4+j+1:
                    misplaced += 1
            else:
                cnv.create_rectangle(A, B, fill="white")

# Fonction pour trouver la position de la case vide
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is None:
                return i, j
    return None

# Mélange des cases du plateau + création du bouton pour mélanger 
def shuffle_board():
    global board, moves
    last_element = board[-1]  # Extraire le dernier élément
    shuffled = board[:-1]  # Copier la liste sans le dernier élément
    random.shuffle(shuffled)  # Mélanger la liste sans le dernier élément
    shuffled.append(last_element)  # Insérer le dernier élément à sa place
    board = shuffled
    moves = 0
    create_board()

shuffle_button = tk.Button(root, text="Mélanger", command=shuffle_board)
shuffle_button.pack()

# Fonction pour faire bouger les cases 
def move(direction):
    global moves, misplaced
    i, j = find_empty(board)
    if direction == "up":
        if i < 3 and board[i+1][j] is None:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  
            moves += 1
            misplaced += 1 if board[i][j] != i*4+j+1 else 0
    elif direction == "down":
        if i > 0 and board[i-1][j] is None:
            board[i][j], board[i-1][j] = board[i-1][j], board[i][j]
            moves += 1
            misplaced += 1 if board[i][j] != i*4+j+1 else 0
    elif direction == "left":
        if j < 3 and board[i][j+1] is None:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            moves += 1
            misplaced += 1 if board[i][j] != i*4+j+1 else 0
    elif direction == "right":
        if j > 0 and board[i][j-1] is None:
            board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
            moves += 1
            misplaced += 1 if board[i][j] != i*4+j+1 else 0

    create_board() 

# Fonction pour gérer les événements clavier
def key_pressed(event):
    if event.keysym == "Up":
        move("up")
    elif event.keysym == "Down":
        move("down")
    elif event.keysym == "Left":
        move("left")
    elif event.keysym == "Right":
        move("right")

root.bind("<KeyPress>", key_pressed)
root.focus_set()

create_board()
root.mainloop()

 
