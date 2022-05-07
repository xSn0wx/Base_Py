def element_dans_liste(e, l):
    for i in l:
        if e.lower() == i.lower():
            return True
    return False
    # l-lower = [el.lower() for el in l]    return e.lower() in l_lower
    

nom = ["Jean", "Sophie", "Marin", "Cristhophe", "Zoe", "Martin"]

if element_dans_liste("jean", nom):
    print("Est la")
else:
    print("Pas la")

# ------------------------------------------------------------------------------
