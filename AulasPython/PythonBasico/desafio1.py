nome = 'Luiz'
idade=32
altura=1.80
peso=80
ano_atual=2020
imc=peso/(altura**2)
ano_nasc=ano_atual-idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de Luiz é: {imc:.2f}')
print(f'Luiz nasceu em {ano_nasc}.')