# https://www.beecrowd.com.br/judge/pt/problems/view/1733

nome = input()
horasExtras = float(input())
salMinimo = 1192.40
valorhorasExtras = 10.00

salhorasEx = horasExtras * valorhorasExtras
salBruto = (3 * salMinimo) + salhorasEx

if salBruto > 2000.00:
    descontoInss = salBruto * (12 / 100)
else:
    descontoInss = salBruto * (5 / 100)
    
if salBruto > 2500.00:
    descontoIr = salBruto * (20 / 100)
else:
    descontoIr = 0
    
descontos = descontoInss + descontoIr
salLiquido = salBruto - descontos

print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %(salBruto))
print("Salário líquido: R$%.2f" %(salLiquido))