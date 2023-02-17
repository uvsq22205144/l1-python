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

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range (1, n_max +1) :
        syracuse(i)
    return True
print(testeConjecture(10000))