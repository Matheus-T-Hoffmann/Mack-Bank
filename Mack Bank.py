'''
Projeto 2 - Algoritmos e Programação 1
Integrantes:
Marcos Pedro Scherer
Matheus Tramont Hoffmann
'''

import random
import time

def print_linha():
  return print('_______________________________________________________________________')

#Função para receber o input de nome e previnir que ele seja vazio
def confere_nome():
  nome = str(input('Nome do cliente: '))
  while len(nome) == 0:
    nome = str(input('Nome do cliente: '))
  return nome

#A mesma função, para o telefone
def confere_telefone():
  telefone = str(input('Telefone: '))
  while len(telefone) == 0:
    telefone = str(input('Telefone: '))
  return telefone

#A mesma função, para o email
def confere_email():
  email = str(input('Email: '))
  while len(email) == 0:
    email = str(input('Email: '))
  return email

#Função para receber o input de saldo e previnir que ele seja menor que 1000
def confere_saldo():
  saldo = float(input('Saldo inicial: R$ '))
  while saldo < 1000:
    print('Seu primeiro deposito deve ser maior ou igual a R$1,000.00')
    saldo = float(input('Saldo inicial: R$ '))
  return saldo

#Função que performa o cadastro de senha, obrigando que ela tenha 6 caracteres e verificando-a duas vezes
def confere_senha():
  senha2 = "x"
  senha1 = "x"
  while len(senha1) != 6:
    print('Sua senha deve conter 6 caracteres.')
    senha1 = str(input('Senha: '))
  while senha1 != senha2:
    senha2 = str(input('Confirme sua senha: '))
  return senha1

#Função para tentativas de senha. No caso de 3 erros, retorna 0 e bloqueia as opções que requerem acesso a conta
def confirma_senha(senha_cliente):
  tentativas = 2
  senha = input('Digite sua senha: ')
  while senha != senha_cliente and tentativas > 0:
    print(f'Senha incorreta. Tentativas restantes: {tentativas}')
    senha = input('Digite sua senha: ')
    tentativas-=1
  if senha == senha_cliente:
    print('Senha digitada corretamente.')
    return 1
  else:
    print('Tentativas de senha finalizadas. Opções 3, 4, 5 e 6 bloqueadas')
    return 0

#Função que verifica se o número da conta digitado está correto
def confere_conta(numero_conta):
  conta_input = input('Informe o número da conta: ')
  while conta_input != numero_conta:
    print('Seu número de conta não foi encontrado. Por favor tente novamente.')
    conta_input = input('Informe o número da conta: ')

#Função que recebe o valor do depósito e obriga que seja maior que zero
def confere_valor_deposito():
  deposito = float(input('Valor do depósito: R$ '))
  while deposito <= 0:
    print('Seu deposito deve ser maior que zero.')
    deposito = float(input('Valor do depósito: R$ '))
  return deposito

#A mesma função, para o saque
def confere_saque():
  saque = float(input('Valor do saque: R$ '))
  while saque <= 0:
    print('Seu saque deve ser maior que zero.')
    saque = float(input('Valor do saque: R$ '))
  return saque

#Função responsável por gerar o número de conta aleatório. No caso de um número menor que 1000, adiciona zeros na frente, sendo uma string
def gereAleatorio():
  min = 0
  max = 9999
  numero_conta = str(random.randint(min, max))
  numero_conta = (len(str(max))-len(numero_conta))*'0'+ numero_conta
  return numero_conta

#Função que formata a lista historico_op para ser lida na opção de Consultar Extrato
def lista_operações():
  for i in historico_op:
    if i > 0:
      print(f'Depósito: R$ {i:.2f}')
    else:
      i = i *-1
      print(f'Saque: R$ {i:.2f}')

opção = 0
historico_op = []
contador1 = 0
aval_senha = 1

#Loop do menu
while True:
    print('MACK BANK - ESCOLHA UMA OPÇÃO')
    print_linha()
    print("(1) Cadastrar conta corrente\n(2) Depositar\n(3) Sacar\n(4) Consultar saldo\n(5) Consultar extrato\n(6) Alterar dados da conta\n(7) Finalizar\n")
    opção = int(input(f'Sua opção: '))
    print('')

    #Requer que a opção 1 nunca tenha sido acessada
    if opção == 1 and contador1 == 0:
        #CADASTRAR CONTA CORRENTE
        print('MACK BANK - CADASTRO DE CONTA')
        print_linha()
        conta_cadastrada = gereAleatorio()
        print(f'Número da conta: {conta_cadastrada}')
        nome_cliente = confere_nome()
        telefone_cliente = confere_telefone()
        email_cliente = confere_email()
        saldo_cliente = confere_saldo()
        limite_cliente = 1000
        print(f'Limite de crédito: R$ {limite_cliente:.2f}')
        senha_cliente =  confere_senha()
        print('Cadastro realizado!')
        time.sleep(1)
        input('Aperte Enter para voltar ao menu... ')
        contador1 += 1
    elif opção == 1 and contador1 != 0:
        print('Você já cadastrou sua conta.')
        time.sleep(1)
        print('')

    #Requer que a opção 1 já tenha sido acessada
    if opção == 2 and contador1 == 1:
        #DEPOSITAR
        print("MACK BANK - DEPÓSITO")
        print_linha()
        confere_conta(conta_cadastrada)
        print(f'Nome do cliente: {nome_cliente}')
        deposito = confere_valor_deposito()
        saldo_cliente += deposito
        historico_op.append(deposito)
        print('Depósito realizado com sucesso!')
        time.sleep(1)
        input('Aperte Enter para voltar ao menu... ')

    #A opção só pode ser acessada se a opção 1 de cadastro já foi completa. Isto é necessário, já que apenas uma conta pode receber depósitos nesse código
    elif opção == 2 and contador1 == 0:
       print('É necessário cadastrar sua conta primeiro.')
       time.sleep(1)
       print('')

    #Requer que a opção 1 tenha sido acessada e que a confirmação de senha não tenha falhado anteriormente
    if opção == 3 and aval_senha == 1 and contador1 == 1:
       #SAQUE
        print('MACK BANK - SAQUE')
        print_linha()
        confere_conta(conta_cadastrada)
        print(f'Nome do cliente: {nome_cliente}')
        aval_senha = confirma_senha(senha_cliente)
        #Este trecho apenas procede se o usuário acertar a senha dentor das 3 tentativas
        if aval_senha == 1:
            valor_saque = confere_saque()
            #Esta cadeia if-elif-else avalia se é possível fazer o saque e, caso seja, se o limite de crédito será usado.
            if valor_saque <= saldo_cliente:
                saldo_cliente -= valor_saque
                historico_op.append(valor_saque*-1)
            elif valor_saque <= saldo_cliente + limite_cliente:
                historico_op.append(valor_saque*-1)
                valor_saque -= saldo_cliente
                saldo_cliente = 0
                limite_cliente -= valor_saque
                print('VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO')
            else:
                print('Seu saque excede o valor do seu saldo + seu limite de crédito.')
            print('Saque realizado com sucesso!')
        time.sleep(1)
        input('Aperte Enter para voltar ao menu... ')

    #Caso a confirmação de senha tenha fracassado, a opção está bloqueada.
    elif opção == 3 and aval_senha == 0:
       print('Opção bloqueada.')
       time.sleep(1)
       print('')

    #A opção só pode ser acessada se a opção 1 de cadastro já foi completa
    elif opção == 3 and contador1 == 0:
       print('É necessário cadastrar sua conta primeiro.')
       time.sleep(1)
       print('')

    #As mesmas condições da opção 3 se aplicam às opções 4, 5 e 6
    if opção == 4 and aval_senha == 1 and contador1 == 1:
        #CONSULTAR SALDO
        print('MACK BANK - SALDO EM CONTA')
        print_linha()
        confere_conta(conta_cadastrada)
        print(f'Nome do cliente: {nome_cliente}')
        aval_senha = confirma_senha(senha_cliente)
        if aval_senha == 1:
            print(f'Saldo em conta: R$ {saldo_cliente:.2f}')
            print(f'Limite de crédito: R$ {limite_cliente:.2f}')
        time.sleep(1)
        input('Aperte Enter para voltar ao menu... ')
    elif opção == 4 and aval_senha == 0:
       print('Opção bloqueada.')
       time.sleep(1)
       print('')
    elif opção == 4 and contador1 == 0:
       print('É necessário cadastrar sua conta primeiro.')
       time.sleep(1)
       print('')

    if opção == 5 and aval_senha == 1 and contador1 == 1:
       #CONSULTAR EXTRATO
        print('MACK BANK - EXTRATO DA CONTA')
        print_linha()
        confere_conta(conta_cadastrada)
        print(f'Nome do cliente: {nome_cliente}')
        aval_senha = confirma_senha(senha_cliente)
        if aval_senha == 1:
            print(f'Limite de crédito: R$ {limite_cliente:.2f}')
            print('ÚLTIMAS OPERAÇÕES:')
            lista_operações()
            print(f'SALDO EM CONTA: R$ {saldo_cliente:.2f}')
            if saldo_cliente < 0:
                print('Atenção ao seu saldo!')
            time.sleep(1)
            input('Aperte Enter para voltar ao menu... ')
    elif opção == 5 and aval_senha == 0:
       print('Opção bloqueada.')
       time.sleep(1)
       print('')
    elif opção == 5 and contador1 == 0:
       print('É necessário cadastrar sua conta primeiro.')
       time.sleep(1)
       print('')

    #Esta opção é a nova funcionalidade do nosso código. Ela permite alterar o telefone, email e senha da conta, após cadastro e confirmação da senha
    if opção == 6 and aval_senha == 1 and contador1 == 1:
       #ALTERAR DADOS DA CONTA
        print('MACK BANK - ALTERAR DADOS DA CONTA')
        print_linha()
        confere_conta(conta_cadastrada)
        print(f'Nome do cliente: {nome_cliente}')
        aval_senha = confirma_senha(senha_cliente)
        if aval_senha == 1:
            opção_dados = 0
            while opção_dados < 1 or opção_dados > 3:
                print('(1) Alterar telefone\n(2) Alterar email\n(3) Alterar senha')
                opção_dados = int(input('Sua opção: '))
            if opção_dados == 1:
                print(f'Telefone atual: {telefone_cliente}')
                telefone_cliente = confere_telefone()
            elif opção_dados == 2:
                print(f'Email atual: {email_cliente}')
                email_cliente = confere_email()
            elif opção_dados == 3:
                senha_cliente = confere_senha()
            time.sleep(1)
            input('Aperte Enter para voltar ao menu... ')
    elif opção == 6 and aval_senha == 0:
       print('Opção bloqueada.')
       time.sleep(1)
       print('')
    elif opção == 6 and contador1 == 0:
       print('É necessário cadastrar sua conta primeiro.')
       time.sleep(1)
       print('')
    
    #Opção que quebra o loop do código
    if opção == 7:
       #FINALIZAÇÃO
        print('MACK BANK - SOBRE')
        print_linha()
        print('Este programa foi desenvolvido por\nMarcos Pedro Scherer\nMatheus Tramont Hoffmann')
        time.sleep(1)
        break