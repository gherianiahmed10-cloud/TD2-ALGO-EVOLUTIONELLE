"""
gheriani trabelsi ahmed - LSI3 3.1
TD2 - Exercice 3 : Voyageur de commerce par recherche taboue
"""
from collections import deque


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


def tabou(initial, villes, iters, taille_tabou):
    s = initial
    d = f(initial, villes)
    tab = deque(maxlen=taille_tabou)
    for i in range(iters):
        voisins = calcul_voisins(s, villes)
        voisins = [voisin for voisin in voisins if voisin not in tab]
        if len(voisins) == 0:
            break
        s_prime = min(voisins, key=lambda x: f(x, villes))
        d_prime = f(s_prime, villes)
        tab.append(s_prime)
        if d_prime < d:
            s = s_prime
            d = d_prime
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
    s = tabou(initial, villes, 5, 5)
    print(f"le chemin est {s}")
    print(f"le cout est {f(s, villes)}")


if __name__ == "__main__":
    main()
