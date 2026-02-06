maior=0
menor=0
publi=int(input('Digite a quantidade de publicações que você deseja analisar: '))
for d in range(1,publi + 1):
    dados=int(input(f'Digite o número de curtidas da {d}ª foto: '))
    if d == 1:
        maior = dados
        menor = dados
    else:
        if dados > maior:
            maior = dados
        if dados < menor:
            menor = dados
print(f'A foto com mais curtidas teve {maior} curtidas.')
print(f'A foto com menos curtidas teve {menor} curtidas.')
