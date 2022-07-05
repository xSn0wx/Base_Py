# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je m'appelle " + self.nom)

# ---
nb_personne = input("Vous etes combien ? ")
noms = []

for i in range(0, int(nb_personne)):
    nom = input(f"Nom de la personne {i + 1}: ")
    noms.append(Personne(nom))

for i in noms:
    i.SePresenter()
    