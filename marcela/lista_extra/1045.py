# https://www.beecrowd.com.br/judge/pt/problems/view/1045

valorString = str(input())
valoresFloat = []

valores = valorString.split()
for valor in valores:
    valoresFloat.append(float(valor))

valoresOrdenados = sorted(valoresFloat, reverse=True)

a = valoresOrdenados[0]
b = valoresOrdenados[1]
c = valoresOrdenados[2]

#se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    #se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    if a**2 == (b**2 + c**2):
        print("TRIANGULO RETANGULO")
    #se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    #se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO  
    elif a**2 < (b**2) + (c**2):
        print("TRIANGULO ACUTANGULO")
        
    #se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    if a == b and b == c:
        print("TRIANGULO EQUILATERO")
    
    #se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
    elif (a == b and b != c) or (b == c and c != a) or (c == a and b != a):
        print("TRIANGULO ISOSCELES")