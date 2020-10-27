##Exercício: Validação de Dados
##Abra o programa que calcula a média e imprime a situação do aluno,
##feito no exercício sobre condicionais.Aplique a validação
##de dados para que:
##
##- O programa nunca seja interrompido por erro
##- A nota seja entre 0 e 10
##- O número de faltas seja entre 0 e 20

nome = input("Digite seu nome: ")
valid_nota = False
while valid_nota == False:
    nota_prova1= input("Digite sua nota1: ")
    try:
        nota_prova1 = float(nota_prova1)
        if nota_prova1 <0 or nota_prova1 >10:
            print('A nota tem que ser entre 0 e 10')
        else:
            valid_nota= True
    except:
        print('Nota inválida. Use apenas números e separe os decimais com ponto. (ex: 9.5)')

        
valid_nota = False
while valid_nota == False:
    nota_prova2= input("Digite sua nota2: ")
    try:
        nota_prova2 = float(nota_prova2)
        if nota_prova2 <0 or nota_prova2 >10:
            print('A nota deve ser entre 0 e 10')
        else:
            valid_nota = True
    except:
        print('Nota inválida.Use apenas números e separe os decimais com ponto. (ex: 9.5)')

valid_falta= False

while valid_falta == False:
    faltas= input("Total de faltas: ")
    try:
        faltas = float(faltas)
        if faltas <0 or faltas >20:
            print('Faltas devem ser entre 0 e 20')
        else:
            valid_falta = True
    except:
        print('Valor inválido. Tente novamente')

        
media = (nota_prova1 + nota_prova2)/ 2
assid = (20-faltas)/20 *100

      
       
          
      
     

               
if media>=6 and assid >=70:
    print("Aluno:",nome,"\n"
          "Média:",media,"\n"
          "Percentual de presença:", str(assid)+"%""\n"
          "Resultado: Aprovado")
elif media <6 and assid <70:
    print("Aluno:",nome,"\n"
          "Média:",media,"\n"
          "Percentual de presença:", str(assid)+"%""\n"
          "Resultado: Reprovado por faltas e por média")
elif media <6:
    print("Aluno:",nome,"\n"
          "Média:",media,"\n"
          "Percentual de presença:", str(assid)+"%""\n"
          "Resultado: Reprovado por média")
elif assid <70:
    print("Aluno:",nome,"\n"
          "Média:",media,"\n"
          "Percentual de presença:",str(assid)+"%""\n"
          "Resultado: Reprovado por faltas")
else:
    print('ERROR')

