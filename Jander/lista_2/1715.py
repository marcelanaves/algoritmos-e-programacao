# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

codigo = float(input())
valor = float(input())
if codigo == 1:
    total = valor
    print(f"Valor total a ser pago: R${total:.2f}")
elif codigo == 2:
    total = valor - (valor * 0.13)
    print(f"Valor total a ser pago: R${total:.2f}")
elif codigo == 3:
    total = valor - (valor * 0.07)
    print(f"Valor total a ser pago: R${total:.2f}")
else:
    print(f"OPÇÃO INVÁLIDA!")

