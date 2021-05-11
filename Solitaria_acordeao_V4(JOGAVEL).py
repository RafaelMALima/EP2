import random 

def extrai_naipe(carta):
    return carta[(len(carta)) - 1]
def extrai_valor(carta):
    return carta[:-1]
def lista_movimentos_possiveis(baralho, indice):
    movimentos = []
    naipes = []
    valores = []
    for i in range(len(baralho)):
        naipes.append(extrai_naipe(baralho[i]))
        valores.append(extrai_valor(baralho[i]))
    if indice == 1 or indice == 2:
        if naipes[indice] == naipes[indice -1] or valores[indice] == valores[indice -1]:
                movimentos.append(1)
    elif indice != 0:
        if naipes[indice] == naipes[indice -1] or valores[indice] == valores[indice -1]:
            movimentos.append(1)
        if naipes[indice] == naipes[indice -3] or valores[indice] == valores[indice -3]:
            movimentos.append(3)

    return movimentos
def empilha(baralho, origem, destino):
    baralho[destino] = baralho[origem]
    baralho.pop(origem)
    return baralho
def possui_movimentos_possiveis(baralho):
    restam_movimentos = False
    for i in range (len(baralho)):
        if lista_movimentos_possiveis(baralho,i) != []:
            restam_movimentos = True
    return restam_movimentos
def cria_baralho ():
    baralho = ['A♠','J♠','Q♠','K♠','A♥','J♥','Q♥','K♥','A♦','J♦','Q♦','K♦','A♣','J♣','Q♣','K♣']
    for i in range (2,11):
        baralho.append('{}♠'.format(i))
    for i in range (2,11):
        baralho.append('{}♥'.format(i))
    for i in range (2,11):
        baralho.append('{}♦'.format(i))
    for i in range (2,11):
        baralho.append('{}♣'.format(i))

    return baralho


baralho = cria_baralho()
random.shuffle(baralho)
continua = True
while continua == True:
    for i in range(len(baralho)):
        print ("{}.{}".format(i + 1, baralho[i]))
    print(len(baralho))
    carta = int(input("Digite o número da posição da carta que você quer mover"))
    if carta - 1 in range (len(baralho)):
        movimentos = lista_movimentos_possiveis(baralho, carta - 1)
        if movimentos == []:
            print("a carta não possui movimentos possíveis")
        elif movimentos == [1,3]:
            print ("Para empilhar sobre {}, digite 1, e para {}, digite 2".format(baralho [carta - 2], baralho[carta - 4]))
            empilhada = int(input("qual a posição da carta que você quer que seja empilhada?"))
            if empilhada == 1:
                baralho = empilha(baralho,carta - 1, carta - 1 - empilhada)
            elif empilhada == 2:               
                baralho = empilha(baralho,carta - 1, carta - 1 - empilhada)
            else:
                print ("este movimento é invalido")
        else:
            baralho = empilha(baralho, carta - 1, carta - 1 - movimentos[0])
    continua = possui_movimentos_possiveis(baralho)

if len(baralho) == 1:
    print("Parabéns, você ganhou!!!")
else:
    print("Você perdeu, que pena! Para tentar novamente, reinicie o código do arquivo")



