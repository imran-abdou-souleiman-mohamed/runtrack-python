def premier(liste):
    liste[0], liste[-1] = liste[-1], liste[0]
    return liste

L = [1,2,3,4,5]
print(L)
L = premier(L)
print(L)