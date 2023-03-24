import tkinter as tk
import random

class Taquin(tk.Frame):
    def __init__(self, parent, nb_lignes=int (4) ,nb_colonnes=4,size=32):
        self.nb_lignes = nb_lignes
        self.nb_colonnes = nb_colonnes
        self.size = size
        self.tiles = []
        self.tiles_pos = {}
        self.empty_pos = None
        self.moves = 0
        self.parent = parent
        self.canvas_width = nb_colonnes * size
        self.canvas_height = nb_lignes * size
         
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,width=self.canvas_width, height=self.canvas_height, background="white")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        self.canvas.bind("<Button-1>", self.click)
        self.init_board()
        self.shuffle_board()

    def init_board(self):
        for nb_lignes in range(self.nb_lignes):
            for nb_colonnes in range(self.nb_colonnes):
                tile_number = nb_colonnes + nb_lignes * self.nb_colonnes + 1
                if tile_number == self.nb_lignes * self.nb_colonnes:
                    tile = None
                else:
                    tile = tk.PhotoImage(file=f"{tile_number}.gif")
                tile_label = tk.Label(image=tile, borderwidth=0)
                tile_label.image = tile
                x = nb_colonnes * self.size
                y = nb_lignes * self.size
                self.canvas.create_image(x, y, image=tile, anchor="nw")
                self.tiles.append(tile_label)
                self.tiles_pos[tile_number] = (nb_lignes, nb_colonnes)
        self.empty_pos = self.tiles_pos[self.nb_lignes * self.nb_colonnes]
# 1er def initialisation des cases (dimensions,nombre de colonnes et ligns etc)
# 2eme def initialisation du plateau de jeu 