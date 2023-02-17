def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0]*24*3600 + temps[1]*3600 + temps[2]*60 + temps[3]

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps)) 

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    j = seconde // (24*3600)
    r = seconde % (24*3600)
    h = r // 3600 
    r = r % 3600
    m = r // 60 
    r = r % 60 
    return (j, h, m, r)
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")

def AffichePluriels (Mots, Nombres) : 
    if Nombres > 0 :
        print("", Nombres, Mots, end = "")
    if Nombres > 1 : 
        print("s", end = "")
def AfficheTemps (Temps) : 
    AffichePluriels("Jour", Temps [0])
    AffichePluriels(("Heure"), Temps[1])
    AffichePluriels("Minute", Temps[2])
    AffichePluriels("Seconde", Temps[3]) 
AfficheTemps((1,0,14,23))  
print()

def demandeTemps():
    j = -1
    h = -1
    m = -1
    s = -1 
    while j < 0 : 
        j = int(input("donner un autre jour"))
    while h < 0 or h >= 24 : 
        h = int(input("donner une autre heure"))
    while m < 0 or m >= 60 : 
        m = int(input("donner d'autres minutes"))
    while s < 0 or s >= 60 :
        s = int(input("donner d'autres secondes"))
    return ( j, h, m, s)
AfficheTemps(demandeTemps())

def sommeTemps(temps1,temps2): 
    return secondeEnTemps(tempsEnSeconde(temps1)+ tempsEnSeconde(temps2))

def proportionTemps(temps,proportion):
    return secondeEnTemps(tempsEnSeconde(temps)* (proportion))
AfficheTemps(proportionTemps((2,0,36,0),0.2))
print()

import time 
def tempsEnDate(temps):
    a = 1970 + (temps[0] // 365)
    nb = 1 + temps[0] % 365
    return (a, nb, temps[1], temps[2], temps[3])
def afficheDate(date : tuple = ()):
    if len(date) == 0 : 
        date = tempsEnDate(secondeEnTemps(time.time()))
    print("jours numéro", date[1], "de l'année", date[0], "à", str(date[2]) + ":" + str(date[3]) + str(date[4]))
temps = secondeEnTemps(1000000000)
AfficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()


