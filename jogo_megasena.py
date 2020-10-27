##import time
##tempo_detalhes = time.localtime()
##print(tempo_detalhes)
##
##
##tempo = time.localtime()
##hora = tempo.tm_hour
##minutos = tempo.tm_min
##
##print(str(hora) +' horas')
##print(str(minutos) + ' minutos')

import random

def megasena():
	jogo = []
	while len(jogo) <6:
		num = random.randint(1,60)
		if num in jogo:   ## se o num se repetir dentro da lista jogo, ele sai e volta pro inicio
			continue  
		else:             ## agora caso não se repita, ele vai continuar adicionando o numero a lista.
			jogo.append(num)
	print(sorted(jogo)) ## ordena a lista

	
>>> megasena()


##Sequencia que escolhe aluno aleatorio
alunos = ['joao','pedro','maria','helena','guilherme']
random.choice(alunos)

##pega uma amostra da lista alunos
random.sample(alunos,3)
