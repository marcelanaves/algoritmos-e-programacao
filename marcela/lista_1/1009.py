# https://www.beecrowd.com.br/judge/pt/problems/view/1009

nome = str(input())
salfixo = float(input())
vendas = float(input())

bonus = float(vendas * (15/100))

total = salfixo + bonus

print("TOTAL = R$ %0.2f" %(total))