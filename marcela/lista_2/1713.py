# https://www.beecrowd.com.br/judge/pt/problems/view/1713

valorHora = float(input())
numHoras = float(input())

salBruto = valorHora * numHoras
imposto = salBruto * 0.11
inss = salBruto * 0.08
sindicato = salBruto * 0.05
salLiquido = salBruto - imposto - inss - sindicato