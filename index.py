import random

body = 0
body = int(body)

def nasobeni(x, y):
    vysledek = x * y
    return vysledek

def kontrola(vysledek, z):
    if vysledek == z:
        print("Správně !!")
        g = body + 1
        body = g 
    else:
        print("Špatně !")



for a in range(9):
    x = random.randint(1,10)
    y = random.randint(1,10)
    vysledek = nasobeni(x ,y)

    z = input(f"{x} * {y} = ")
    z = int(z)

    kontrola(vysledek, z)