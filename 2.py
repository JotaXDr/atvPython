def calcArea(base, altura):
    area = base * altura
    return area

base = int(input("insira o valor da base: "))
altura = int(input("insira o valor da altura: "))

resultado = calcArea(base, altura)

print("A área é:", resultado)
