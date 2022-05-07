# Fonction

""" def est_majeur(age):
    if age >= 18:
        return True
    return False


def afficher_infos_personne(nom="", age=0):
    if nom == "":
        print("Vous n'avez pas donné de nom, l'age vaut", age)
        return

    if age == 0:
        print("La personne est", nom)
    else:
        print("La personne est", nom + ", son age est", age, "ans")
    print("Le nom comporte", len(nom), "caractères")
    if est_majeur(int(age)):
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")
    print()

# ----------------------------------------------------------------------

print("Début du programme")
print()

nom  = input("Quel est votre nom ? ")
age = input("Quel est votre age ? ")
print()

afficher_infos_personne(nom, age)
print()

print("Fin du programme")"""

# Hierarchie
'''
recuper_et_afficher_info_personne
    -> recuper_info_personne()
    -> afficher_info_personne(nom, age)
        -> est_majeur()
'''


def est_majeur(age: int):
    if age >= 18:
        return True
    return False


def recuper_info_personne(nombre):
    nom = input(f"Nom de la personne {nombre} : ")
    age = input(f"Age de la personne {nombre} : ")
    return nom, age


def afficher_info_personne(nombre, nom, age: int):
    print(f"Le nom de la personne {nombre} est : ", nom, ", son age est", age, "ans")
    print("Le nom comporte", len(nom), "caractères")
    if est_majeur(int(age)):
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")
    print()


def recuper_et_afficher_info_personne(nombre):
    a, b = recuper_info_personne(nombre)
    afficher_info_personne(nombre, a, b)


nb_personne = input("Combien etes vous ? ")
nb_personne_int = int(nb_personne)

for i in range(nb_personne_int):
    recuper_et_afficher_info_personne(i + 1)
    print()
afficher_info_personne("007", "James", "40")


# -----------------------------------------------------------


# FONCTION RECURSIVE
def demander_choix_utilisateur(min, max):
    reponse_str = input("Quel est votre choix entre " + str(min) + " et " + str(max) + ": ")
    try:
        reponse_int = int(reponse_str)
        if not min <= reponse_int <= max:
            print("ERREUR: Vous devez rentrer un nombre entre", min, "et", max)
            print()
            return demander_choix_utilisateur(min, max)
        return reponse_int
    except:
        print("ERREUR: Vou devez rentrez un nombre")
        print()
        return demander_choix_utilisateur(min, max)


choix = demander_choix_utilisateur(1, 4)
print("Choix de l'utilisateur:", choix)
print()


# -----------------------------------------------------------

# CALLBACK
def afficher_table(n, operateur_str, operation_cbk):
    for i in range(1, 10):
        print(i, operateur_str, n, "=", operation_cbk(i, n))


"""def mult_callback(w, x):
    return w * x


def add_callback(w, x):
    return w + x


def power_callback(w, x):
    return pow(w, x)"""

# FONCTION LAMBDA
n = input("Quelle table souhaitez vous executer: ")
afficher_table(int(n), "x", lambda w, x: w * x)
print()
afficher_table(int(n), "+", lambda w, x: w + x)
print()
afficher_table(int(n), "^", lambda w, x: pow(w, x))

# -----------------------------------------------------------
