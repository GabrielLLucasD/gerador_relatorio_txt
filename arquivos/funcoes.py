

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

if __name__ == "__main__":
    bytes = float(input("entre com os bytes: "))
    unidade = input("entre com a unidade que deseja(escreva somente a primeira letra, ex 'm' para mb)-> ")
    print("{}b = {}".format(unidade,bytesto(bytes,unidade)))
