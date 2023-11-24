L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]


valeurs_intervalle = [valeur for valeur in L if 25 <= valeur <= 90]


Pvaleurs_intervalle = 1
for valeur in valeurs_intervalle:
    Pvaleurs_intervalle *= valeur


print("Produit valeurs dans l'intervalle [25, 90] est :", Pvaleurs_intervalle)