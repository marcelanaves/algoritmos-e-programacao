# https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = input('')
fixo = float(input())
vendas = float(input())
comissao = 0.15
salario = fixo + (vendas*comissao)
print(f"TOTAL = R$ {salario:.2f}")

