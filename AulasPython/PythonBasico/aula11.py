"""
Operadores lógicos:
and - um e dois são verdadeiros
or - um ou dois é verdadeira
not - não é verdadeiro
in - está em
not in - não está em
"""

a=2
b=3
c=4
d='Luiz Claudio'

print(a == b or b < c) #a igual à b OU b menor que c

print(a==b and b < c)#a igual à b E b menor que c

print(not a==b)#a NÃO for igual à b

if 'u' in d: #se existir 'U' na string do 'd'
    print('Existe a letra U no seu nome.')

if 'v' not in d: #se NÃO existir 'V' na string do 'd'
    print('Não existe a letra V no seu nome.')