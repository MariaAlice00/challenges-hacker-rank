'''
    - percorrer uma lista
    - saber quantos valores a lista tem
    - selecionar quantos números são positivos, negativos e nulos
    - fazer a proporção das quantidades com a quantidade de valores
        ex: são 2 valores positivos e existem 4 valores ao total na lista
            2 / 4 = 0.500000
    OBS: tem que ter 6 valores após a vírgula
'''

def plusMinus(arr):
    positivos = 0
    negativos = 0
    nulos = 0
    for num in arr:
        if num == 0:
            nulos += 1
        elif num >= 1:
            positivos += 1
        else:
            negativos += 1
    a = round(positivos / n, 6)
    b = round(negativos / n, 6)
    c = round(nulos / n, 6) 

    print('{:.6f}'.format(a))
    print('{:.6f}'.format(b))
    print('{:.6f}'.format(c))

n = int(input())
arr = input()