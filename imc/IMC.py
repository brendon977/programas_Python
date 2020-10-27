## user.title() faz a primeira letra ser sempre maiuscula.


##user = input('Seu nome:')
##idade = int(input('Digite sua idade: '))
##
##def mensagem(user,idade):
##    print('Seja bem vindo {}, voce tem {} anos!'.format(user.title(),idade))
##
##mensagem(user,idade)
##peso = float(input('Insira seu peso: '))
##altura = float(input('Insira sua altura: '))
##
##def imc(peso,altura): 
##    valor_imc = peso /(altura*altura)
##    return(valor_imc) ## vai retornar o resultado
##
##if imc(peso,altura) > 32:    ## consigo usar a função imc como uma variavel 
##    print('Voce está obeso!')
##else:
##    print('Voce não está obeso')
##
##
##
##def exemplo(): ## as variaves de uma função são variaveis locais, não podem ser acessadas e apenas utilizadas dentro da função
##    y= 10
##    print(y)
##
##exemplo()


##Exercicio Funções
##faça um programa que receba o sexo, peso e altura do usuário e em seguida apresente:
##    -IMC
##    -Classificação do IMC baseado na seguinte tabela:
       


import func  ## utilizando o modulo func de funções que foi criado e separado e está sendo importado nesse programa.

       
print('Vamos calcular seu imc')            

valid_peso = False
while valid_peso == False:
    peso = input('Digite seu peso: ')
    try:
        peso = float(peso)
        if peso <0:
            print('Peso inválido.Digite apenas numeros acima de zero')
        else:
            valid_peso = True
            print('\n')
    except:
        print('Peso inválido.Digite apenas números separando os decimais com ponto.')
        print('\n')
        
   
valid_peso = False        
        


valid_altura= False
while valid_altura == False:
    altura = input('Digite sua altura em metros (ex: 1.70): ')
    try:    ## try tenta fazer a conversão de uma variável
        altura= float(altura)
        if altura <0:
            print('Altura inválida.Digite apenas numeros acima de zero')
        else:
            valid_altura= True
            print('\n')
    except:
        print('Altura inválida.Digite apenas números separando os decimais com ponto.')
valid_altura= False




valid_sexo= False
while valid_sexo == False:
    sexo = input('Sexo (M ou F): ').lower()
    if sexo != 'm' and sexo != 'f':
        print("insira M para masculino ou F para feminino")
    else:
        valid_sexo = True

valid_sexo= False





v_imc = str(func.imc(peso,altura))
c_imc = func.class_imc(sexo,peso,altura)

print('O seu imc é:', v_imc[0:5]) ## transformando o imc em string para pegar apenas os 4 primeiros digitos do resultado.
print('A sua classificação é:',c_imc)



         

   



