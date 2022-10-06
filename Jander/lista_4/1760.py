# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

mais90 = 0
idades = 0
for c in range(4):
    idade = int(input())
    idades += idade
    peso = float(input())
    if peso > 90:
        mais90 += 1
print(f"Qtd pessoas > 90Kg: {mais90}" )
print(f"Idade média: {idades/4:.2f}")
