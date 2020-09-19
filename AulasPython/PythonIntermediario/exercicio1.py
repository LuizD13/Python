"""
1- Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""

"""
2- Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles.
"""

"""
3- Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual. Retorne o valor do 
primeiro número somado do aumento do percentual do mesmo.
"""

"""
4- Fizz Buzz - Se o parâmetro da função for divisível por 2, retorne fizz, se o parâmetro da função for divisível
por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e 3, retorne FizzBuzz, caso contrário, retorne
o número enviado.

"""


# 1:
def saudacao(nome, saudaca0):
    print(f'{saudaca0}, {nome}!')


saudacao('Luiz Claudio', 'Seja Bem-Vindo')


# 2:
def soma(num1, num2, num3):
    return num1 + num2 + num3


print(
    soma(int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: '))))


# 3:

def percentual(num, percent):
    valor_percent = (num * percent) / 100
    return num + valor_percent


print(percentual(int(input('Digite um número: ')), int(input('Digite uma porcentagem: '))))


# 4:

def fizzbuzz(par):
    if par % 3 == 0 and par % 5 == 0:
        return 'FizzBuzz'
    elif par % 5 == 0:
        return 'Buzz'
    elif par % 3 == 0:
        return 'Fizz'
    else:
        return par


print(fizzbuzz(int(input('Digite um número válido: '))))
