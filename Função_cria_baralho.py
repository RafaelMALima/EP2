def cria_baralho ():
    #Ta feio pra burro, e com certeza tem um jeito melhor de fazer. Infelizmente nao faco ideia ent por enquanto fica assim mesmo. Se eu pensar um jeito melhor eu comento essa jossa aqui em baixo.
    baralho = ['A♠','J♠','Q♠','K♠','A♥','J♥','Q♥','K♥','A♦','J♦','Q♦','K♦','A♣','J♣','Q♣','K♣']
    for i in range (2,11):
        baralho.append('{}♠'.format(i))
    for i in range (2,11):
        baralho.append('{}♥'.format(i))
    for i in range (2,11):
        baralho.append('{}♦'.format(i))
    for i in range (2,11):
        baralho.append('{}♣'.format(i))

    print (baralho)
    print (len(baralho))
    return baralho
        