def pair_or_not(nombre):
    if type(nombre) == int and nombre > 0:
        if nombre % 2 == 0:
            print("Chiffre pair")
        else:
            print("Chiffre impair")
    else:
        print("Chiffre doit être un entier positif")

pair_or_not(4)
pair_or_not(1)
pair_or_not(-52)