
#Fonction qui calcul le produit et la somme de deux entiers et les retourne
def SommeProduit(entier1,entier2):
    somme = entier1 + entier2
    produit = entier1 * entier2
    return somme,produit


#Prise des valeurs que l'on converti en entier
reponse = input("Entrez un nombre : ")
entier1 = int(reponse)
reponse = input("Entrez un deuxième nombre: ")
entier2 = int(reponse)


#Appel de la fonction
resultat = SommeProduit(entier1, entier2)

#Affichage
print("Somme:",resultat[0],"| Produit:",resultat[1])

