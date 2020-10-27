#Faça um programa que leia o ano de nascimento de um
#jovem e informe, de acordo com sua idade:

#- Se ele ainda vai se alistar ao serviço militar
#- Se é a hora de se alistar
#- Se já passou do tempo do alistamento

#Seu programa também deverá mostrar o tempo
#que falta ou que passou do prazo.

from datetime import date
valid_nasc = False
while valid_nasc == False:
    ano_nascimento= input("Digite seu ano de nascimento: ")
    try:
        ano_nascimento = int(ano_nascimento)
        if ano_nascimento <= 0:
            print('Insira números maiores que zero!')
        else:
            valid_nasc = True
    except:
        print('Insira apenas números inteiros')
valid_nasc = False


idade= date.today().year - ano_nascimento
old= idade - 18

if idade<18:
    print("Sua idade é \033[1;34m{}\033[m anos voce ainda não precisa se alistar ao serviço militar.".format(idade))
elif idade ==18:
    print("Sua idade é \033[1;31m{}\033[m anos voce precisa se alistar ao serviço militar.".format(idade))
else:
    print("Sua idade é \033[1;36m{}\033[m anos, seu tempo de alistamento ja passou {} anos.".format(idade,old))