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

resultat = fun2()
print(resultat)

liste = [1,2,3,4]

def choi():
    val = choice(liste)
    return val

valeur = choi()
print(valeur)