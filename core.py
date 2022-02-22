from base import imp

class User:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def cadastrar(self):
        arq = open('contas.txt', 'a+')
        arq.writelines(f'{self.nome}-{self.senha}\n')
        print(arq.read())
        


