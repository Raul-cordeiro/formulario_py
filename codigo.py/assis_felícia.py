#ficha de cadastro
from time import sleep
venda = str(input('nova venda digite sim ou não: '))
while venda == 'S, s':
    print('ficha de clientes')
    sleep(1)
    print('vamos iniciar')
    sleep(2)
    print('*****adicione os dados do cliente*****')
    print('=-' * 10)
    sleep(1)
    nome = str(input('nome: ')).upper()
    print('=-' * 10)
    sleep(2)
    sexo = str(input('sexo: '))
    print('=-' * 10)
    sleep(2)
    idade = str(input('idade: '))
    print('=-' * 10)
    sleep(2)
    estado_civil = str(input('estado civíl: '))
    print('=-' * 10)
    sleep(2)
    data_nasc = int(input('data de nascimento: '))
    print('=-' * 10)
    sleep(2)
    produto = str(input('tipo de produto: ')).upeer()
    print('=-' * 10)
    print('digite (v) para avista ou (P)para a prazo')
    forma_de_pagamento = str(input('forma de pagamento: '))
    if forma_de_pagamento == 'P':
        cpf = int(input('digite cpf: '))

    print('=-' * 10)
    sleep(2)
    venda = str(input('nova venda digite sim ou não: '))
    sleep(2)
    print('processando')
    print('raul Cordeiro agradece\n obrigado por escolher nossos produtos')
    
    

