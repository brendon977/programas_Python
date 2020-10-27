#Crie um programa que faça o computador
#jogar jokenpo com voce.


from random import randint
from time import sleep # para colocar timer no programa
valid_jogador = False
itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
while valid_jogador == False:
    jogador= input('Qual sua jogada? ')
    try:
        jogador = int(jogador)
        if jogador <0 or jogador >2:
            print("Escolha entre as opções de 0 a 2")
        else:
            valid_jogador = True
    except:
        print('Insira apenas números')

valid_jogador = False

print('JO')
sleep(1) # sleep de 1 segundo
print('KEN')
sleep(1)
print('PO')
sleep(1)
print("-="*11)
print('O computador escolheu{}'.format(itens[computador])) #com itens[computador] ele passa a escrever o nome dos itens que cair em vez dos numeros.
print('O jogador jogou{}'.format(itens[jogador]))
print("-="*11)

if computador == 0:
    if jogador ==0:
        print("Empate")
    elif jogador ==1:
        print("Jogador venceu")
    elif jogador ==2:
        print("Computador venceu")
    else:
        print("Jogada inválida")

elif computador ==1:
    if jogador ==0:
        print("Computador venceu")
    elif jogador ==1:
        print("Empate")
    elif jogador ==2:
        print("Jogador venceu")
    else:
        print("Jogada inválida")


elif computador ==2:
    if jogador ==0:
        print("Jogador venceu")
    elif jogador ==1:
        print("Computador venceu")
    elif jogador ==2:
        print("Empate")
    else:
        print("Jogada inválida")
