from Exercicio4 import gera_numero_aleatorios

lista = gera_numero_aleatorios(10)

nomes = ["Roberta", "Josefa", "Anastácio", "Ana", "Oswaldo"]
[lista.append(nomes) for nome in nomes]

print(f"Os números da lista agrupados em espaço geram a seguinte String: \n {''.join([str(item) for item in lista])}")