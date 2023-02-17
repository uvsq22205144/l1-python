#question 1 
34

#question 2 
carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
print(carre_mag)

#question 3
carre_pas_mag = [ligne[:] for ligne in carre_mag]
carre_pas_mag[3][2] = 7
print(carre_pas_mag)

#question 4
def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for ligne in carre :
        print(ligne)
    print()
afficheCarre(carre_mag)
print()
afficheCarre(carre_pas_mag)

#question 5 
def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    somme = sum(carre[0])
    for somme_ligne in carre :
        if somme != sum(somme_ligne) : 
            return -1
    return somme
print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

#question 6 
def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    C1 = [ligne[0] for ligne in carre]
    S1 = sum (C1)
    for nc in range(1,len(carre)) :
        C2 = [ligne [nc] for ligne in carre]
        if S1 != sum(C2) :
            return -1
    return S1
print("test des colonnes")
print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))

#question 7 

def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    d1 = [carre [i][i] for i in range (len(carre))]
    d2 = [carre [i][len(carre)-i-1] for i in range (len(carre))]
    S1 = sum (d1)
    if S1 != sum(d2) :
        return -1
    return S1
print("test des diagonales")
print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))

#question 8 

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    return testLignesEgales(carre) == testColonnesEgales(carre) and testLignesEgales(carre)\
        == testDiagonalesEgales(carre) and testLignesEgales(carre) != -1
print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))

#question 9 

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    liste =[]
    for ligne in carre : 
        liste.extend(ligne)
    for i in range (1, len(carre)*len(carre) + 1) :
        if i not in liste : 
            return False 
    return True
print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))