def demander_note(nb):
    total = [""]
    for i in range(nb):
        moyenne = input(f"Quelle est votre moyenne de la matière {i + 1} ? ")
        print()
        try:
            moyenne_int = float(moyenne)
            print(moyenne_int)
            total.append(moyenne_int)
        except ValueError:
            print("ERREUR: Les notes doivent être des NOMBRES!")
            print()
            print("RECOMMENCONS")
            demander_note(nb)
    del total[0]
    return total


def demander_note_coef(nb):
    total = [""]
    coefi = [""]
    coe = [""]
    tot = [""]
    for i in range(nb):
        moyenne = input(f"Quelle est votre moyenne de la matière {i + 1} ? ")
        coef = input(f"Quelle est le coeficient de la matière {i + 1} ? ")
        print()
        try:
            moyenne_int = float(moyenne)
            total.append(moyenne_int)
            coef_int = float(coef)
            coefi.append(coef_int)
            coe.append(coef_int)
        except ValueError:
            print("ERREUR: Les notes et les coefficients doivent être des NOMBRES!")
            print()
            print("RECOMMENCONS")
            demander_note(nb)
    del total[0]
    del coefi[0]
    del coe[0]
    for i in range(nb):
        a = total[0]*coefi[0]
        tot.append(a)
        del total[0]
        del coefi[0]
    del tot[0]
    somme_total = sum(tot)
    somme_coef = sum(coe)  # POur pour / le somme par le coef il fuatr transferer la somme des 2 listes dans 2 var
    somme_finale = somme_total/somme_coef
    return somme_finale


def demander_nb_matiere(nb_int=0):
    nb_matiere = input("Combien avez vous de matières ? ")
    print()
    try:
        nb_int = int(nb_matiere)
    except ValueError:
        print("ERREUR: Vous devez entrez un NOMBRE!")
        demander_nb_matiere()
    return nb_int


# -------------------------------------------------------------------------
question = input("Es ce un moyenne avec coefficient yes/no ? ")
if question == "no":
    print()
    nb_matiere_int = demander_nb_matiere()
    liste = demander_note(nb_matiere_int)
    print(liste)
    print("Votre moyenne est: ", sum(liste) / nb_matiere_int)
elif question == "yes":
    nb_matiere_int = demander_nb_matiere()
    somme_final = demander_note_coef(nb_matiere_int)
    print("Votre moyenne est: ", somme_final)
else:
    print()
    print("Veuillez utilisez yes ou no !!")
    exit()
print()
print("FIN DU PROGRAMME")
