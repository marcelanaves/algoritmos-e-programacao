# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

valor = float(input())
if valor < 20:
  venda = (valor*1.45)
else:
  venda = (valor*1.30)
print(f"Valor de venda: R${venda:.2f}")

