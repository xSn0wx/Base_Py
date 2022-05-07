def poser_question(question):
    titre_question = question[0]
    choix = question[1]
    choix_bonne_reponse = question[2]
    print("QUESTION : ", titre_question)
    nb_choix = 0
    for i in range(len(choix)):
        print(f"  {i + 1}-", choix[i])
        nb_choix += 1
    print()
    reponse_int = demander_reponse_user(1, nb_choix)
    print()
    reponse_correcte = False
    if choix[reponse_int-1].lower() == choix_bonne_reponse.lower():
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
    return demander_reponse_user(min, max)

    
def lancer_questionnaire(questionnaire):
    score = 0
    for question in questionnaire:
        if poser_question(question):
            score += 1
    print(f"Score final : {score}/{len(questionnaire)}")


questionnaire = (
        ("Quel est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris"),
        ("Quel est le plus petit pays du monde ?", ("Monaco", "Le Vatican", "Malte", "Sealand"), "Sealand"),
        ("Quel est le 3eme pays le plus riche du monde ?", ("Japon", "France", "Chine", "Allemagne"), "Japon"),
        ("Quel est le second pays le plus puissant du monde millitairement ?",("USA", "Russie", "Chine", "R-U"), "Russie")
                )

lancer_questionnaire(questionnaire)
