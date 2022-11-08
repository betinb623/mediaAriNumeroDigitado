qv = int(input('Qtde de valores: '))
print()  # salta uma linha
s = 0  # armazena a soma dos valores (acumulador)
for i in range(qv):  # repete qv vezes
    val = float(input(f'Valor {i + 1}: '))  # leitura dos valores
    s += val  # soma dos valores

ma = s / qv  # cálculo da média
print(f'\nMédia aritmética = {ma:.2f}')