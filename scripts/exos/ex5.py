#Initialisation du tableau et de la somme
tableau = []

print("Donnez 10 nombres")

#Boucle for, on répète 10 fois 
for i in range(10):

    #Stockage de la réponse donnée
    reponse = input()

    #On change la réponse en nombre décimal
    valeur = float(reponse)

    #Ajout de la valeur donnée dans le tableau à l'indice i
    tableau.append(valeur)

#Calcul et affichage de la somme du tableau
print("Somme du tableau donné :", sum(tableau))
