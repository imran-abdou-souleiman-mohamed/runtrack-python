produit = "croissant"
prix = 1
stock = 10
print("produit", produit)
print("prix", prix)
print("stock", stock)
quantite_achat = int(input("Merci de mettre votre quantité :"))
stock -= quantite_achat
prix *= 1.1
print("\nAprès l'achat et l'ajustement :")
print("produit:", produit)
print("prix (après inflation):", prix)
print("stock:", stock)