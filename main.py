#### Imports et définition des variables globales
"""on importe sys pour augmenter le nb de récursion"""
import sys
#### Fonctions secondaires
sys.setrecursionlimit(2000)

def artcode_i(s:str)->list:
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    selon un algorithme itératif
    """
    if s == "":  # cas où s est vide
        return []

#initialisation
    c=[s[0]]
    r=[1] #liste des caractères qui se repetent
    for k in range (1,len(s)):
        if s[k] == s[k - 1]:
            r[-1] = r[-1]+1  # Augmenter le dernier compte
        else:
            c.append(s[k])  # Ajouter un nouveau caractère
            r.append(1)

    #Créer une liste de tuples à partir des listes de c et O
    result=[(c[i],r[i])for i in range (len(c))]
    return result

def artcode_r(s:str)->list:
    """retourne la liste de tuples encodant une chaîne de caractères passée
    en argument selon un algorithme récursif
    """
    # cas de base
    if not s:
        return []
    #initialisation
    k=1

    #recherche de caractère identique au premier
    while k < len(s) and s[k]==s[0]:
        k=k+1

    # Appel récursif
    return [(s[0], k)] + artcode_r(s[k:])


#### Fonction principale


def main():
    """on test la fonction principale
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
