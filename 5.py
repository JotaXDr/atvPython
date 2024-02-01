import random

numAleatorio = random.randint(0, 10)
while True:
    tentativa = int(input("Adivinhe o número de 0 a 10: "))
    if tentativa == numAleatorio:
        print("Acertou")
        break
    else:
        print("Errado, tente novamente")
