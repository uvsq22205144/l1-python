import tkinter as tk
import random
from tkinter import filedialog
#from tkinter import messagebox



# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu du Taquin")

# Définition du plateau de jeu
board = [[6, 7, 4, 8], [5, 15, 13, 2], [12, 14, 9, 1], [3, 11, 10, None]]
win = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, None]]
moves = 0
misplaced = 0

# Création du canvas
cnv = tk.Canvas(root, width=400, height=400)
cnv.pack()

moves_history=[]

# Fonction pour savoir si le jeu est résolvable
def is_solvable(board):
    flat_board = [item for sublist in board for item in sublist]
    inversion_count = 0
    for i in range(len(flat_board)):
        for j in range(i+1, len(flat_board)):
            if flat_board[i] and flat_board[j] and flat_board[i] > flat_board[j]:
                inversion_count += 1
    if inversion_count % 2 == 0:
        return True
    else:
        return False
        
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
    if board == win:
        show_win_message()


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
    if not is_solvable(board):
        log_text.insert(tk.END, "Le plateau est insolvable !\n")
        return
    else :
        log_text.insert(tk.END, "Tu peux jouer ! Le plateau est résolvable.\n")
        
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

#Fonction bravo 
def show_win_message():
    global game_over
    game_over = True
    cnv.create_text(200, 200, text="Bravo, tu as gagné !!!", fill="gray10", font=("Arial", 20, "bold"))

#Fonction sauvegarde
def save_config():
    config = entry.get()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            file.write(config)

# Fonction pour recharger une partie
def load_config():
     # ouvrir le fichier 
    file_path = filedialog.askopenfilename(defaultextension=".txt")
    if file_path:
        # lire la configuration dupuis le fichier 
        with open(file_path, "r") as file:
            config_data = file.read()
        # mettre les donnees dans une liste 
        config = [int(x) for x in config_data.split()]
        
        return config
    else:
        # ne rien retournez si le fichier est vide 
        return []



#Boutons et autres commandes 

shuffle_button = tk.Button(root, text="Mélanger", command=shuffle_board, bg ="DarkOrchid1") #bouton pour melanger
shuffle_button.pack()

cnv.bind("<Button-1>", move_tile) #bouton qui reconnait le clic de la souris 

undo_button = tk.Button(root, text="Annuler", command=undo_move, bg="DarkOrchid1")# bouton pour annuler
undo_button.pack()

log_text = tk.Text(root, width=50, height=10)
log_text.pack()

entry= tk.Entry(root)
entry.pack()

save_button = tk.Button(root, text="Sauvegarder", command=save_config)
save_button.pack()

load_button = tk.Button(root, text="Afficher", command=load_config)
load_button.pack()


create_board()
root.mainloop()
