class Question:
    def __init__(self, titre_question, choix, choix_bonne_reponse):
        self.titre_question = titre_question
        self.choix = choix
        self.choix_bonne_reponse = choix_bonne_reponse

    """
    def FromData(data):
        q = Question(data[2], data[0], data[1])
        return q
    """

    def poser(self):
        print("QUESTION : ", self.titre_question)
        nb_choix = 0
        for i in range(len(self.choix)):
            print(f"  {i + 1}-", self.choix[i])
            nb_choix += 1
        print()
        reponse_int = Question.demander_reponse_user(1, nb_choix)
        print()
        reponse_correcte = False
        if self.choix[reponse_int-1].lower() == self.choix_bonne_reponse.lower():
            print("Bonne réponse")
            print()
            reponse_correcte = True
        else:
            print("Mauvaise réponse")
            print()
        return reponse_correcte

    def demander_reponse_user(min, max):
        reponse_str = input(f"Votre réponse (entre {min} et {max}) : ")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int
            else:
                print(f"ERREUR: Vous devez rentrer un nombre entre {min} et {max}")
        except:
            print(f"ERREUR: Veuillez rentrer uniquement des chiffres")
        print()


class Questionnaire:
    def __init__(self, questions):
        self.questions = questions

    def lancer(self):
        score = 0
        for question in self.questions:
            if question.poser():
                score += 1
        print(f"Score final : {score}/{len(self.questions)}")
        return score


questionnaire = Questionnaire((
        Question("Quel est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris"),
        Question("Quel est le plus petit pays du monde ?", ("Monaco", "Le Vatican", "Malte", "Sealand"), "Sealand"),
        Question("Quel est le 3eme pays le plus riche du monde ?", ("Japon", "France", "Chine", "Allemagne"), "Japon"),
        Question("Quel est le second pays le plus puissant du monde millitairement ?",("USA", "Russie", "Chine", "R-U"), "Russie")
                )).lancer()

"""
data = (("Marseille", "Nice", "Paris", "Nantes"), "Quel est la capitale de la France ?", "Paris")
q = Question.FromData(data)
q.poser()
"""
# FromData est un patern factory