from exercicios.cadastro_cartao import funcs_principais_cc as fp
from exercicios.utils import message, option, clear, close_program

#Armazena as informações do(s) cartão(es):                       
dados_cartao = {}

def main(dados_cartao):
    while True:
        message("CADASTRO DE CARTÕES", ['cadastrar cartão', 'ver dados do cartão', 'excluir cartão', 'sair'])
        opcao = option(4)
        clear()
        
        match opcao:
            case 1:
                dados_cartao = fp.cadastrar_cartao(dados_cartao) 
            case 2:
                dados_cartao = fp.ver_dados_cartao(dados_cartao)
            case 3:
                dados_cartao = fp.excluir_cartao(dados_cartao)
            case 4:
                close_program("Tchau!")
                break

#Executa a função principal (main):
if __name__ == "__main__":
    main(dados_cartao)

