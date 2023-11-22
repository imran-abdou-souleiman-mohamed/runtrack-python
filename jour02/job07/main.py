chaine = "abcdefghijklmnopqrstuvwxyz"
rows = len(chaine)

for i in range(rows):
    for j in range(i + 1):
        print(chaine[j], end=" ")

    print("\n")