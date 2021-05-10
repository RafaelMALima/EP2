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
    print (naipes)
    print (valores)
    if indice == 1 or indice == 2:
        if naipes[indice] == naipes[indice -1] or valores[indice] == valores[indice -1]:
                movimentos.append(1)
    elif indice != 0:
        if naipes[indice] == naipes[indice -1] or valores[indice] == valores[indice -1]:
            movimentos.append(1)
        if naipes[indice] == naipes[indice -3] or valores[indice] == valores[indice -3]:
            movimentos.append(3)

    return movimentos

