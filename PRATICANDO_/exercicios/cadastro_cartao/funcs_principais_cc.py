from exercicios.cadastro_cartao import funcs_cadastrar_cartao as fcc
from exercicios.utils import message, pause_clear, clear, msg_exceptions


def cadastrar_cartao(dados_cartao):
    '''
    Cadastra as informações gerais do cartão.
    
    :return: dados_cartao
    '''
    message("Antes de prosseguir, preste atenção aos dados inseridos!")
    pause_clear()      
                            
    #Chamando as funções de "funcs_cadastrar_cartao.py":      
    agencia = fcc.info_agencia()
    tipo_cartao = fcc.info_tipo_cartao()
    num_cartao = fcc.info_num_cartao()
    validade_cartao = fcc.info_validade_cartao()
    cvv = fcc.info_cvv()
    nome_titular = fcc.info_nome_titular()
    cpf = fcc.info_cpf()
    apelido_cartao = fcc.info_apelido_cartao(dados_cartao)
    
    #Insere as informações do cartão em um dicionário:
    dados_cartao.update({
        apelido_cartao: {'Agência': agencia, 'Tipo de cartão': tipo_cartao, 'Núm. do cartão': num_cartao,
                         'Validade do cartão': validade_cartao, 'CVV': cvv, 'Nome do titular': nome_titular,
                         'CPF': cpf}
    })
    
    message("Cartão cadastrado com sucesso!")
    pause_clear()
    return dados_cartao


def ver_dados_cartao(dados_cartao):
    '''
    Mostra as informações do cartão caso tenha algum cartão cadastrado.
    
    :return: dados_cartao
    '''
    #Verifica se existe algum cartão em "dados_cartao":
    if dados_cartao:
        while True:
            message("Informe o apelido do cartão para acessar as informações dele!")
            acesso_infos_cartao = input('Informe o apelido do cartão: ').capitalize()
            
            #verifica se o cartão existe em "dados_cartao":
            if acesso_infos_cartao not in dados_cartao:
                msg_exceptions('Cartão não cadastrado!')
                continue
            else:
                clear()
                print('--------------------------------------------------')
                #Informa as chaves e os valores do dicionário de acordo com o apelido do cartão informado:
                for chave, valor in dados_cartao[acesso_infos_cartao].items():
                    print(f'{chave}: {valor}')
                print('--------------------------------------------------')
                pause_clear()
                return dados_cartao
            
    #Caso não haja cartões cadastrados:
    else:
        msg_exceptions("Não existe cartão(ões) cadastrado(s)!")


def excluir_cartao(dados_cartao):
    '''
    Exclui um cartão cadastrado.
    
    :param dados_cartao: dicionário com as informações dos cartões
    :return: dados_cartao
    '''
    if dados_cartao:
        while True:
            selecionar_cartao = input('Informe o apelido do cartão que deseja excluir: ').capitalize()
            #Caso o cartão selecionado não exista em "dados_cartao":
            if selecionar_cartao not in dados_cartao:
                msg_exceptions('Cartão não cadastrado!')
                continue
            else:       
                confirmacao = input('Você tem certeza? (sim/nao/não) ').lower()
                match confirmacao:
                    #Exclui o cartão:
                    case 'sim':
                        del dados_cartao[selecionar_cartao]
                        clear()
                        message("Cartão excluído com sucesso")
                        pause_clear()
                        break
                    #Cancela a operação de exclusão:
                    case 'nao' | 'não':
                        msg_exceptions('Operação cancelada!')
                        break
                    #Caso a resposta seja inválida:
                    case _:
                        msg_exceptions('Comando inválido!')
                        continue
    else:
       msg_exceptions("Não existe cartão(ões) cadastrado(s)!")
        
    return dados_cartao