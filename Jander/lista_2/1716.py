# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

plano = input()
atual = float(input())
if plano == 'A':
  salario = atual * 1.10
  print(f"Novo salário: R${salario:.2f}")
elif plano == 'B':
  salario = atual * 1.15
  print(f"Novo salário: R${salario:.2f}")
elif plano == 'C':
  salario = atual * 1.20
  print(f"Novo salário: R${salario:.2f}")

