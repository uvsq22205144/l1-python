# Projet taquin

## Biologie Informatique TD2, groupe projet 6 : AZZOPARDI Laly, DERBAL Amina & MADANI FOUATIH Iram


### Code source disponible sur `https://github.com/uvsq22205144/l1-python`


### Explications des règles du Taquin

Le Taquin est un puzzle constitué de 15 carrés numérotés de 1 à 15 qui peuvent coulisser horizontalement et verticalement à l’intérieur d’un cadre carré
qui contient un emplacement vide. Un carré ne peut coulisser que si l’emplacement voisin dans la direction choisie est vide.
#### L’objectif est de déplacer les carrés de manière à obtenir la configuration donnée à la figure 1 : 


<img src="https://raw.githubusercontent.com/uvsq22205144/l1-python/master/projetTaquin/IMG_2323.jpg" alt="taquin" width="250" height="250">



En général, le jeu démarre à partir d’une configuration choisie au hasard comme illustré à la figure 2. Il
faut noter que certaines configurations de départ n’admettent pas de solution. 


<img src="https://raw.githubusercontent.com/uvsq22205144/l1-python/master/projetTaquin/IMG_2324.jpg" alt="taquin" width="250" height="250">

### Figure 2

Il nous a été demandé de fournir une interface graphique permettant de jouer au jeu du taquin. La configuration de départ doit être choisie au hasard, mais la case libre doit être en bas à droite. L’interface graphique devait être Tkinter.

##### Notre programme doit également permettre de :

* sauvegarder une partie en cours puis de la recharger;
* revenir en arrière, c’est-à-dire annuler des déplacements de carrés

##  Utilisation du programme 


・Def is_solvable(): 

→Cette fonction vérifie si un jeu de taquin est résoluble ou non en comptant le nombre d'inversions dans le tableau.
On commence par aplatir le tableau en une seule liste pour faciliter le comptage des inversions puis on compares les éléments entre eux. Une inversion se produit si pour chaque pairs d’elements (i,j) ou indice de l’élément i < indice élément j, l’élément i est plus grand que l’element j. 
Si le nombre d'inversions est pair, cela signifie que le puzzle est résoluble.



・Def create_board (): 

→cette fonction a pour but de créer une grille du jeu, on boucle sur toutes les lignes et colonnes de la grille (4x4) et crée un rectangle à chaque emplacement.
le code écrit le numéro de la case à l'intérieur du rectangle et vérifie si le numéro correspond à sa position dans la grille gagnante (win)



・Def undo_move():

→Cette fonction permet d'annuler le dernier mouvement effectué dans le jeu de taquin.
Cette fonction vérifie le nombre de mouvements jusqu'à présent et si ce nombre est égale a 0, cela signifie qu'il n'y a aucun mouvement à annuler. Sinon, la fonction recherche l'avant-dernier élément dans moves_history et le stock dans une liste. Il supprime le dernier element et met a jour le board. 



・Def shuffle_board():

→la fonction verifier l’état du plateau est renvoie si ce dernier est resoluble ou pas, puis elle recherche la position de la case vide en assignant les coordonnées de cette case à la variable empty_pos.
La fonction place tout les element du plateau a part la case vide dans une liste en utilisant une boucle puis melanger tout les elements de cette liste. 
Ensuite la fonction place touts les elements de la liste mélanger dans l’ordre dans toutes les positions du plateau sauf la position vide. 
La case vide est placée a la dernière case
La fonction create_board est appelée pour afficher le nouveau plateau melanger. 



・Def move_tile(): 

→ cette fonction est appelée a chaque fois qu’on clique sur une tuile du plateau, elle vérifie si la position de la tuile cliquée est échangeable avec la position de la case vide. 
Cette fonction met a jour les variables moves_history en plaçant la nouvelle liste dedans. 
La fonction create_board est appelée pour afficher le nouveau plateau avec les positions échanger. 



・def show_win_message():

→La fonction "show_win_message" est appelée lorsque le joueur réussit à résoudre le puzzle et aligne tous les numéros en ordre croissant de gauche à droite et de haut en bas.



・Def save_config():

→La fonction "save_config()" récupère la configuration de la zone de texte, demande à l'utilisateur de sélectionner un emplacement de fichier et écrit la configuration dans le fichier sélectionné. 

・Def load_config():

→La fonction "load_config()" demande à l'utilisateur de sélectionner un fichier de configuration et affiche la configuration dans une boîte de dialogue.

##  Sources et aides du projet 

* La fonction 'create_board()' a été réussi grâce à l'aide de ce site : http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/taquin/taquin.html pour la création d'une grille de jeu esthétique. 
* Ce même site nous a aussi aidé à comprendre le mouvement des tuiles ce qui nous a permit de faire notre propre fonction 'move_tile(event)'

