L = [8, 24, 48, 2, 16]


multiples_de_3 = sum(1 for nombre in L if nombre % 3 == 0)


print("Le nombre de multiples de 3 dans la liste est :", multiples_de_3)