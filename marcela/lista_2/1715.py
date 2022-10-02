# https://www.beecrowd.com.br/judge/pt/problems/view/1715

tipo = int(input())
valorCompra = float(input())

if tipo == 1:
    valorT = valorCompra
    print("Valor total a ser pago: R$%.2f" %(valorT))
    
elif tipo == 2:
    valorT = valorCompra - (valorCompra *0.13)
    print("Valor total a ser pago: R$%.2f" %(valorT))

elif tipo == 3:
    valorT = valorCompra - (valorCompra *0.07)
    print("Valor total a ser pago: R$%.2f" %(valorT))

else:
    print("OPÇÃO INVÁLIDA!")