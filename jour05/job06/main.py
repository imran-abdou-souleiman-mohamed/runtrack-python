def distance_toilettes_par_semaine(nombre_marches, hauteur_marche):
    nombre_jours_semaine = 7
    nombre_allers_retours_par_jour = 2  

    distance_totale_cm = nombre_marches * hauteur_marche * nombre_allers_retours_par_jour * nombre_jours_semaine
    distance_totale_m = distance_totale_cm / 100  

    return distance_totale_m


nombre_marches = 10
hauteur_marche = 20  

distance_totale = distance_toilettes_par_semaine(nombre_marches, hauteur_marche)
print(f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_totale:.2f} m par semaine.")