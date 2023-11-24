def arrondi(liste):
    
    def manuel(lst):
        n = len(lst)
        for i in range(n):
            for j in range(0, n - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]

   
    for i in range(len(liste)):
        liste[i] = int(liste[i] + 0.5)  

  
    manuel(liste)

    return liste


ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

print("Liste d'origine :", ma_liste)


ma_liste_arrondie_triee = arrondi(ma_liste)

print("Liste arrondie et triée :", ma_liste_arrondie_triee)