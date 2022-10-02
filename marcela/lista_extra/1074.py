# https://www.beecrowd.com.br/judge/pt/problems/view/1074

quantidadeDigitada = int(input())
respostas = []
for x in range(quantidadeDigitada):
    valorDigitado = int(input())
    positivoOuNegativo = ""
    parOuImpar = ""
    if valorDigitado == 0:
        respostas.append("NULL");
    else:
        if valorDigitado % 2 == 0:
            parOuImpar = "EVEN"
        else:
            parOuImpar = "ODD"
        
        if valorDigitado > 0:
            positivoOuNegativo = "POSITIVE"
        else:
            positivoOuNegativo = "NEGATIVE"
        
        respostas.append(parOuImpar + " " + positivoOuNegativo)

for x in range(quantidadeDigitada):
    print(respostas[x])