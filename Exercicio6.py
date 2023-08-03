from Exercicio4 import  gera_numero_aleatorios

numeros = gera_numero_aleatorios(10)
print(f"Lista de números inicial é: {numeros}")

for i in range(1, len(numeros), 2):
    print(f"Número {numeros[i]} no indice {i}")