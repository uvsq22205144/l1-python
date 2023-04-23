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

##### Tout d'abord, création et initialisation d'une fenêtre et d'un canva (interface graphique : Tkinter)

On commence avec la création d'une fenêtre qu'on nomme "Jeu du Taquin" puis le plateau de jeu est défini comme une liste de listes 'board' contenant des entiers et un None (qui est notre case vide). 
Un objet Canvas est créé avec une taille de 400 x 400 et ajouté à la fenêtre principale à l'aide de la méthode pack().

On continue avec la création de la première fonction 'create_board' initialiser la grille de jeu et les tuiles du Taquin on a définit la police de caractères utilisée pour les chiffres dans le plateau de jeu, c'est Arial en taille 27 et en gras.

##### Mouvements des tuiles 

La fonction 'move_tile(event)' permet de déplacer une tuile en fonction du clic sur le canvas. 

'create_board()': appelle la fonction create_board() pour mettre à jour l'affichage de la grille de jeu avec les modifs des différents déplacements.


##  Sources et aides du projet 

* La fonction 'create_board()' a été réussi grâce à l'aide de ce site : http://pascal.ortiz.free.fr/contents/tkinter/projets_tkinter/taquin/taquin.html pour la création d'une grille de jeu esthétique. 
* Ce même site nous a aussi aidé à comprendre le mouvement des tuiles ce qui nous a permit de faire notre propre fonction 'move_tile(event)'

