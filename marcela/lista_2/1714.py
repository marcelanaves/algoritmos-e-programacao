# https://www.beecrowd.com.br/judge/pt/problems/view/1714

valorP = float(input())

if valorP < 20:
    valorV = (valorP * 0.45) + valorP
    print("Valor de venda: R$%.2f" %(valorV))
    
else:
    valorV = (valorP * 0.3) + valorP
    print("Valor de venda: R$%.2f" %(valorV))