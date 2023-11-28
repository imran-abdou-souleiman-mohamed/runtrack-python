def chiffrement_cesar(message, decalage):
    message_chiffre = ""

    for lettre in message:

        if lettre.isalpha():

            est_majuscule = lettre.isupper()


            lettre = lettre.lower()


            lettre_chiffree = chr((ord(lettre) - ord('a') + decalage) % 26 + ord('a'))


            if est_majuscule:
                lettre_chiffree = lettre_chiffree.upper()


            message_chiffre += lettre_chiffree
        else:

            message_chiffre += lettre

    return message_chiffre


message_original = "Hello, World!"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)
print("Message original:", message_original)
print("Message chiffré:", message_chiffre)