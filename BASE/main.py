# Premier Programme

def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " quel est votre age ? ")
        try:
            age_int = int(age_str)
        except ValueError:
            print("ERREUR : vous devez entrez un nombre pour l'age")
        return age_int


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def afficher_informations_personne(nom, age, taille=0):
    print()
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
    print("L'an prochain vous aurez " + str(age + 1) + " ans")
    if age == 17:
        print("Vous êtes presque majeur")
    elif 12 <= age < 18:
        print("Vous êtes Adolescent")
    elif age == 1 or age == 2:
        print("Vous êtes un bébé")
    elif age < 10:
        print("Vous êtes enfant")
    elif age > 60:
        print("Vous êtes sénior")
    elif age == 18:
        print("Tout juste majeur : Félicitation")
    elif age > 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

    if not taille == 0:
        print("Votre taille : " + str(taille) + " m")


# ------------------------------------------------------------------------

for i in range(0, int(input("Combien êtes vous ? "))):
    print()
    nom = "personne" + str(i + 1) + " : " + input("Quel est votre nom ? ")
    age = demander_age(nom)
    afficher_informations_personne(nom, age)

print()
print("Merci passez une bonne  journée !")
