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

moves_history=[]

# Fonction pour créer le plateau de jeu
def create_board():
    global misplaced, board, moves_history
    
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
                cnv.create_rectangle(A, B, fill="gray85")
    if len(moves_history) == 0:
        moves_history.append([row[:] for row in board]) # Ajout de l'état initial de la planche

# Fonction pour annuler le dernier mouvement
def undo_move():
    global board, moves, moves_history
    
    if moves == 0 or len(moves_history) < 2:
        print("Aucun mouvement à annuler")
        return
    print("Annulation du dernier mouvement")
    
    last_state = moves_history[-2]
    board = [row[:] for row in last_state]
    moves_history.pop(-1)
    moves -= 1
    create_board()


#Fonction pour mélanger le plateau
def shuffle_board():
    global board, moves
    # Enlever la case vide
    empty_pos = None
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] is None:
                empty_pos = (i, j)
                break
        if empty_pos:
            break
    # Enlever la dernière case (15)
    last_element = board[3][3]
    shuffled = [board[i][j] for i in range(4) for j in range(4) if (i, j) != empty_pos]
    # Mélanger la liste
    random.shuffle(shuffled)
    index = 0
    for i in range(4):
        for j in range(4):
            if (i, j) != empty_pos:
                board[i][j] = shuffled[index]
                index += 1
    # Remettre la case vide
    board[3][3] = last_element
    moves = 0
    create_board()


# Fonction pour déplacer une case
def move_tile(event):
    global moves
    x, y = event.x, event.y
    i, j = y // 100, x // 100
    if i < 3 and board[i+1][j] is None:
        board[i+1][j], board[i][j] = board[i][j], board[i+1][j]
        moves += 1
    elif i > 0 and board[i-1][j] is None:
        board[i-1][j], board[i][j] = board[i][j], board[i-1][j]
        moves += 1
    elif j < 3 and board[i][j+1] is None:
        board[i][j+1], board[i][j] = board[i][j], board[i][j+1]
        moves += 1
    elif j > 0 and board[i][j-1] is None:
        board[i][j-1], board[i][j] = board[i][j], board[i][j-1]
        moves += 1
    moves_history.append([row[:] for row in board])  # Copier une nouvelle liste de board dans moves_history
    create_board()




shuffle_button = tk.Button(root, text="Mélanger", command=shuffle_board, bg ="DarkOrchid1") #bouton pour melanger
shuffle_button.pack()
cnv.bind("<Button-1>", move_tile) #bouton qui reconnait le clic de la souris 
undo_button = tk.Button(root, text="Annuler", command=undo_move, bg="DarkOrchid1")# bouton pour annuler
undo_button.pack()

create_board()
root.mainloop()
