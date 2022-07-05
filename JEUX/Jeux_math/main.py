import random

# gérer les erreurs

print("""
     ____.                          .___                        __  .__     
    |    | ____  __ _____  ___    __| _/____      _____ _____ _/  |_|  |__  
    |    |/ __ \|  |  \  \/  /   / __ |/ __ \    /     \\__  \\   __\  |  \  
/\__|    \  ___/|  |  />    <   / /_/ \  ___/   |  Y Y  \/ __ \|  | |   Y  \ 
\________|\___  >____//__/\_ \  \____ |\___  >  |__|_|  (____  /__| |___|  / 
              \/            \/       \/    \/         \/     \/          \/   """)

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTION = input("Combien de question voulez vous faire ? ")
int_nb_question = int(NB_QUESTION)


def difficultes():
    global NOMBRE_MAX
    print("""Choisissez un niveau de difficulte:
                                1 - Facile (Nombre de 1 a 10)
                                2 - Moyen (Nombre de 1 a 50,)
                                3 - Difficile (Nombre de 1 a 100)""")
    diff = input("Votre choix: ")
    if diff == "1":
        print("Vous êtes en mode débutant")
        NOMBRE_MAX = 10
        print()
    elif diff == "2":
        print("Vous êtes en mode intermédiaire")
        NOMBRE_MAX = 50
        print()
    else:
        print("Vous êtes en mode expers")
        NOMBRE_MAX = 100
        print()


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 3)
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
    elif o == 2:
        operateur_str = "-"
    elif o == 3:
        operateur_str = "/"
    reponse_str = input(f"Calculez: {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a + b
    if o == 1:
        calcul = a * b
    elif o == 2:
        calcul = a - b
    elif o == 3:
        calcul = a / b
    if reponse_int == calcul:
        return True
    return False


difficultes()

nb_points = 0
for i in range(0, int_nb_question):
    print(f"Question n°{i + 1} sur {NB_QUESTION}: ")
    if poser_question():
        print("Réponse correcte")
        nb_points += 1
    else:
        print("Réponse incorrecte")
    print()

print(f"Votre note est: {nb_points} / {NB_QUESTION}")

moyenne = int(NB_QUESTION) / 2

if nb_points == int_nb_question:
    print("Exellent !")
elif nb_points == moyenne:
    print("Vous avez la moyenne")
elif nb_points == 0:
    print("Révisez vos maths ! ")
elif nb_points > moyenne:
    print("Pas mal")
else:
    print("Peut mieux faire")
