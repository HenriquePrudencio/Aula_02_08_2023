# import random
# numeros_aleatorios = [random.randint(20, 1580) for _ in range(10)]
# print(numeros_aleatorios)
# for numero in numeros_aleatorios:
#     if numero % 5 == 0:
#         if numero > 1500:
#             break
#         elif 95 < numero < 150:
#             continue
#         print(numero)

from Exercicio4 import  gera_numero_aleatorios

numeros = gera_numero_aleatorios(10)
print(f"Lista de números aleatórios: \n {numeros}")

for numero in numeros:
    if numero % 5 == 0:
        print(f"Número múltiplo por 5: {numero}")
        if numero > 1500:
            break
        elif 95 < numero < 150:
            print(f"Número {numero} menor que 95 e maior que 150")
        else:
            continue
        print(numero)