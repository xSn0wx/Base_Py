def tri_personnalise(e):
    return len(e)


def afficher_pizza(collection, n_premier_element=-1):
    c = collection
    if not n_premier_element == -1:
        c = collection[:n_premier_element]

    nb_pizza = len(c)
    if nb_pizza == 0:
        print("AUCUNE PIZZA")
        return

    c.sort(key=tri_personnalise, reverse=True)

    print(f"-------LISTE DES PIZZAS ({nb_pizza})-------")
    for i in c:
        print(i)
    print()
    print(f"Premiere Pizza: {c[0]}")
    print(f"Dernière Pizza: {c[-1]}")



def ajouter_pizza_user(collection):
    a = input("Pizza à ajouter: ")
    if a.lower in collection:
        print("ERREUR: le pizza existe déjà")
    else:
        collection.append(a)



# ------------------------------------------------------
pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]
ajouter_pizza_user(pizzas)
afficher_pizza(pizzas)

# lower() -> minuscule
# upper() -> majuscule