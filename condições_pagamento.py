#Elabore um programa que calcule o valor para ser
# pago por um produto,
#considerando o seu preço normal e
#condição de pagamento:

#-à vista dinheiro/cheque:10% de desconto
#à vista no cartão:5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
valid_preco = False
valid_opcao = False


while valid_preco == False:
    preco=input("Valor do produto: R$ ")
    try:
        preco = float(preco)
        if preco < 0 :
            print('Insira valores acima de 0')
        else:
            valid_preco = True
    except:
        print('Insira apenas números')
valid_preco = False

print('''Forma de pagamento: 
[1] a vista dinheiro/cheque
[2] a vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
while valid_opcao == False:
    opcao= input('Escolha a opção: ')
    try:
        opcao = int(opcao)
        if opcao < 0 or opcao > 4:
            print("Escolha uma opção entre 1 e 4")
        else:
            valid_opcao = True
    except:
        print('Insira apenas números')

valid_opcao = False

if opcao==1:
    total= preco -(preco*0.1)
    print("Desconto de 10%, valor R$ \033[1;31m{}\033[m".format(total))
elif opcao==2:
    total= preco - (preco*0.05)
    print("Desconto de 5%, valor R$ \033[1;33m{}\033[m".format(total))
elif opcao==3:
    total= preco
    print("Preço normal R$ \033[4;30m{}\033[m".format(total))
elif opcao==4:
    total= preco +(preco*0.2)
    print(" valor parcelado em 3X ou mais. O preço do seu produto sairá R$ \033[1;30m{}\033[m".format(total))
