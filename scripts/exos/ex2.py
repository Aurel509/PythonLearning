#On récupère la valeur donnée par l'utilisateur
reponse = input('Donnez votre âge : ')

#On transforme la valeur récupérée en nombre
age = int(reponse)

#On vérifie si l'âge donné est valide.
if(age > 0 and age < 120):


#Vérification de l'âge
    if(age < 18):
        print("Vous êtes mineur")
    else:
        print("Vous êtes majeur")

#Dans le cas où l'age n'est pas valide, on renvoi un message d'erreur
else:
    print("L'âge donné n'est pas valide.")
