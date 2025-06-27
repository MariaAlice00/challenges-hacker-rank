# Primeiro criei uma função para ordenar a lista
# Depois percorri a lista em ordem crescente, somando os valores, parando no penúltimo elemento
# Por fim percorri a lista em ordem descrescente, somando os valores, deixando o primeiro elemento de lado

def sorted_list(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def miniMaxSum(arr):
    # Write your code here
    arr = sorted_list(arr)
    val_min = 0
    val_max = 0
    for x in range(len(arr)-1):
        val_min += arr[x]
    for y in range(len(arr)-1, 0, -1):
        val_max += arr[y]
    print(val_min, val_max)


lista = [13, 21, 3, 14, 5]

miniMaxSum(lista)