from os import system
from time import sleep


def limpar_tela():
    system('cls')


def menu():
    print('--------------------------------------------------')
    print('--------------> CADASTRO DE CARTÃO <--------------')
    print('[1] Cadastrar cartão \n[2] Ver dados do cartão '
          '\n[3] Alterar dados do cartão \n[4] Excluir cartão '
          '\n[5] Sair')
    print('--------------------------------------------------')
    print('--------------------------------------------------')


def obter_opcao():
    try:
        opcao = int(input('Informe a opção: '))
        print('--------------------------------------------------')
        if 1 <= opcao <= 5:
            return opcao
        else:
            limpar_tela()
            print('A opção sugerida é inválida!')
            
    except ValueError:
        limpar_tela()
        print('A opção sugerida é inválida!')


def menu_agencia():
    print('-------------------------')
    print('-> AGÊNCIAS DISPONÍVES <-')
    print('-------------------------')
    print('[1] Visa \n[2] MasterCard '
          '\n[3] Hipercard \n[4] Alelo')
    print('-------------------------')


def menu_tipo_cartao():
    print('-------------------------')
    print('---> TIPOS DE CARTÃO <---')
    print('-------------------------')
    print('[1] Crédito \n[2] Débito '
          '\n[3] Crédito e Débito')
    print('-------------------------')

            
def cadastrar_cartao(dados_cartao):
    print('------------------------------------------------------------')
    print('- Antes de prosseguir, preste atenção aos dados inseridos! -')
    print('------------------------------------------------------------')
    sleep(6)
    limpar_tela()
               
    #Funções:
    def definir_agencia():
            while True:
                menu_agencia()
                try:
                    global agencia
                    agencia = int(input('Agência: '))
                    print('-------------------------')
                    if 1 <= agencia <= 4:
                        match agencia:
                            case 1:
                                agencia = 'Visa'
                            case 2:
                                agencia = 'MasterCard'
                            case 3:
                                agencia = 'Hipercard'
                            case 4:
                                agencia = 'Alelo'
                        limpar_tela()
                        break                    
                    else:
                        limpar_tela()
                        print('A agência sugerida é inválida!')                   
                except ValueError:
                    limpar_tela()
                    print('A agência sugerida é inválida!')     
        
    def definir_tipo_cartao():   
            while True:
                menu_tipo_cartao()
                try:
                    global tipo_cartao
                    tipo_cartao = int(input('Tipo de cartão: '))
                    print('-------------------------')
                    if 1 <= tipo_cartao <= 3:                   
                        match tipo_cartao:
                            case 1:
                                tipo_cartao = 'Crédito'
                            case 2:
                                tipo_cartao = 'Débito'
                            case 3:
                                tipo_cartao = 'Crédito e Débito' 
                        limpar_tela()
                        break                                                                                                                         
                    else:
                        limpar_tela()
                        print('O tipo de cartão sugerido é inválido!')
                                
                except ValueError:
                    limpar_tela()
                    print('O tipo de cartão sugerido é inválido!')
        
    def definir_num_cartao():
            while True:
                try:
                    global numero_cartao
                    print('COLOQUE ESPAÇOS A CADA 4 DÍGITOS!')
                    print('--------------------------------------------------')
                    numero_cartao = input('Número do cartão (16 dígitos): ')
                    elimina_espacos = numero_cartao.replace(' ', '')
                    
                    if elimina_espacos.isdigit() == False:
                        limpar_tela()
                        print('Só é permitido números!!')
                        print('--------------------------------------------------')                       
                    else:
                        if len(elimina_espacos) == 16:
                            limpar_tela()
                            break
                        else:
                            limpar_tela()
                            print('O número precisa ter 16 dígitos!')
                            print('--------------------------------------------------')
                            
                except ValueError:
                    limpar_tela()
                    print('Só é permitido números!')
                    print('--------------------------------------------------')
        
    def definir_validade_cartao():
            while True:
                try:
                    global validade_cartao
                    mes = int(input('Mês de validade (1-12): '))           
                    ano = int(input('Ano de validade (1 ou 2 dígitos): '))
                    validade_cartao = f'{mes:02}/{ano:02}'           
                except ValueError:
                    limpar_tela()
                    print('Só é permitido números!')
                    print('--------------------------------------------------')           
                limpar_tela()
                break
        
    def definir_cvv():
            while True:
                try:
                    global cvv
                    cvv = input('CVV (3 dígitos): ')
                    if cvv.isdigit() == False:
                        limpar_tela()
                        print('Só é permitido números!')
                        print('--------------------------------------------------')                        
                    else:
                        if len(cvv) == 3:
                            limpar_tela()
                            break
                        else:
                            limpar_tela()
                            print('É obrigatório ter 3 digítos!')
                            print('--------------------------------------------------')
                except ValueError:
                    limpar_tela()
                    print('Só é permitido números!')
                    print('--------------------------------------------------')  
        
    def definir_nome_titular():
            while True:
                global nome_titular_formatado
                nome_titular = input('Nome do titular: ').split()
                nome_titular_formatado = ' '.join(nome_titular.capitalize() for nome_titular in nome_titular)
                elimina_espacos = nome_titular_formatado.replace(' ', '')
                
                if elimina_espacos.isalpha() == False:
                    limpar_tela()
                    print('Só é permitido letras!')
                    print('--------------------------------------------------')
                else:
                    if len(nome_titular) >= 3:
                        limpar_tela()
                        break
                    else:
                        limpar_tela()
                        print('É necessário, pelo menos, três nomes!')
                        print('--------------------------------------------------')
        
    def definir_cpf():
            while True:
                try:
                    global cpf
                    cpf = input('CPF (11 dígitos, com ponto e traço): ')
                    elimina_carac_especiais = cpf.replace('.','').replace('-', '')
                    
                    if elimina_carac_especiais.isdigit() == False:
                        limpar_tela()
                        print('Só é permitido números!') 
                        print('--------------------------------------------------')
                    else:    
                        if len(elimina_carac_especiais) == 11:
                            limpar_tela()
                            break
                        else:
                            limpar_tela()
                            print('Cpf inválido, é necessário 11 dígitos!')
                            print('--------------------------------------------------')
                except ValueError:
                    limpar_tela()
                    print('Só é permitido números!')
                    print('--------------------------------------------------')          
        
    def definir_apelido_cartao():
            global apelido_cartao
            apelido_cartao = input('Apelido do cartão: ').capitalize()                        
        
    #Chamando as funções:       
    definir_agencia()
    definir_tipo_cartao()
    definir_num_cartao()
    definir_validade_cartao()
    definir_cvv()
    definir_nome_titular()
    definir_cpf()
    definir_apelido_cartao()    
        
    #Retorna a mensagem de cadastro realizado e insere as informações:      
    limpar_tela()
    print('Cartão cadastrado com sucesso!')
    return {'agencia': agencia, 'tipo_cartao': tipo_cartao,
            'numero_cartao': numero_cartao, 'validade_cartao': validade_cartao,
            'cvv': cvv, 'nome_titular': nome_titular_formatado,
            'cpf': cpf, 'apelido_cartao': apelido_cartao}


def ver_dados_cartao(dados_cartao):
    if dados_cartao:
        limpar_tela()
        print('--------------------------------------------------')
        print('Agencia: ', dados_cartao['agencia'])
        print('Tipo de cartão: ', dados_cartao['tipo_cartao'])
        print('Número do cartão: ', dados_cartao['numero_cartao'])
        print('Validade do cartão: ', dados_cartao['validade_cartao'])
        print('CVV: ', dados_cartao['cvv'])
        print('Nome do titular: ', dados_cartao['nome_titular'])
        print('CPF: ', dados_cartao['cpf'])
        print('Apelido do cartão: ', dados_cartao['apelido_cartao'])
        print('--------------------------------------------------')
        input('Pressione ENTER para retornar ao menu...')
        limpar_tela()
        print('Visualização encerrada!')
    else:
        limpar_tela()
        print('Você não possui um cartão cadastrado!')
    return dados_cartao


def excluir_cartao(dados_cartao):
    if dados_cartao:
        confirmacao = input('Você tem certeza? (sim/nao/não) ').lower()
        match confirmacao:
            case 'sim':
                dados_cartao.clear()
                limpar_tela()
                print('Cartão excluído com sucesso!')
            case 'nao' | 'não':
                limpar_tela()
                print('Operação encerrada, exclusão cancelada!')
            case _:
                limpar_tela()
                print('Não entendi, tente novamente!')
    else:
        limpar_tela()
        print('Você não possui um cartão cadastrado!')
    return dados_cartao


def alterar_dados_cartão(dados_cartao):
    if dados_cartao:
        limpar_tela()
        print('---------------------------------------------------------')
        print('------- Você só pode alterar o apelido do cartão! -------')
        print('---------------------------------------------------------')
        
        while True:
            alternativa = input('Você deseja alterar o apelido do cartão? (sim/nao) ').lower()
            match alternativa:
                case 'sim':
                    limpar_tela()
                    alterar_apelido_cartao = input('Informe o novo apelido: ').capitalize()   
                                                               
                    if alterar_apelido_cartao == dados_cartao['apelido_cartao']:
                        limpar_tela()
                        print('O novo apelido não pode ser igual ao antigo!')
                        print('---------------------------------------------------------')                       
                    else:
                        limpar_tela()
                        dados_cartao['apelido_cartao'] = alterar_apelido_cartao
                        print('Apelido alterado com sucesso!')                       
                        break                                   
                case 'nao' | 'não':
                    limpar_tela()
                    print('Operação encerrada, alteração cancelada!')
                    break
                case _:
                    limpar_tela()
                    print('Não entendi, tente novamente!')
                    print('--------------------------------------------------')
    else:
        limpar_tela()
        print('Você não possui um cartão cadastrado!')
    return dados_cartao
  
                                
dados_cartao = {}

while True:
    menu()
    opcao = obter_opcao()
    
    match opcao:
        case 1:
            limpar_tela()          
            result = cadastrar_cartao(dados_cartao)
            if result is not None:
                dados_cartao = result
        case 2:
            dados_cartao = ver_dados_cartao(dados_cartao)
        case 3:
            dados_cartao = alterar_dados_cartão(dados_cartao)
        case 4:
            dados_cartao = excluir_cartao(dados_cartao)
        case 5:
            for contagem in range(5, 0, -1):
                print(f'Encerrando em {contagem}...')
                sleep(1)
            break