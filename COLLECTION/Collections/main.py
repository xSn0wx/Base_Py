# Collections : (Tableau: Array), Listes, Tuples...
# Tuples (): immutable = Non modifiable != Liste []: mutable = Modifiable
# Plusieurs éléments

# --------------------TUPLES-----------------------
note = ("Math: 16", "Français: 13", "PC: 19", "SVT: 16")
for i in note:
    print(i)
    # print(i[-1]) --> Afficher les dernieres lettres
print()
# range est un tuples

# --------------------LISTES-----------------------
personnes = ["Melanie", "Jean", "Martin", "Alice"]
nouvelle_personne = "David"
personnes.append(nouvelle_personne)  # Ajouter David dans la Liste
del personnes[1]  # Supprimer le 2ème personne


def afficher_personne(c):
    for j in c:
        print(j)


afficher_personne(personnes)
print()


# --------------------FONCTION & TUPLES-----------------------

def obtenir_information():
    return "Melanie", 37, 1.60


nom, age, taille = obtenir_information()
print(f"Information:\nNOM: {nom}\nAGE: {age}\nTAILLE: {taille}")
infos = obtenir_information()
print(*infos)  # unpack tuples

# --------------------SLICES-----------------------

# [start:stop:step]
snk = ("Livai", "Eren", "Mikasa", "Armin", "Erwin", "Jean")
for i in snk[0:2]:
    print(i)

mot_long = "anticonstitutionnellement"
print("Anticonstitutionnellement à l'envers donne:", mot_long[::-1])
