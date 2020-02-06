"""
Quantidade de caracteres
"""

usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')
qtd_caracteres = len(usuario + senha)#len = retorna a quantidade de caracteres em uma string como int

print(f'A quantidade total de caracteres digitados foi {qtd_caracteres}')
