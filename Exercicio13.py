from Exercicio11 import gera_numero_aleatorios

numeros = gera_numero_aleatorios(20)
numeros = [str(numero) for numero in numeros]
numeros_agrupados = "".join(numeros)

print(f"Os números da lista agrupados sem espaço geram a seguinte string:\n {numeros_agrupados.replace(' ', '')}")