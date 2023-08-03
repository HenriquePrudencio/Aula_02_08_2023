from Exercicio4 import  gera_numero_aleatorios

lista = gera_numero_aleatorios(10)

nomes = ["Roberta", "Josefa", "Anastácio", "Ana", "Oswaldo", "Rogério", "Biro Biro"]
lista.append(nomes)

lista_inteiros = [numero for numero in lista if isinstance(numero, int)]

print(f"A lista contendo apensa números é \n{lista_inteiros}")