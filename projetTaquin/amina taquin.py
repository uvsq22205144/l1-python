import tkinter as tk  #Librairie Tkinter
import random #Fonction pour pouvoir choisir un nombre aléatoirement
from tkinter import messagebox #Ouvrir un pop-up avec une information

LARGEUR = 400 
HAUTEUR = 400 
mouvement = 0 
POLICE=('Arial', 27, 'bold') #Police d'écriture

taquin=[[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, None]]

taquinprecedent=[]
#Fonction pour pouvoir annuler un mouvement et le remplacer par la matrice precedente.

taquin_victoire=[[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15,None]]
#Le resultat obtenu pour gagner la partie.

# Création des tuiles
tuile=[None for i in range(17)] #Création des tuiles vides qu'on rempli par la suite avec les numeros.
def tableaudejeu():
    global taquin,i_vide,j_vide
    for i in range(4):
        for j in range(4):
            x=100*j
            y=100*i 
            debutcarre=(x,y)
            fincarre= (x+100, y+100)
            milieucarre=(x+50, y+50) #Creer une variable qui represente la moitié du carré pour pouvoir y mettre le numero, centré.
            numero=taquin[i][j]
            if numero==16: 
                carre=canvas.create_rectangle(debutcarre, fincarre, fill="gray85")
                chiffre=canvas.create_text(milieucarre, text=numero, fill="gray85", font=POLICE)
                tuile[numero]=(carre, chiffre)
                i_vide=i
                j_vide=j
            else:
                carre=canvas.create_rectangle(debutcarre, fincarre, fill="pink")
                chiffre=canvas.create_text(milieucarre, text=numero, fill="purple", font=POLICE) #Integrer le numero dans les tuiles
                tuile[numero]=(carre, chiffre) 
    



#Pour déplacer les tuiles
def deplacer():
    global taquin, taquin_victoire,mouvement,taquinprecedent
    if taquin == taquin_victoire:
        messagebox.showinfo("Bravo, tu as gagné!")
        messagebox.showinfo("Victoire","Veuillez appuyer sur le bouton Mélanger pour rejouer une partie.")
        

    else:
        for i in range(4):
            for j in range(4):
                taquinprecedent.append(taquin[i][j])
        


# Les boutons de l'interface graphique:

def fermer_partie():
    racine.destroy()


def melanger():
    global taquin
    taquin[3][3]=16 #Pour placer le carré vide en bas à droite.
    numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for i in range(3): #Melange les 4 colonnes des 3 premières lignes de la matrice
        for j in range(4):
            x=random.randint(0,len(numeros)-1)
            taquin[i][j]=numeros[x]
            del numeros[x]
    for j in range(3): #Melange les 3 colonnes de la dernière ligne de la matrice, car la toute derniere case est vide.
        x=random.randint(0,len(numeros)-1)
        taquin[3][j]=numeros[x]
        del numeros[x]
    tableaudejeu()  #Actualiser le tableau.


def sauvegarde():
    fic=open("sauvegarde.txt", "w")
    for i in range(4):
        for j in range(4):
            fic.write(str(taquin[i][j]) + "\n")
    fic.close()
    messagebox.showinfo("Sauvegarde", "La Sauvegarde est réussie.") 


def charger_partie():
    global taquin
    fic=open("sauvegarde.txt", "r")
    ligne=fic.readlines() #ligne devient une liste contenant chaque ligne du fichier.
    l=0 
    for i in range(4): 
        for j in range(4):
            taquin[i][j]=int(ligne[l]) #on remplace taquin[0][0] par le premier élément de la liste et ainsi de suite.
            l=l+1 #on passe au prochain élément de la liste.
    fic.close()
    tableaudejeu() #Actualiser le tableau.


def annuler():
    global taquin, taquinprecedent,mouvement
    if mouvement>0:
        a=0 
        for i in range(4): 
            for j in range(4):
                taquin[i][j]=int(taquinprecedent[a]) #on remplace taquin[0][0] par le premier élément de la liste et ainsi de suite.
                a=a+1 #on passe au prochain élément de la liste.
        tableaudejeu() #Redessine le tableau avec la nouvelle matrice, actualise le tableau.
    else:
        messagebox.showerror("Annuler Mouvement", "Vous n'avez aucun mouvement pouvant être annulé.")
    tableaudejeu()  #Actualiser le tableau.
    

     
# création des boutons
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="pink", width=LARGEUR, height=HAUTEUR)
racine.title("Jeu du Taquin")
melanger() #Pour lancer le jeu melangé au demarrage.

bouton_fermer = tk.Button(racine, text="Fermer",command=fermer_partie)
bouton_melanger = tk.Button(racine, text="Melanger",command=melanger)
bouton_sauvegarder= tk.Button(racine, text="Sauvegarder", command=sauvegarde)
bouton_charger = tk.Button(racine, text="Charger",command=charger_partie)
bouton_annuler = tk.Button(racine, text="Annuler mouvement",command=annuler)


#Positionnement des Widgets
bouton_sauvegarder.grid(row=7, column=0, pady=2, padx=2,sticky=tk.W+tk.E, columnspan=1)
bouton_charger.grid(row=7, column=1, pady=2, padx=2,sticky=tk.W+tk.E, columnspan=1)
bouton_annuler.grid(row=8, column=0, pady=2, padx=2,sticky=tk.W+tk.E, columnspan=1)
bouton_fermer.grid(row=10, column = 0, pady=2, padx=2, columnspan=2, sticky=tk.W+tk.E)
bouton_melanger.grid(row=9, column=0, pady=2, padx=2, columnspan=2,sticky=tk.W+tk.E)
canvas.grid(row = 0, column = 0, columnspan=2, sticky=tk.W+tk.E) 

racine.columnconfigure(1, minsize=200) #permet au canvas d'être centré avec les boutons






racine.mainloop()