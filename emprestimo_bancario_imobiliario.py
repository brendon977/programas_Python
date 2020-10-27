#Escreva um programa para aprovar o emprestimo bancario
#para a compra de uma casa.O programa vai perguntar
#o valor da casa, o salario do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não
#pode exceder 30% do salário ou então o empréstimo será negado.
valid_casa= False
valid_salario= False
valid_pgto = False

while valid_casa == False:
    valor_casa= input("Digite o valor da casa: ")
    try:
        valor_casa = float(valor_casa)
        if valor_casa <= 0:
            print('O valor da casa tem que ser maior que 0. ')
        else:
            valid_casa = True
    except:
        print('Digite apenas números !')
valid_casa = False
while valid_salario == False:
    salario= input("Digite o valor do seu salário: ")
    try:
        salario = float(salario)
        if salario <= 0:
            print('O salário deve ser maior que 0.')
        else:
            valid_salario = True
    except:
        print('Digite apenas números')
valid_salario = False

while valid_pgto == False:
    anos_pgto= input("Em quantos anos pretende pagar a casa? ")
    try:
        anos_pgto = float(anos_pgto)
        if anos_pgto <= 0 :
            print('A quantidade de anos precisa ser maior que 0.')
        else:
            valid_pgto = True
    except:
        print('Digite apenas números')
valid_pgto = False



prestacao_mensal= (valor_casa/anos_pgto)/12
porcentagem= salario - (salario * 0.3)

if prestacao_mensal > porcentagem:
    print("Infelizmente seu empréstimo foi negado.Suas prestações mensais seriam R$ \033[1;30m{:.2f}\033[m".format(prestacao_mensal))
elif prestacao_mensal <= porcentagem:
    print("Parabéns seu empréstimo foi aprovado.Suas parcelas mensais serão R$ \033[1;30m{:.2f}\033[m".format(prestacao_mensal))