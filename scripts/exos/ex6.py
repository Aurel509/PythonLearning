#Fonction pour calculer le prix total des baguettes
def prixBaguette(prix,nombre):

    #Calcul du prix total
    total = prix * nombre

    #On renvoi le résultat
    return total


reponse = input("Nombre de baguettes :")
nombre = int(reponse)

#Execution de la fonction avec le nombre de baguettes donné
prixTotal = prixBaguette(0.90, nombre)

print("Prix total :",prixTotal,"€")
