import random

body = 0

def scitani(x, y):
    scitani = x + y
    return vysledek

def odecitani(x, y):
    vysledek = x - y
    return vysledek

def nasobeni(x, y):
    vysledek = x * y
    return vysledek

def deleni(x, y):
    vysledek = x / y
    return vysledek

def kontrola(vysledek, z):
    global body
    if vysledek == z:
        print("Správně !!")
        body += 1
    else:
        print("Špatně !")

operace = [scitani, odecitani, nasobeni, deleni]
operace_nazvy = ['+', '-', '*', '/']

for a in range(10):
    x = random.randint(1,10)
    y = random.randint(1,10)

    index = random.randint(0, len(operace) - 1)
    vysledek = operaceindex

    z = input(f"{x} {operace_nazvy[index]} {y} = ")
    z = float(z)

    kontrola(vysledek, z)

print(f"Máte {body} bodů.")
