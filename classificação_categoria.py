#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
#mostre sua categoria, de acordo com a idade:
# ate 9 anos: mirim
# ate 14 anos: infantil
# ate 19 anos: junior
# ate 20 anos: senior
# Acima: master

from datetime import date
valid_nasc = False
while valid_nasc == False:
    ano_nascimento= input("Digite seu ano de nascimento: ")
    try:
        ano_nascimento = int(ano_nascimento)
        if ano_nascimento <= 0:
            print('O ano de nascimento deve ser maior que zero')
        else:
            valid_nasc = True
    except:
        print('Insira apenas números inteiros')
valid_nasc = False

idade= date.today().year - ano_nascimento
if idade<=9:
    print("Categoria mirim")
elif idade>9 and idade<=14:
    print("Categoria infantil")
elif idade>14 and idade<=19:
    print("Categoria junior")
elif idade>19 and idade<=20:
    print("Categoria senior")
else:
    print("Categoria master")