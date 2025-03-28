from lib.interface import *
from arquivo.__init__ import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho("Opção 1")
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho("Opção 2")
        cabeçalho('NOVO CADASTRO')
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('OPÇÃO DE SAIR DO SISTEMA')
        cabeçalho("Saindo do sistema... Até logo!")
        break
    else:
        # Opção inválida
        print("\033[31mERRO! digite uma opção válida.\033[m")
    sleep(2)
