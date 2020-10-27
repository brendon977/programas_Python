repetir = 's'
fatura = []
total = 0
valid_preco = False

while repetir == 's':
    produto = input('Digite o nome do produto: ')
    
    while valid_preco == False:     ## transformar a string em float uma vez que o input foi inserido.
        preco = input('Digite o preço do produto: ')
        try: ## vai tentar realizar algo, se não conseguir ele realizará uma exceção(except)
            preco = float(preco)
            if preco <= 0: ## validar se o numero é maior que zero.
                print('O preço precisa ser maior que zero')
            else:
                valid_preco = True
            
        except:
            print("Formato de preço inválido. Use apenas números e separe os centavos com '.'.")
    
    fatura.append([produto,preco]) ## se eu quiser adicionar mais de uma variavel , eu as coloco dentro de uma lista.
    total += preco
    valid_preco = False
    repetir = input('Deseja comprar mais algum produto? (S ou N)').lower()

for i in fatura:
    print(i[0],'-',i[1])

print('O total da fatura é', total)    
