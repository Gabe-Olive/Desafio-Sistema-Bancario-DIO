opcoes = '''
        Bem vindo ao Banco da Capital!
        (1) Saque
        (2) Depósito
        (3) Extrato
        (4) Sair 
        '''
limitesaque = 3
saldo = 0
extrato = ''

while True: 
    print(opcoes.center(20))
    escolha = int(input('Escolha uma das Opções acima para prosseguir: '))

    if escolha == 1:
            valorsaque = float(input('Insira o valor que deseja sacar: '))
            if limitesaque == 0:
                print('O número de saques permitido foi alcançado. Tente novamente mais tarde.')
            elif valorsaque > 500:
                print('O limite de saque permitido é de R$500.00. Tente novamente.')
            elif valorsaque > saldo:
                print('O valor do saque excede o valor do saldo.')
            elif valorsaque <= 0:
                print('Valor inválido. Por favor tente novamente!')
            elif valorsaque <= saldo:
                extrato += f'Saque: R${valorsaque:.2f}\n'
                saldo -= valorsaque
                limitesaque -= 1
                print(f'Valor de R${valorsaque:.2f} sacado com sucesso')

    elif escolha == 2:
            valordeposito = float(input('Insira o valor que deseja depositar: '))
            if valordeposito <= 0:
                print('Valor inválido. Por favor tente novamente!')
            else:
                saldo += valordeposito
                extrato += f'Depósito: R${valordeposito:.2f}\n'
                print(f'Valor de R${valordeposito} depositado com sucesso')

    elif escolha == 3:
            if extrato == '':
                print('====== Extrato ======')
                print(f'Não foram realizadas movimentações!\nSaldo: R${saldo:.2f}')
                print('=====================')
            else:
                print('====== Extrato ======')
                print(extrato)
                print(f'Saldo: R${saldo:.2f}')
                print('=====================')

    elif escolha == 4:
          print('Muito obrigado por utilizar nossos serviços! Até mais!')
          break
    
    else:
         print('Opção inválida! Por favor, tente novamente!')
            