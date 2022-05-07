noms = ("Jean", "Emilie", "Paul")
ages = (20, 30, 25, 40)

try:
    z = zip(noms, ages, strict=True)
    print(list(z))
except ValueError:
    print("ERREUR: nombre différents dans le zip")