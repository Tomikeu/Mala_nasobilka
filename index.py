import random

body = 0

def nasobeni(x, y):
    vysledek = x * y
    return vysledek

def kontrola(vysledek, z):
    global body
    if vysledek == z:
        print("Správně !!")
        body += 1
    else:
        print("Špatně !")



for a in range(10):
    x = random.randint(1,10)
    y = random.randint(1,10)
    vysledek = nasobeni(x ,y)

    z = input(f"{x} * {y} = ")
    z = int(z)

    kontrola(vysledek, z)

print(f"Máte {body} bodů.")