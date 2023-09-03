import random

def adivinha(x):
    num_aleatorio = random.randint(1, x)
    adivinha = 0

    while adivinha != num_aleatorio:
        adivinha = int(input(f'Adivinhe o número entre 1 e {x}: '))
        if adivinha < num_aleatorio:
            print('Número errado! pense em um número MAIOR... : ')
        elif adivinha > num_aleatorio:
            print('Número errado! pense em um número MENOR... : ')

    print(f'EURECA!! você pensou no número {num_aleatorio} corretamente!!')

adivinha(10)