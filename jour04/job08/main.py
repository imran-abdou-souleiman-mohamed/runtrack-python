L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]


valeurs_paires = sum(nombre for nombre in L if nombre % 2 == 0)


print("La somme des valeurs paires dans la liste est :", valeurs_paires)