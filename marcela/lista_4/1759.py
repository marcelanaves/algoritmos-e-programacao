# https://www.beecrowd.com.br/judge/pt/problems/view/1759

anoAtual = int(input())
salario = 1000
percentual = 1.5

if anoAtual < 2006:
    print("O ano informado deverá ser > 2005!")
else:
    while anoAtual >= 2006:
        salario = salario + (salario/100 * percentual)
        percentual = percentual + 1
        anoAtual = anoAtual - 1
    print("Salário atual: R$%.2f" %(salario))