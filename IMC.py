print('Vem descobrir o valor do  seu \033[4mIMC\033[m!')
peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura (em \033[1mmetros\033[m): '))
imc=peso/altura**2
if imc<18.5:
    print(f'Seu IMC deu: {imc:.1f} e você está classificado(a) no grupo: \033[4;31mmagreza\033[m!')
elif imc>=18.5 and imc<=24.9:
    print(f'Seu IMC deu: {imc:.1f} e você está classificado(a) no grupo: \033[4;32mpeso normal\033[m.')
elif imc>=25.0 and imc<=29.9:
    print(f'Seu IMC deu {imc:.1f} e você está classificado(a) no grupo: \033[4;33msobrepeso\033[m!')
elif imc>=30.0 and imc<=39.9:
    print(f'Seu IMC deu: {imc:.1f} e você está classificado(a) no grupo: \033[4;31mobesidade\033[m!')
else:
    print(f'CUIDADO! \nSeu IMC deu: {imc:.1f} e você está classificado(a) no grupo: \033[4;31mobesidade grave\033[m!!!')

