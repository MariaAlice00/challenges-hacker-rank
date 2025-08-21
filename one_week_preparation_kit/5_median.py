def organizando(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr)

def findMedian(arr):
    arr = organizando(arr)
    mediana = 0
    pos_meio_um = len(arr) / 2
    pos_meio_dois = pos_meio_um - 1
    posicao = 0
    if len(arr) == 1:
        mediana = arr[0]
    else:
        if len(arr) % 2 == 0:
            posicao = (arr[pos_meio_um] + arr[pos_meio_dois]) / 2
            posicao = int(posicao)
            mediana = arr[posicao-1]
        else:
            posicao = (len(arr)+1) / 2
            posicao = int(posicao)
            mediana = arr[posicao-1]
    return mediana

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = findMedian(arr)

print(result)