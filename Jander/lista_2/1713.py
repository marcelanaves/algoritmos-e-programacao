# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valor = float(input())
horas = float(input())
salario = valor * horas
irrf = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
liquido = salario - irrf - inss - sindicato
print(f"Salário bruto: R${salario:.2f}\nImposto: R${irrf:.2f}\nINSS: R${inss:.2f}\nSindicato: R${sindicato:.2f}\nLíquido: R${liquido:.2f}")

