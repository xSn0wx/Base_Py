nom_chauffeur = ["Patrick", "Paul", "Mark", "Jean", "Pierre", "Marie", "Maxime"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]
distance_min = distance_chauffeur_km[0]

for distance in distance_chauffeur_km:
    if distance < distance_min:
        distance_min = distance

index_min = distance_chauffeur_km.index(distance_min)


print("Distance minimale:", distance_min, "km")
print("Index de la distance minimale:", index_min)
print("Nom du chauffeur :", nom_chauffeur[index_min])

# V2
noms_et_distances = [("Patrick", 1.5), ("Paul", 2.2), ("Marc", 0.4)]

nom_et_distance_min = noms_et_distances[0]
for nom_et_distance in noms_et_distances:
    if nom_et_distance[1] < nom_et_distance_min[1]:
        nom_et_distance_min = nom_et_distance

print("Distance minimale:", nom_et_distance_min[1], "nom du chauffeur:", nom_et_distance_min[0])