#Escreva um programa que leia dois numeros inteiros e compare-os
#mostrando na tela uma mensagem:

#- O primeiro valor é maior
#- O segundo valor é maior
#- Não existe valor maior, os dois são iguais

valid_num1=False
valid_num2= False
while valid_num1 == False:
    n1= input("Digite o primeiro valor: ")
    try:
        n1= int(n1)
        valid_num1 = True

    except:
        print('Insira apenas números inteiros')
valid_num1 = False

while valid_num2 == False:
    n2= input("Digite o segundo valor: ")
    try:
        n2 = int(n2)
        valid_num2 = True
    except:
        print('Insira apenas números inteiros')
valid_num2 = False


if n1>n2:
    print("valor1 \033[1;30m{}\033[m, valor2 \033[1;33m{}\033[m. O Primeiro valor é maior".format(n1,n2))
elif n2>n1:
    print("valor1 \033[1;30m{}\033[m, valor2 \033[1;33m{}\033[m. O segundo valor é maior".format(n1,n2))
elif n1==n2:
    print("valor1 \033[1;30m{}\033[m, valor2 \033[1;33m{}\033[m. Não existe valor maior, os dois são iguais".format(n1,n2))