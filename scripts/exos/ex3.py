#On récupère la valeur donnée par l'utilisateur
reponse = input('Donnez un nombre : ')

#On transforme la valeur récupérée en nombre
valeur = int(reponse)


print("Table des ",valeur)
#On effectue boucle for qui sera répété 10 fois (de 1 à 10.)
for facteur in range(1,11):

#On calcul la multiplication, et on affiche le résultat à chaque intération
    resultat = valeur * facteur
    print(valeur," * ",facteur," = ",resultat)
