def valeur(liste, index):
    if index >= 1 and index < len(liste) - 1:
        liste[index] = liste[index - 1] + liste[index + 1]


L = [1, 2, 3, 4, 5]


print("Liste initiale :", L)
deuxieme_valeur = L[1]
print("Deuxième valeur de la liste :", deuxieme_valeur)
valeur(L, 3)
print("Liste après la modification :", L)
derniere_valeur = L[-1]
print("Dernière valeur de la liste :", derniere_valeur)