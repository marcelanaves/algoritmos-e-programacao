# https://www.beecrowd.com.br/judge/pt/problems/view/1716

plano = (input())
salario = float(input())

if plano == "A":
    novosalario = salario + (salario * 0.10)
    print("Novo salário: R$%.2f" %(novosalario))
    
elif plano == "B":
    novosalario = salario + (salario * 0.15)
    print("Novo salário: R$%.2f" %(novosalario))

elif plano == "C":
    novosalario = salario + (salario * 0.20)
    print("Novo salário: R$%.2f" %(novosalario))