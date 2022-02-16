from funcoes import bytesto
##variaveis globais

tamanho = []
porcentagem_tamanho = []
espaco_total = 0
nomes = []
count = 0

##ler os usuarios.txt
with open("usuarios.txt", "r") as arquivo:
    linha = arquivo.readlines()

    ##para cada string em uma linha retire o espaçamento e crie uma lista##
    ##pegue o segundo elemento da lista(os bytes do txt de cada usuario) e faça a conversao em mb
    ##dada essa conversão crie uma lista com somente os tamanhos de disco dos usuarios
    for n in linha:
        valores = n.split()
        byte = round(bytesto(valores[1], "m"), 3)
        tamanho.append(byte)
        espaco_total += byte
        nomes.append(valores[0])

    ##para cada elemento no tamanho de disco, calcule a porcentagem com base no  espaço total
    ##adicione uma lista sobre lista com o tamanho e a porcentagem que ele representa
    for elemento in tamanho:
        porcentagem = (elemento * 100)/espaco_total
        porcentagem_tamanho.append(round(porcentagem,2))



with open("relatorio.txt", "w") as relatorio:
    relatorio.write("""ACME Inc.           Uso do espaço em disco pelos usuários
---------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso
                                                 
""")
    for nome in nomes:
        disco_porcentagem = porcentagem_tamanho[count]
        disco_tamanho = tamanho[count]
        count +=1
        relatorio.write(f"{count:<4} {nome:<12} {disco_tamanho:<22} {disco_porcentagem}% \n")





    print("o tamanho usado em cada disco é {}(MB)".format(tamanho))
    print("o espaço total utilizado é {} MB".format(espaco_total))
    print("lista com porcentagem do espaço total -> {}".format(porcentagem_tamanho))







