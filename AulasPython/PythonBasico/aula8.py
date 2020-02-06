"""
Entrada de dados(Input) - Aula 3
"""

nome = input('Qual o seu nome? ')#input - Pede um valor ao usuário - Sempre retorna string, a menos que sela feito TypeCast(int())
idade = input('Qual a sua idade? ')

ano_nasc=2020-int(idade)

print(f'{nome} tem {idade} anos, e nasceu em {ano_nasc}')