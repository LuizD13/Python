"""
Funções úteis (built-in)
isnumeric - retorna true se todos os caracteres da string são números
isdigit - retorna true se todos os caracteres fazem parte de um inteiro
isdecimal - retorna true se todos os caracteres da string são decimais
"""

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    print(int(num1)+int(num2))
except:
    print('Não pude converter.')