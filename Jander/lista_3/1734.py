# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

n = int(input())
cont = n
fatorial = 1
while cont >= 1:
    fatorial *= cont
    cont -= 1
print(f'{n}! = {fatorial}')

