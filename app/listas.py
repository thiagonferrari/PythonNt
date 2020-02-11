lista = []
lista = ['Thiago', 'Fulano', 'Ciclano', 'Beltrano', 'Aquele lá']

#----- Tamanho da lista
print(len(lista))

#----- Pegando um dado na lista
print(lista[0])
#----- Pegando intervalo
print(lista[1:3])
#----- Pegando intervalo reverso
print(lista[3:1:-1])

#----- For com range - usa idx
for i in range(0,5):
    print(lista[i])

#----- For com dados - melhor pra percorrer vetor
for n in lista:
    print(n)