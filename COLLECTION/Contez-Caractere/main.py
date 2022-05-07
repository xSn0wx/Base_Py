# Methode 1
noms = ["Jean", "Sophie", "Martin", "Cristophe", "Zoe"]
s = 0
for i in noms:
    s += len(i)
print("Nombre total de caractères :", s)

# Methode 2
car_nom = []
# car_nom[len(nom) for nom in noms]
for i in noms:
    car_nom.append(len(i))
print("Nombre total de caractères :", sum(car_nom))

# Methode 3

print("Nombre total de caractères :", len("".join(noms)))
