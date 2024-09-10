# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

print('=' * 50)
print(f'{'VALIDANDO EXPRESSÕES MATEMÁTICAS':^50}')
print('=' * 50)

expression = str(input('Digite a expressão: ')).strip()
print('Sua expressão está válida!' if expression.count('(') == expression.count(')') else 'Sua expressão está errada!')
