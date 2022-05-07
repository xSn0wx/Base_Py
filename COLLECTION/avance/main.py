# Append / Extend / += / Insert
noms = ["Jean", "Sophie", "Martin"]
noms_supplémentaires = ["Cristophe", "Zoé"]
# for e in noms_supplémentaires:
   #  noms.append(e)
noms.extend(noms_supplémentaires) # ou noms += noms_supplémentaires ou noms = noms + noms_supplémentaires
noms.insert(0, "Toto")  # (index, "")


# Slices  (dernier élément exclu)
print(noms[0:-2]) # 0:2 = :2


# Tris : Sort / Sorted
noms.sort(reverse=True) # Par ordre désalphabétique (inplace)
noms_tries = sorted(noms, key=lambda nom:len(nom)) 
# lambda permet de rentrer une foncion et en resortir une autre
print(noms_tries)


# Operation : min, max, in, sum
ages = [21, 20, 30, 25, 22, 18]
print(max(ages)) # 30
print(min(noms_tries)) # Christophe car c'est en fonction de l'odre alphabétique
if "Jean" in noms:
    print("Présent")
else:
    print("Absent")
print(sum(ages)) # somme INT


# Swapper (échanger) 2 élément
noms[0], noms[4] = noms[4], noms[0]


# Join et Split
# Join = Rejoindre -> coller
noms_join = ", ".join(noms_tries)
print(noms_join)
# Split : Séparer
noms_re = noms_join.split(", ")
print(noms_re)


# Index, Find, Count
# ['Zoé', 'Toto', 'Jean', 'Sophie', 'Martin', 'Cristophe']
element_cherche = "Martin"
nb_occurence = noms.count(element_cherche)
if element_cherche in noms:
    print(noms.index(element_cherche))
    print("Dans la liste l'élément apparait:", nb_occurence, "fois.")
else:
    print("L'élément n'est pas dans la collection")
a = "Jean-Martin-Toto"
i = a.find("Martin")  
# Que pour les STR, quand c'est pas trouvé -1 sinon 5 car M est à l'index 5


# Les Completions de listes
mha = ["Ochako", "Shoto", "Izuku", "All Might", "Katsuki"]
longeur_noms = [] 
# for nom in mha:
   # longeur_noms.append(len(nom))
longeur_noms = [len(nom) for nom in mha if len(nom) < 10]
nom_avec_o = [nom for nom in mha if "h" in nom]
print(longeur_noms)
print(nom_avec_o)
longeur_noms = [len(nom) if len(nom) < 10 else 0 for nom in mha]
a = [i for i in range(11) if (i//2)*2 == i] 
print(a)  # Print que les nombres pairs
b = [(i, True if (i//2)*2 == i else False) for i in range(11)] 
print(b)


# Any et All
# Any -> Quelconque  !=  All = Tous 
a = [False, False, True, False]
print(any(a))  # -> True car il y au moins un élément Vrai
print(all(a))  # -> False car tous les éléments ne sont pas vrai
nom_avec_z = any([True if "z" in nom.lower() else False for nom in mha])
if nom_avec_z:
    print("Trouvé")
else:
    print("Non trouvé")


# any / isdigit
def chaine_contient_chiffre(chaine):
    return any([c.isdigit for c in chaine])

nom = input("Quel est votre nom ? ")
if nom == "":
    print("Votre nom est vide")
elif chaine_contient_chiffre(nom):
    print("Le nom ne doit pas contenir de chiffre")  
else:
    print("Bonjour", nom)

nom = "toto"

# Zip
pizza_nom = ("4 fromages", "Calzone", "Hawai")
pizza_prix = (10.5, 11, 8)

np = list(zip(pizza_nom, pizza_prix))

for (nom, prix) in np:
    print(f"{nom} - {prix}$")

unzipped = list(zip(*np)) # Inverse de zip()
