# https://www.beecrowd.com.br/judge/pt/problems/view/1760

qtde = 0
media = 0

for x in range(4):
    idade = int(input())
    peso = float(input())
    if peso > 90:
        qtde = qtde + 1 
    media = media + idade
    mediaIdade = media / 4

print("Qtd pessoas > 90Kg: %i" %(qtde))
print("Idade média: %.2f" %(mediaIdade))