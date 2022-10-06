# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

salario = 1015
anoInicial = 2006
aumento = 0.025
ano = int(input())
if ano < 2006:
    print('O ano informado deverá ser > 2005!')
else:
    while anoInicial < ano:
        salario = salario + salario * aumento
        aumento += 0.01
        anoInicial += 1
    print(f"Salário atual: R${salario:.2f}")

