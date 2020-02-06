"""
Formatações
"""

nome = 'Luiz Cláudio' #str
idade=32 #int
altura=1.80 #float
e_maior= idade > 18 #bool(True / False)
peso=80
imc=peso/(altura**2)

print(nome,'tem',idade,'anos de idade, e seu IMC é:',imc)
print(f'{nome} tem {idade} anos de idade, e seu IMC é: {imc}')#f - Formata a string exibida
print(f'{nome} tem {idade} anos de idade, e seu IMC é: {imc:.2f}')#.2f - Formata o float para a quantidade de casas decimais(2f,3f,1f, etc.)
print('{} tem {} anos de idade, e seu IMC é: {:.2f}'.format(nome, idade, imc))#Format - Formata a string com os valores entre parênteses