def demander_des_noms():
    nom = []
    age = []
    a = 0
    while True:
        nom_personne = input("Quel est ton nom ? ")
        if nom_personne == "":
            break
        age_personne = input("Quel est ton age ? ")
        print()
        nom.append(nom_personne)
        age.append(age_personne)
        a += 1
    for i in range(a):
        print(f"Le nom de la personne {i + 1} est", nom[0], "son age est", age[0], "ans.")
        print()
        del age[0]
        del nom[0]




demander_des_noms()