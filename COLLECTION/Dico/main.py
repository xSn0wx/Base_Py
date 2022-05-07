# ----------------PARTIE 1------------------
personne = {"nom": "Melanie", "age": 25, "taille": 1.60}
print(personne["nom"])
personne["age"] = 15
personne["poste"] = "Developpeur"
print(personne)

for i in personne:
    print((f"Clef: {i} - Valeur: {personne[i]}"))
print()
print()

# ----------------PARTIE 2------------------

personnes = [
    ("Lucie", 25, 1.6),
    ("George", 28, 1.9),
    ("Paul", 18, 1.7),
    ("Martin", 15, 1.5)
]

def obtenir_information(nom, liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None

infos = obtenir_information("Martin", personnes)

# VS 

personne_dict = {    
    "Mélanie": (25, 1.6),
    "George": (28, 1.9),
    "Paul": (18, 1.7),
    "Martin": (15, 1.5)
}

infos = personne_dict["Paul"]
infos = personne_dict.get("Claire")
if not infos:                            # if infos == None:
    print("La clef n'existe pas")
else:
    print(infos)

# La méthode 2 est beaucoup plus rapide car elle ne boucle pas