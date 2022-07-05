#IsInstance

class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
        if not isinstance(age, int):
            print("L'age doit etre de type INT")
            self.age = 0

    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}")
        if self.age > 0:
            print(f"L'an prochain j'aurais {self.age + 1} ans")

personne = Personne("Jean", 20)
personne.AfficherInfos()
print("--------------------------------")
print()


#Polymorphisme
class EtreVivant:
    def afficher_infos(self):
        print("Je suis un etre vivant")

class Chat(EtreVivant):
    def afficher_infos(self):
        print("Je suis un chat")

class Personne2(EtreVivant):
    def afficher_infos(self):
        print("Je suis une personne")

l = [EtreVivant(), Chat(), Personne2()]
for e in l:
    e.afficher_infos()

def additionner(a, b):
    somme = 0
    if isinstance(a, int):
        somme += a
    if isinstance(a, str):
        somme += len(a)
    if isinstance(b, int):
        somme += b
    if isinstance(b, str):
        somme += len(b)
    return somme

print(additionner(5, "aaaa"))
print("--------------------------------")
print()


#Heritage multiple 
class EtreVivant2:
    def afficher_infos(self):
        print("Je suis un etre vivant")

class Predateur:
    def chasser_proie(self):
        print("miam miam")

class Lion(EtreVivant, Predateur):
    def afficher_infos(self):
        print("Je suis un lion")

lion = Lion()
lion.afficher_infos()
lion.chasser_proie()
print("--------------------------------")
print()


#Comparer objet
#Copy objet -> shallow copy / deep copy
import copy

class Personne3:
    def __init__(self, nom: str, age: int, amis):
        self.nom = nom
        self.age = age
        self.amis = amis
    
    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")
        print("Amis :", self.amis)

    def __eq__(self, other):
        return self.nom == other.nom and self.age == other.age


personne1 = Personne3("Jean", 20, ["Claire", "Marc", "Emilie"])
personne1.AfficherInfos()

# personne2 = copy.copy(personne1)
# shallow copy
# personne1.amis[0] = "Chantale" sa change aussi personne2
personne2 = copy.deepcopy(personne1)
personne1.amis[0] = "Chantale"
personne2.AfficherInfos()
# personne 2 n'a pas Chantale

print(personne1 == personne2) # Compare donné -> True
print(personne1 is personne2) # Compare l'objet -> False
print(personne1.__dict__ == personne2.__dict__) # Compare les dicos
print("--------------------------------")
print()


# __str__ & __repr__

class Personne4:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age
    
    def AfficherInfos(self):
        print(f"Je m'appelle {self.nom}, j'ai {self.age} ans")

    # def __str__(self):
    #    return "STR"

    # dev
    def __repr__(self):
        return __class__.__name__ + str(self.__dict__)
        # -> Personne4{'nom': 'Jean', 'age': 20}
    # Change meme dans le debug

prsn1 = Personne4("Jean", 20)
prsn1.AfficherInfos()

print(prsn1)
# <__main__.Personne4 object at 0x7ff8af931580> 
# grace a __str__ -> STR (representation str)
print("--------------------------------")
print()


# Methode d'instance, de classe et statiques

class Stormtrooper :
    TYPE = "Stormtrooper"
    def __init__(self, nom):
        self.nom = nom
    
    # methode d'instance
    def se_presenter(self):
        print(f"Je m'appelle {self.formater_chaine(self.nom)} - " + self.TYPE)

    # Premier caractere en majuscule
    # méthode statique -> depend pas du self
    @staticmethod   # Un écorateur
    def formater_chaine(a):
        return a[0].upper() + a[1:].lower()

    @classmethod
    def methode_de_classe(cls):
        print("Type de classe : " + cls.TYPE)


clone1 = Stormtrooper("death trooper")
clone1.se_presenter()
print(Stormtrooper.formater_chaine("toTO")) # -> Toto
Stormtrooper.methode_de_classe()
print("--------------------------------")
print()


# Modificateur d'acès : public / private / protected
# public = accès interieur et extérieur
# private = accès intérieur (__x)
# protected = accès intérieur et class dérivées  (_x)
class Ia :
    def __init__(self, nom):
        self._nom = nom

    def se_presenter(self):
        print(f"Je m'appelle {self.formater_chaine(self._nom)}")

class Etudiant(Ia):
    def se_presenter(self):
        print(f"Je suis étudiant, je m'appelle {self.formater_chaine(self._nom)}")

ia1 = Ia("Alexa")
etudiant = Etudiant
ia1.se_presenter()