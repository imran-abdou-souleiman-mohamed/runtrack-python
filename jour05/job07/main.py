def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            # L'étudiant a échoué, pas d'arrondi nécessaire
            notes_arrondies.append(note)
        else:
            # Calculer le prochain multiple de 5
            prochain_multiple_de_5 = (note // 5 + 1) * 5

            # Vérifier si l'arrondi est nécessaire
            if prochain_multiple_de_5 - note < 3:
                notes_arrondies.append(prochain_multiple_de_5)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

# Exemple d'utilisation
notes_eleves = [83, 75, 42, 36, 91]
notes_arrondies = arrondir_notes(notes_eleves)
print("Notes originales:", notes_eleves)
print("Notes arrondies:", notes_arrondies)