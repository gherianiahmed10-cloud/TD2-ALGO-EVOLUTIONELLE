"""
gehriani trabelsi ahmed - LSI3 3.1
TD2 - Exercice 2 : Problème de transport par recherche taboue
"""
from collections import deque


def estValide(demandes, s, nb_containers):
    demandes_per_depot = [0 for _ in range(len(nb_containers))]
    for i in range(len(demandes)):
        depot_nb = s[i] - 1
        demandes_per_depot[depot_nb] += demandes[i]
    for i in range(len(demandes_per_depot)):
        if demandes_per_depot[i] > nb_containers[i]:
            return False
    return True


def calcul_voisins(demandes, s, nb_containers):
    voisins = []
    nb_depots = len(nb_containers)
    for i in range(len(demandes)):
        v = s[:]
        for x in range(1, nb_depots + 1):
            if x != s[i]:
                v[i] = x
                if estValide(demandes, v, nb_containers):
                    voisins.append(v[:])
    return voisins


def f(s, couts):
    somme = 0
    for i in range(len(s)):
        somme += couts[s[i] - 1][i]
    return somme


def tabou(demandes, couts, initial, nb_containers, taille_tabou, iters):
    s = initial
    cout_s = f(s, couts)
    tab = deque(maxlen=taille_tabou)
    for i in range(iters):
        voisins = calcul_voisins(demandes, s, nb_containers)
        voisins = [voisin for voisin in voisins if voisin not in tab]
        if not voisins:
            break
        s_prime = min(voisins, key=lambda x: f(x, couts))
        cout_s_prime = f(s_prime, couts)
        tab.append(s_prime)
        if cout_s_prime < cout_s:
            cout_s = cout_s_prime
            s = s_prime
    return s


def main():
    nb_containers = [8, 9]
    couts = [[5, 3, 4], [6, 7, 2]]
    demandes = [4, 5, 8]
    initial = [2, 2, 1]
    taille_tabou = 5
    iters = 5
    s = tabou(demandes, couts, initial, nb_containers, taille_tabou, iters)
    print(f"la solution est {s}")
    print(f"le cout est {f(s, couts)}")


if __name__ == "__main__":
    main()
