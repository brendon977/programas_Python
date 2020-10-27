#Desenvolva uma lógica que leia o peso e altura
# de uma pessoa, calcule seu IMC e mostre seu status
#de acordo com a tabela abaixo:

#-Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
#25 ate 30: Sobrepeso
#30 ate 40: Obesidade mórbida

#Validação de dados inclusa




valid_peso= False
while valid_peso == False:
    peso= input("Digite seu peso: ")
    try:
        peso = float(peso)
        if peso <0:
            print('Insira apenas numeros maiores que 0')
        else:
            valid_peso = True
    except:
        print('Insira apenas números!')
valid_peso = False



valid_altura = False
while valid_altura == False:
    altura = input("Digite sua altura: ")
    try:
        altura = float(altura)
        if altura == str:
            print("Insira apenas números e separando apenas usando ponto(.)")
        else:
            valid_altura= True
    except:
        print("Insira apenas números e separando apenas usando ponto'(.)'")

valid_altura= False


iMC= peso/(altura*altura)

if iMC<18.5:
    print("Seu imc {:.2f}. Abaixo do peso!".format(iMC))
elif iMC>=18.5 and iMC<=25:
    print("Seu imc {:.2f}. Peso ideal!".format(iMC))
elif iMC>25 and iMC<=30:
    print("Seu imc {:.2f}. Sobrepeso!".format(iMC))
elif iMC>30 and iMC<=40:
    print("Seu imc {:.2f}. Obesidade mórbida!".format(iMC))
