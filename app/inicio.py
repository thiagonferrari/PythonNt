# #----- Impressão
# print('\n')
# print('*' * 50)
# print('Ola', 'Joelma', 'do Calypso')
# print('Ola' + 'Chimbinha' + 'do Calypso')
# print('*' * 50)

#----- Pegar entrada do usuário
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

#----- Usando format para concatenação de string
print('ola {} {}' .format(nome, sobrenome))

#----- Interpolação de strings
print(f'ola {nome} {sobrenome}')

idade = int(input('Digite a idade'))
print(idade)