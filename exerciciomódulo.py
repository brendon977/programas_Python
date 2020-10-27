##Exercício Modulos
##Usando o módulo Time(Built-in) e o Matplotlib(Externo), faça um programa que pede
##que o usuário digite uma palavra 5 vezes seguidas.Conte o tempo que ele leva para
##digitar a palavra a cada repetição e ao final gere um gráfico com os tempos.

import time
import matplotlib.pyplot as plt
tempos = []
vezes = []
legenda = []
vez = 1
repet = 3
validacao = False
print('Este programa marcará o tempo gasto para digitar a palavra PROGRAMAÇÃO.Você terá que digitá-la '  +  str(repet) + ' vezes')
input('Aperte enter para começar.')      

while vez <= repet:
    while validacao == False:
         palavra= input('Digite a palavra: ')
         try:
            palavra = str(palavra)
            if palavra != 'programação':
                print('Digite a palavra programação.')
            else:
                validacao = True    
         except:
             print('Digite apenas caracteres.')
    validacao = False        
    inicio = time.time() ## mesma função do time.clock()
    input('Digite a palavra: ')
    fim = time.time()
    tempo = round(fim - inicio,2)
    tempos.append(tempo)
    vezes.append(vez)
    vezstr = str(vez)+ 'a vez'
    legenda.append(vezstr)
    vez +=1
       
   
plt.xticks(vezes,legenda) ## vai substituir os nomes da lista vezes pela lista legenda
plt.plot(vezes,tempos)
plt.show()




