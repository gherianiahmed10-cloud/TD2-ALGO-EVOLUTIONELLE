"""
gheriani trabelsi ahmed - LSI3 3.1
TD2 - Exercice 3 : Voyageur de commerce par recuit simulé
"""
from random import *
from math import exp


def f(s, villes):
    somme = 0
    for i in range(len(villes)):
        a = s[i] - 1
        b = s[(i + 1) % len(villes)] - 1
        curr = villes[a][b]
        somme += curr
    return somme


def estValide(s, villes):
    for i in range(len(villes)):
        a = s[i] - 1
        b = s[(i + 1) % len(villes)] - 1
        if villes[a][b] == -1:
            return False
    return True


def calcul_voisins(s, villes):
    v = []
    for i in range(len(villes) - 1):
        for j in range(len(villes)):
            voisin = s[:]
            voisin[i], voisin[j] = voisin[j], voisin[i]
            if estValide(voisin, villes):
                v.append(voisin)
    return v


def recuit_simule(initial, villes, iters):
    s = initial
    T = 100
    for i in range(iters):
        voisins = calcul_voisins(s, villes)
        if len(voisins) == 0:
            T = T // 2
            continue
        choix = randint(0, len(voisins) - 1)
        s_prime = voisins[choix]
        delta = f(s_prime, villes) - f(s, villes)
        if delta < 0:
            s = s_prime
        else:
            u = random()
            if u < exp(-delta / T):
                s = s_prime
        T = T // 2
    return s


def main():
    initial = [1, 2, 3, 4, 5, 6, 7, 8]
    villes = [
        [-1, 14, 15, -1, -1, -1, -1, 17],
        [14, -1, 13, 14, 20, -1, -1, 21],
        [15, 13, -1, 11, 21, 17, 9, 9],
        [-1, 14, 11, -1, 11, 10, 8, 20],
        [-1, 20, 21, 11, -1, 15, 18, -1],
        [-1, -1, 17, 10, 15, -1, 9, -1],
        [-1, -1, 9, 8, 18, 9, -1, 13],
        [17, 21, 9, 20, -1, -1, 13, -1]
    ]
    s = recuit_simule(initial, villes, 5)
    print(f"le chemin est {s}")
    print(f"le cout est {f(s, villes)}")


if __name__ == "__main__":
    main()
