from base import imp, lin
from core import User


lin(25)
imp('LOGIN/CADASTRO')
lin(25)

menu =['CASDASTRAR','LOGIN','SAIR']

c = 0
for e in menu:
    c = c+1
    imp(f'{c}-{e}')
lin(25)
opc = int(input('Opção: '))

if opc == 1:
    val =''
    while val != 'N':
        nome = str(input('Nome:  '))
        senha = str(input('Senha:  '))
        user = User(nome, senha)
        user.cadastrar()
        val = str(input('Deseja continuar?[S/N] ')).upper()
        if val == 'S':
            continue
        elif val == 'N':
            break 
        else:
            imp('Entrada inválida! Digite [S/N]')

elif opc == 2:
    nome1 = str(input('Nome: ')).strip()
    senha1 = str(input('Senha: ')).strip()
    file = open('contas.txt')
    if nome1 and senha1 in file.read():
        imp('Conta encontrada')
    else:
        imp('ops! Crie uma conta..')
        

elif opc == 3:
    exit()

else:
    imp('Entrada inválida!')



