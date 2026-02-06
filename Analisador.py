maiorn=0
menorn=0
soma=0
media=0
pares=0
impares=0
positivos=0
negativos=0
zero=0
tot=int(input('Digite o total de números que você deseja analisar: '))
for t in range(1,tot+1):
    nu=int(input('Digite um número: '))
    soma = soma + nu
    media = soma / (tot)
    if t==1:
        maiorn=nu
        menorn=nu
    if nu > maiorn:
        maiorn=nu
    if nu < menorn:
        menorn=nu
    if nu % 2==0:
        pares=pares+1
    if nu % 2 !=0:
        impares=impares+1
    if nu > 0:
        positivos = positivos + 1
    if nu < 0:
        negativos = negativos + 1
    if nu == 0:
        zero = zero + 1

print(f'Maior número: {maiorn}')
print(f'Menor número: {menorn}')
print(f'Soma: {soma}')
print(f'Média: {media}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
print(f'Positivos: {positivos}')
print(f'Negativos: {negativos}')
print(f'Zero: {zero}.')