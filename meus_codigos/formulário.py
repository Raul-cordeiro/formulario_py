#ficha de cadastro
from time import sleep
senha = int(input('digite sua senha.. '))
while senha == 1234:
    print('iniciando nova venda')
    if senha != 1234:
        print('tente novamente...')
        senha = int(input('digite sua senha.. '))
    print('ficha de clientes')
    sleep(1)
    print('vamos iniciar')
    sleep(1)
    print('*****adicione os dados do cliente*****')
    sleep(1)
    nome = str(input('nome: ')).upper()
    print('=-' * 10)
    sleep(1)
    sexo = str(input('sexo: '))
    print('=-' * 10)
    sleep(1)
    idade = str(input('idade: '))
    print('=-' * 10)
    sleep(1)
    estado_civil = str(input('estado civíl: '))
    print('=-' * 10)
    sleep(1)
    data_nasc = int(input('data de nascimento: '))
    print('=-' * 10)
    sleep(1)
    produto = str(input('tipo de produto: ')).upper()
    print('=-' * 10)
    print('digite (v) para avista ou (P)para a prazo')
    forma_de_pagamento = str(input('forma de pagamento: '))
    cpf = int(input('digite seu cpf.. '))
    if forma_de_pagamento == 'p':
        forma_de_pagamento == 'prazo'
    else:
        print('pagamento avista')

    print('=-=' * 10)
    sleep(1)
    senha = str(input('deseja fazer uma nova venda digite sim ou não: '))
    if senha == 'nao':    
        sleep(1)
        print('processando')
        sleep(1)
        print('finalizando')
        sleep(1)
        print('Cord_lab agradece\n obrigado por escolher nossos produtos\n grupo Raul Cordeiro')
        sleep(1)
        print('=-=' * 10)
        print('=-=' * 10)
        print('apresentando ficha do cliente')
        sleep(2)
        lista = [nome, sexo, idade, estado_civil, data_nasc, produto, forma_de_pagamento, cpf]
        sleep(2)
        print(lista)
        sleep(1)
        print('fim')
        
        
    