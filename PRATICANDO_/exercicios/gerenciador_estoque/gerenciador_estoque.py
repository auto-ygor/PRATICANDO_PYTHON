from exercicios.utils import message, clear, close_program, option
from exercicios.gerenciador_estoque.funcs_principais_ge import *

#Armazena as informações do estoque:
estoque = {}

#Função principal do programa:
def main(estoque):
    while True:
        message("GERENCIADOR DE ESTOQUE", ["adicionar produto", "remover produto", "listar produto(s)", "consultar produto", "sair"])
        opcao = option(5)
        clear()

        match opcao:
            case 1:
                estoque = adicionar_produto(estoque)
            case 2:
                estoque = remover_produto(estoque)
            case 3:
                listar_produtos(estoque)
            case 4:
                consultar_produto(estoque)
            case 5:
                close_program("Até a próxima!")
                break

#Executa a função principal do programa (main):
if __name__ == "__main__":
    main(estoque)