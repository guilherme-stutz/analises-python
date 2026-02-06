usuario ='guilherme-stutz'
senha ='guilherme.stutz123'
u=input('Usuário: ').strip()
s=input('Senha: ').strip()
if u == usuario and s == senha:
    codigo = 'nome-sobrenome'
    print('* \033[4;32mPergunta de Segurança\033[m *')
    c = input('Por que esse nome de usuario? ')
    if c == codigo:
        print('Acesso Liberado!')
    else:
        print('Resposta errada!')
        print('Acesso Negado')
else:
    print('Acesso Negado')
