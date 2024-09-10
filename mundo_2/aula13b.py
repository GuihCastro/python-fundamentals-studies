'''n = int(input('Digite um número para finalizar a contagem: '))

for c in range(0, n+1):
    print(c)
print('FIM!')'''

start = int(input('Início: '))
end = int(input('Fim: '))
step = int(input('Passo: '))

for c in range(start, end+1, step):
    print(c)
print('FIM!')
