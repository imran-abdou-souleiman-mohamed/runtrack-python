montant_initial = 11000
taux_rendement_annuel = 0.02
gain_annuel = taux_rendement_annuel*montant_initial
# mise en place variable
montant_total = montant_initial+gain_annuel
print(montant_total)
# valeur initial 
montant_initial += 5000
taux_rendement_annuel += 0.02
nouveau_gain_annuel = taux_rendement_annuel*montant_initial
# mise a jour du taux
print(nouveau_gain_annuel)
# calcule valeur tout les compte
montant_total = montant_initial+nouveau_gain_annuel
# montant total 
retrait = 0.10 * montant_total
# on stock la valeur des 10%
montant_initial -= retrait
print(montant_initial)
# mise a jour du compte apres le retrait des 10%
taux_rendement_annuel -= 0.01
# on diminue rendement 1%
montant_final = montant_initial + nouveau_gain_annuel
nouveau_gain = taux_rendement_annuel*montant_final
print(nouveau_gain)