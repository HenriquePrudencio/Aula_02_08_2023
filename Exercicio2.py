import re
frase = 'Paulo é d4veloper e um b0m musico'
print(re.findall(r'\w*\d\w*', frase))


# palavras = ('Paulo é d4veloper e um b0m musico').split()
# palavras_com_numeros = []
#
# for palavra in palavras:
#     tem_numero = any(c.isdigit() for c in palavra)
#     somente_letras = any(c.isalpha() for c in palavra)
#     if tem_numero:
#         palavras_com_numeros.append(palavra)
#     else:
#         print(f"Palavra somente com letras {palavra}")
#
# print(f"Palavras com números e letras {palavras_com_numeros}")