#Déclaration des variables pour la population et l'année
pop = 87646
annee = 2021

#Tant que la population n'a pas atteint 100 000 habitants...
while(pop < 100000):
    
    #Calcul du nombre d'habitants arrondi
    resultat = round(pop + (pop * 0.89/100))

    #Incrémentation de l'année
    annee += 1
    
    #Affichage de l'année en cours et du nombre d'habitants
    print("Année",annee,
          "| Population prévue :",pop,
          " + (",pop,"* 0.89/100) =", resultat)

    #Mise à jour de la population pour l'année suivante
    pop = resultat

    
