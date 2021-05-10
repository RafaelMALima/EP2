def possui_movimentos_possiveis(baralho):
    restam_movimentos = False
    for i in range (len(baralho)):
        if lista_movimentos_possiveis(baralho,i) != []:
            restam_movimentos = True
    return restam_movimentos