"""
Faça um programa que peça ao usuário para digitar um número inteiro.
Informe se este número é par ou impar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""


num = input('Digite um número inteiro: ')

try:
    if int(num) % 2==0:
        print('Esse número é par.')
    elif int(num) % 2!=0:
        print('Esse número é impar.')
except:
    print('Digite um número inteiro válido.')