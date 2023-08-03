# import random
# print([random.randint(20, 1580) for _ in range(10)])
#
# numeros_aleatorios = []
#
# for _ in range(10):
#     numeros_aleatorios.append(random.randint(20, 1580))
#
# print(numeros_aleatorios)

import random
def gera_numero_aleatorios(quantidade) -> list:
    numeros_aleatorios = []

    for _ in range(quantidade):
        numeros_aleatorios.append(random.randint(20, 1580))
    return numeros_aleatorios

print(gera_numero_aleatorios(10))