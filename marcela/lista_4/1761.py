# https://www.beecrowd.com.br/judge/pt/problems/view/1761

soma = 0
valor = 1

while valor != 0:
    valor = float(input())
    soma = soma + valor
if valor == 0:
    valorPago = float(input())
troco = valorPago - soma

print ("Total da compra: R$%.2f" %(soma))
print ("Valor pago: R$%.2f" %(valorPago))
print ("Troco: R$%.2f" %(troco))