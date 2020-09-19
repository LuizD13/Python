"""
For in - Estrutura de repetição em Python
Iterando Strings com For
função range (start=0,stop,step=1)
"""

texto = 'Python basico'
nova_string = ''

numero2 = 11

for letra in texto:
    if letra == 't' or letra == 'h':
        continue  # ele pula para a próxima repetição
        nova_string = nova_string + letra.upper()
    else:
        nova_string += letra
        break  # interrompe a repetição e termina o For
    # print(letra.strip())  # strip - remove espaços da string
print(nova_string)

for numero in range(11, 132, 11):  # múltiplos de 11 até o próprio 11
    print(numero)

