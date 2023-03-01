from Desafios.ex115.lib.interface import sistema
from Desafios.ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoexiste(arq):
    criarquivo(arq)


while True:
    resposta = sistema.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    else:
        print('\033[34mTenha um bom dia :D\033[m')
        break
