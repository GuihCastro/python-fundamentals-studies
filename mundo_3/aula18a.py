teste = list()
teste.append('Guilherme')
teste.append(32)
galera = list()
galera.append(teste[:])
teste[0] = 'Mariana'
teste[1] = 32
galera.append(teste[:])
print(galera)
