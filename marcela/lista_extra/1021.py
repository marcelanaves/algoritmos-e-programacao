# https://www.beecrowd.com.br/judge/pt/problems/view/1021

valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.10, 0.05, 0.01]
notasGastas = [0, 0, 0, 0, 0, 0]
moedasGastas = [0, 0, 0, 0, 0, 0]
contador = 0

for nota in notas:
    while valor >= nota:
        valor = round(valor - nota, 2)
        notasGastas[contador] = notasGastas[contador] + 1
    contador = contador + 1

contador = 0

for moeda in moedas:
    while valor >= moeda:
        valor = round(valor - moeda, 2)
        moedasGastas[contador] = moedasGastas[contador] + 1
    contador = contador + 1

print("NOTAS:")
for x in range(6):
    print("%i nota(s) de R$ %.2f"%(notasGastas[x], notas[x]))

print("MOEDAS:")
for x in range(6):
    print("%i moeda(s) de R$ %.2f"%(moedasGastas[x], moedas[x]))