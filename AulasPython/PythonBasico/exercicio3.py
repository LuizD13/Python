"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos, escreva: "Seu nome é curto"; Se tiver entre 5 e 6 letras, escreva:
"Seu nome é normal"; maior que 6 escreva: "Seu nome é muito grande"
"""
primeiro_nome = input('Digite seu primeiro nome: ')

try:
    if len(primeiro_nome) >=1 and len(primeiro_nome) <=4:
        print('Seu nome é curto.')
    elif len(primeiro_nome) >=5 and len(primeiro_nome) <=6:
        print('Seu nome é normal.')
    elif len(primeiro_nome) >=6:
        print('Seu nome é muito grande.')
    else:
        print('Digite um nome válido.')
except:
    print('Digite um nome válido.')