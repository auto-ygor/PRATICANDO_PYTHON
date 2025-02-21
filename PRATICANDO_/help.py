#Neste arquivo, é possível entender o que todas as funções contidas na pasta "praticando_" fazem!!

'''
Para importar as funções de determinado arquivo/exercício, cheque a pasta 
em que ele está e veja um arquivo python chamado "func_nomeDoArquivo.py".

Exemplo de como importar as funçoes do arquivo escolhido: from func_nomeDoArquivo/Exercicio import *

Caso queira importar funções específicas: from func_nomeDoArquivo/Exercicio import funcao_escolhida
'''

#Exemplo (mude conforme os exemplos acima):
from utilidades.utils import message

#Obtém a ajuda (passe a função escolhida como parâmetro):
help(message)