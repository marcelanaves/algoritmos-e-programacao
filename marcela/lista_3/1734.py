# https://www.beecrowd.com.br/judge/pt/problems/view/1734

n = int(input())
c = n
x = 1
while c > 0:
    x = x * c
    c = c - 1
    
print("%i! = %i" %(n, x))