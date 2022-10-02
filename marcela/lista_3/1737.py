# https://www.beecrowd.com.br/judge/pt/problems/view/1737

quantidadesN = int(input())
cont = 1
soma = 0

while cont <= quantidadesN:
    num = int(input())
    cont = cont + 1
    soma = soma + num
if quantidadesN > 0:
    print("Soma dos números informados: %.2f" %(soma))
else:
    print("Informe uma quantidade > 0!")