# https://www.beecrowd.com.br/judge/pt/problems/view/1065

pares = 0
for c in range(5):
    n = int(input())
    if n % 2 == 0:
        pares += 1
print(f"{pares} valores pares")

