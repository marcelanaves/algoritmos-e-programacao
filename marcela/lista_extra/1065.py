# https://www.beecrowd.com.br/judge/pt/problems/view/1065

quantidadePar = 0
for indice in range(5):
    valorDigitado = int(input())
    if valorDigitado % 2 == 0:
        quantidadePar += 1
print(str(quantidadePar) + " valores pares")