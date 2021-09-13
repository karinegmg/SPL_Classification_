listaCerta = ['1', '2', '3', '4']

dicio = [('padrao1', '[1, 2, 3]'), ('padrao2', listaCerta), ('padrao3', '[1, 2, 3]')]

tags = dict(dicio)

print(tags['padrao1'])

listaErrada = ['3', '2', '1', '4']


print(sorted(listaErrada) in tags.values())

# listaErrada = ['3', '2', '1', '4']
# listaErrada.sort()

# print(listaErrada in tags.values())