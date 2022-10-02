# https://www.beecrowd.com.br/judge/pt/problems/view/1019

valor = int(input())
minutos = valor % 3600 / 60
horas = valor / 3600
segundos = valor % 3600 % 60
print("%i:%i:%i" %(horas, minutos, segundos))