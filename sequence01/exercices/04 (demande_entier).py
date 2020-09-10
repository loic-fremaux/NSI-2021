def demande_entier():
    while True:
        number = float(input("Entrez un nombre entier: "))
        if number == int(number):
            print("Bravo ! C'est un nombre entier !")
            break
        else:
            print("Essayez à nouveau :(")


demande_entier()
