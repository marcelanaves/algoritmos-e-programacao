# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

precos = 1
soma = 0
while precos != 0:
    precos = float(input())
    soma += precos
dinheiro = float(input())
troco = dinheiro - soma
print(f'Total da compra: R${soma:.2f}')
print(f'Valor pago: R${dinheiro:.2f}')
print(f'Troco: R${troco:.2f}')

