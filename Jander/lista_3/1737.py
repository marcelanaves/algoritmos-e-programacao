# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

quantidade = int(input())
soma = 0
cont = 0
if quantidade <= 0:
    print(f'Informe uma quantidade > 0!')
else:
    while quantidade > cont:
        num = int(input())
        soma += num
        quantidade -= 1
    print(f'Soma dos números informados: {soma:.2f}')

