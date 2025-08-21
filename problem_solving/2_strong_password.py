# '''
# Critérios da senha:
# - Seu comprimento é de pelo menos 6.
# - Contém pelo menos um dígito.
# - Contém pelo menos um caractere minúsculo em inglês.
# - Contém pelo menos um caractere maiúsculo em inglês.
# - Contém pelo menos um caractere especial. Os caracteres especiais são:!@#$%^&*()-+

# números  =  "0123456789" 
# minúsculas  =  "abcdefghijklmnopqrstuvwxyz" 
# maiúsculas  =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
# caracteres_especiais  =  "!@#$%^&*()-+"

# retornar: o número mínimo de caracteres a adicionar
# '''
# def is_number(password):
#     number  =  "0123456789"
#     for letter in password:
#         if letter in number:
#             return True
#     return False

# def is_lower(password):
#     lower  =  "abcdefghijklmnopqrstuvwxyz" 
#     for letter in password:
#         if letter in lower:
#             return True
#     return False

# def is_upper(password):
#     upper  =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     for letter in password:
#         if letter in upper:
#             return True
#     return False

# def is_special(password):
#     special  =  "!@#$%^&*()-+"
#     for letter in password:
#         if letter in special:
#             return True
#     return False

# def minimumNumber(n, password): 
#     add = 0
#     if is_number(password) == False:
#         add += 1
#     if not is_lower(password) == False:
#         add += 1
#     if not is_upper(password) == False:
#         add += 1
#     if not is_special(password) == False:
#         add += 1
#     n += add
#     if n < 6:
#         n += (6-n)
#     return n


# n = int(input().strip())

# password = input()

# answer = minimumNumber(n, password)

# print(answer)
