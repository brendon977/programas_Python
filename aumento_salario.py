#Escreva um programa que pergunta o salario de um funcionario e calcule o valor do seu aumento.

#Para salarios superiores a 1250,00 calcule um aumento de 10%

#Para os inferiores ou iguais, o aumento é de 15%


salario= float(input("Digite o valor do seu salário: "))
if salario>1250.00:
    print("O valor do seu aumento será de R$ \033[1;31m{}\033[m seu novo salario será R$ {}".format(salario*0.10,salario+salario*0.10))
else:
    print("O valor do seu aumento será de  R$ \033[1;35m{}\033[m seu novo salario será R$ {}".format(salario*0.15,salario+salario*0.15))