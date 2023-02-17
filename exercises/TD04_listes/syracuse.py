#question 2
def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    lys = [n]
    while n != 1 :  
        if n % 2 == 0 :
            n = n // 2 
        else : 
            n = n*3 + 1 
        lys.append(n)
    
    return lys
print(syracuse(3))

#question 3
def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range (1, n_max +1) :
        syracuse(i)
    return True
print(testeConjecture(10000))

#question4/5
def tempsVol(n):
    """ Retourne le temps de vol de n """
    return(len(syracuse(n))-1)
print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return[tempsVol(i)for i in range (1, n_max + 1)]
print(tempsVolListe(100))

#question 6 

liste_temps = tempsVolListe(10000)
temps_max = max(liste_temps)
print("L'entier", liste_temps.index(temps_max) + 1, "a le plus grand temps de vol a", temps_max)

#question 7 


