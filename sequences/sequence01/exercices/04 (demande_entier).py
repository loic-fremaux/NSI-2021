def demande_entier():
    """
    ask for an integer while the given number isn't one
    :return: the integer
    """
    while True:
        number = float(input("Entrez un nombre entier: "))
        if number == int(number):
            print("Bravo ! C'est un nombre entier !")
            break
        else:
            print("Essayez à nouveau :(")
    return number


demande_entier()
