n = 1
even = odd = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n!= 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

print('Você digitou {} números pares e {} números ímpares!'.format(even, odd))
