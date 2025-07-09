'''
- Todas as letras da primeira palavra são minúsculas.
- Para cada uma das palavras subsequentes, a primeira letra é maiúscula e as demais são minúsculas.

- retornar a quantidade de palavras
- saveChangesInTheEditor = 5

A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z
'''
def is_upper_lower(l):
    upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
             
    if l in upper:
        return True
    elif l in lower:
        return False


def camelcase(s):
    cont = 1
    for letter in s:
        if is_upper_lower(letter) == True:
            cont += 1
        else:
            pass
    
    return cont


s = input()

result = camelcase(s)

'''
RACIOCÍNIO
- percorrer a string
- se for maiúscula = soma mais 1
- a variável de contagem já começa com 1; a primeira palavra começa com minúscula
'''