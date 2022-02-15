def bytesto(bytes, to, bsize=1024):
    """convert bytes to megabytes, etc.
       sample code:
           print('mb= ' + str(bytesto(314575262000000, 'm')))
       sample output:
           mb= 300002347.946
    """

    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes)
    for i in range(a[to]):
        r = r / bsize

    return(r)




with open("usuarios.txt", "r") as arquivo:
    info = arquivo.readlines()
    tamanho = []
    porcentagem_tamanho = []
    espaco_total = 0

    for n in info:
        valores = n.split()
        byte = round(bytesto(valores[1], "m"), 3)
        tamanho.append(byte)
        espaco_total = byte

    for elemento in tamanho:
        porcentagem = (elemento * 100)/espaco_total
        porcentagem_tamanho.append([elemento, round(porcentagem,2)])

    print("o tamanho usado em cada disco é {}(MB)".format(tamanho))
    print("o espaço total utilizado é {} MB".format(espaco_total))
    print("lista com tamanho em MB e em porcentagem do espaço total -> {}".format(porcentagem_tamanho))





