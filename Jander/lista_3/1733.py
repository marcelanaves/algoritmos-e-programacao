# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = input()
qtdHoras = float(input())
horasExtras = qtdHoras * 10
salarioBruto = 3 * 1192.40 + horasExtras
if salarioBruto > 2000:
    inss = 0.12 * salarioBruto
else:
    inss = 0.05 * salarioBruto
if salarioBruto > 2500:
    irrf = 0.20 * salarioBruto
else:
    irrf = 0
salarioLiquido = salarioBruto - inss - irrf
print(f"Nome: {nome}")
print(f"Salário bruto: R${salarioBruto:.2f}")
print(f"Salário líquido: R${salarioLiquido:.2f}")

