import turtle


def tortue(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
        taille -= 10
    t.forward(taille)


def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


def carres(taille_depart, nb):
    for i in range(0, nb):
        taille = (i+1)*taille_depart
        carre(taille)


# -------------------------------
t = turtle.Turtle()
nb_marche = 5

tortue(60, nb_marche)
carres(10, 10)

turtle.done()
