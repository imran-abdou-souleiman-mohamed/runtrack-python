def my_long_word(longueur, chaine):
    mots = []  
    mot_actuel = ""  

    for caractere in chaine:
        
        if caractere != ' ':
            mot_actuel += caractere
        else:
            
            if len(mot_actuel) > longueur:
                mots.append(mot_actuel)
            mot_actuel = ""  

   
    if len(mot_actuel) > longueur:
        mots.append(mot_actuel)

    
    resultat = ' '.join(mots)

    return resultat

longueur_minimale = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

resultat = my_long_word(longueur_minimale, phrase)

print("Output :", resultat)