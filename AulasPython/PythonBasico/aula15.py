"""
Formatando valores com modificadores

format()

:s - Texto (strings)
:d - inteiros (int)
:f - numeros de ponto flutuante (float)
:.(Numero)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s,d ou f)

< - ESQUERDA
> - DIREITA
^ - CENTRO
"""
num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))

nome = 'Luiz Otávio'
print(f'{nome:s}')

num_1 = 1
print(f'{num_1:0>10}') # 9 zeros + numero

num_2 = 1150
print(f'{num_2:0<10}') # 6 zeros + numero

nome = 'Luiz Cláudio'
print(f'{nome:#^50}')

nome_formatado = '{}'.format(nome)
