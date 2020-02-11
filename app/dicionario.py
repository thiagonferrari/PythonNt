lista = []
tupla = ()
dicionario = {'nome':'Thiago', 'sobrenome':'Ferrari', 'idade':17}

#print(dicionario[2])

pessoa1 = {'nome':'Thiago', 'sobrenome':'Ferrari', 'idade':17, 'cpf':13564234}
pessoa2 = {'nome':'João', 'sobrenome':'DasCoves', 'idade':24, 'cpf':56347568}
pessoa3 = {'nome':'Thiago', 'sobrenome':'DaFeira', 'idade':35, 'cpf':45864758}
pessoa4 = {'nome':'Jose', 'sobrenome':'DaInformatica', 'idade':56, 'cpf':8456432}

lista.append(pessoa1)
lista.append(pessoa2)
lista.append(pessoa3)
lista.append(pessoa4)

for n in lista:
    print(n['sobrenome'])
