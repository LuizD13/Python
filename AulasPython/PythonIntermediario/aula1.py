"""
Funções por def

"""


def soma(num1, num2):
    total = num1 + num2
    return total


def aviso(texto):
    print(f'Aviso: {texto}')


try:
    print(soma(int(input('Digite um número válido: ')), int(input('Digite outro número válido: '))))
except:
    aviso('Erro no cálculo, por favor tente novamente.')
