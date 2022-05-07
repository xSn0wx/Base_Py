def demander_choix_utilisatuer(min, max):
    reponse_str = input("Quel est votre choix entre " + str(min) + " et " + str(max) + ": ")
    try:
        reponse_int = int(reponse_str)
        if not min <= reponse_int <= max:
            print("ERREUR: Vous devez rentrer un nombre entre", min, "et", max)
        return reponse_int
    except:
        print("ERREUR: Vou devez rentrez un nombre")

choix = demander_choix_utilisatuer(1, 4)
print("Choix de l'utilisateur:", choix)