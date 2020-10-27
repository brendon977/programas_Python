#Faça um programa que mostre na tela
# uma contagem regressiva para o estouro
# de fogos de artifício, indo de 10 ate 0,
#com uma pausa de 1 segundo entre eles.
from time import sleep
for fogo in range(10,0,-1):
    print(fogo)
    sleep(1)
print("Estorou fogos !!!!")