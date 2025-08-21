'''
múltiplo de 3 e 5 - print fizzbuzz
multiplo de 3 - fizz
multiplo de 5 - buzz
multiplo de nenhum - print o valor
'''
def fizzBuzz(n):
    for num in range (1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')
        else:
            print(num)

n = int(input().strip())

fizzBuzz(n)
