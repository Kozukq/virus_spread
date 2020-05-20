from random import randrange
from random import choice


def fun1():
    x = 5
    x = int(x)
    return x

def fun2():
    x = fun1()
    z = 5
    res = x + z
    return res

liste = [65,998,3,2,54]

def choi():
    val = choice(liste)
    return val


"""
Couleur en fonction de l'état de la personne
"""
COLOR = {
    "COLOR_GOOD": "BIEN",
    "COLOR_BAD": "MAUVAIS",
    "COLOR_DEAD": "MORT",
}

def choice(couleur):
    couleur = str(couleur)
    print(COLOR[couleur])

col = "COLOR_GOOD"
choice(col)




