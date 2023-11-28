def afficher_tapis_diagonale(n):
    for i in range(n+1):
        for u in range(n+1):
            if i == u:
                print(" ", end=" ")
            else:
                print("#", end=" ")
        print()

afficher_tapis_diagonale(11)