# PROGRAMMATION ORIENTEE OBJET

# Personne  (entité -> class)
#   Donnée : nom, age   ()
#   Actions : (Méthodes)
#       - Se présenter()
#       - demande Nom()  / input


'''def afficher_info_personne(nom, age):
    print(f"La perosonne s'appelle {nom}, son age est {age} ans.")

def demande_info_personne():
    nom = input("Quel est votre nom ? ")
    return nom

nom1 = "Jean"
age1 = 30

nom2 = "Paul"
age2 = 25

afficher_info_personne(nom1, age1)

nom3 = demande_info_personne()
age3 = 18
afficher_info_personne(nom3, age3)'''


# --- DEFINITION ---
class EtreVivant:
    ESPECE = "inconnu"

    def AfficherEspece(self):
        print("Info être espece : ", self.ESPECE)


class Chat(EtreVivant):
    ESPECE = "Chat"
# Le chat sera tjr capable de se presenter car il herite de EtreVivant
# EtreVivant est la class parent de la class Chat
# Chat ou Personne sont des class enfant (dérivées)


class Personne(EtreVivant):
    ESPECE = "Humain"   # Variable class
    def __init__(self, nom: str = "", age: int = 0):  # Le self c'est l'objet
        self.nom = nom  # créer variable instance : nom
        if self.nom == "":
            Personne.DemanderNom(self)
        self.age = age
        # Les variables d'instance doivent etre dans le constructeur
        print("Constucteur personne", self.nom)

    
    def SePresenter(self):
        info_personne = "Bonjour je m'appelle " + self.nom
        if self.age != 0:
            info_personne += ", j'ai " + str(self.age) + " ans"
        print(info_personne)

        if self.age != 0:
            if self.Estmajeur():
                print("Je suis majeur")
            else:
                print("Je suis mineur")
    
    def Estmajeur(self):
        return self.age >= 18   # Sa return un boolen

    def DemanderNom(self):
        self.nom = input("Quel est ton nom ? ")
        

class Etudiant(Personne):
    def __init__(self, nom, age, etude):  # Le self c'est l'objet
        super().__init__(nom, age)
        self.etude = etude

    def SePresenter(self):  # Surchargé SePresenter
        super().SePresenter # super()  ->  Self du parent
        print("Je suis étudiant en", self.etude)


# --- UTILISATION ---

liste_personne = [Personne("Jean", 30), Personne("Paul", 15), Personne(), Personne(age = 20)]
print()
Personne.ESPECE = "Alien"
for i in liste_personne:
    i.SePresenter()
    i.AfficherEspece()
    print()

chat = Chat()
chat.AfficherEspece()

etudiant = Etudiant("Mark", 22, "Developper")
etudiant.SePresenter()
etudiant.AfficherEspece()
