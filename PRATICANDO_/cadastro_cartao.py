from os import system, name
from time import sleep


def limpar_tela():
    '''
    Executa a função de limpar a tela do terminal
    de acordo com o sistema operacional do usuário.
    '''
    if name == 'nt': #Windows
        system('cls')
    else: #Linux, MacOS, etc
        system('clear')


def espera_comando_user():
    input('Pressione ENTER para continuar...')


def cartao_nao_encontrado():
    limpar_tela()
    print('Cartão não encontrado!')
    espera_comando_user()
    limpar_tela()
    

def dados_cartao_vazia():
    limpar_tela()
    print('Você não possui um cartão cadastrado!')
    espera_comando_user()
    limpar_tela()
    
    
def menu_principal():
    print('--------------------------------------------------')
    print('--------------> CADASTRO DE CARTÃO <--------------')
    print('[1] Cadastrar cartão \n[2] Ver dados do cartão \n'
          '[3] Excluir cartão \n[4] Sair')
    print('--------------------------------------------------')
    print('--------------------------------------------------')


def menu_dados_cartao():
    print("----------------------------------------------------------------")
    print("- Para acessar os dados do cartão, informe o apelido do mesmo! -")
    print("----------------------------------------------------------------")
    
    
def obter_opcao():
    try:
        opcao = int(input('Informe a opção: '))
        print('--------------------------------------------------')
        if 1 <= opcao <= 4:
            return opcao
        else:
            limpar_tela()
            print('A opção sugerida é inválida!')
            espera_comando_user()
            limpar_tela()
            
    except ValueError:
        limpar_tela()
        print('A opção sugerida é inválida!')
        espera_comando_user()
        limpar_tela()


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
    espera_comando_user()
    limpar_tela()                
    
    #Funções:
    def definir_agencia():
        while True:
            #Menu das agências disponíveis:
            menu_agencia()
            try:
                agencia = int(input('Agência: '))
                print('-------------------------')
                #Verifica se a agência informada existe:
                if 1 <= agencia <= 4:
                    #Atribui a agência de acordo com a opção informada:
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
                    return agencia
                #Caso a agência não esteja entre as opções:                   
                else:
                    limpar_tela()
                    print('A agência sugerida é inválida!') 
                    espera_comando_user()
                    limpar_tela()
                    continue
                    
            except ValueError:
                limpar_tela()
                print('A agência sugerida é inválida!')
                espera_comando_user()
                limpar_tela()
                                           
    def definir_tipo_cartao():
        while True:
            menu_tipo_cartao()
            
            #Verifica se o tipo do cartão é um número inteiro:
            try:
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
                    return tipo_cartao                                                                                                                       
                else:
                    limpar_tela()
                    print('O tipo de cartão sugerido é inválido!')
                    espera_comando_user()
                    limpar_tela()
                    continue
            
            #Caso o tipo do cartão seja diferente de um número inteiro:                
            except ValueError:
                limpar_tela()
                print('O tipo de cartão sugerido é inválido!')
                espera_comando_user()
                limpar_tela()
                                 
    def definir_num_cartao():
        while True:
            try:
                print('COLOQUE ESPAÇOS A CADA 4 DÍGITOS!')
                print('--------------------------------------------------')
                numero_cartao = input('Número do cartão (16 dígitos): ')
                #Elimina os espaços em branco (facilita a contagem dos dígitos):
                elimina_espacos = numero_cartao.replace(' ', '')
                
                #Verifica se o número do cartão só contém dígitos:
                if not elimina_espacos.isdigit():
                    limpar_tela()
                    print('Só é permitido números!!')
                    print('--------------------------------------------------')
                    espera_comando_user()
                    limpar_tela()
                    continue
                else:
                    #Verifica se o número do cartão tem 16 dígitos:
                    if len(elimina_espacos) == 16:
                        limpar_tela()
                        return numero_cartao
                    else:
                        limpar_tela()
                        print('O número precisa ter 16 dígitos!')
                        print('--------------------------------------------------')
                        espera_comando_user()
                        limpar_tela()
                        continue
                        
            except ValueError:
                limpar_tela()
                print('Só é permitido números!')
                print('--------------------------------------------------')
                espera_comando_user()
                limpar_tela()
            
    def definir_validade_cartao():
        while True:
            try:
                mes = int(input('Mês de validade (1-12): '))           
                ano = int(input('Ano de validade (1 ou 2 dígitos): '))
                #Formata as datas de validade do cartão:
                validade_cartao = f'{mes:02}/{ano:02}'
                limpar_tela()
                return validade_cartao                             
            except ValueError:
                limpar_tela()
                print('Só é permitido números!')
                print('--------------------------------------------------')
                espera_comando_user()
                continue

    def definir_cvv():
        while True:
            try:
                cvv = input('CVV (3 dígitos): ')
                #Verifica se o cvv só contém números:
                if not cvv.isdigit():
                    limpar_tela()
                    print('Só é permitido números!')
                    print('--------------------------------------------------')
                    espera_comando_user()
                    limpar_tela()
                    continue                       
                else:
                    #Verifica se o cvv tem 3 dígitos:
                    if len(cvv) == 3:
                        limpar_tela()
                        return cvv 
                    else:
                        limpar_tela()
                        print('É obrigatório ter 3 digítos!')
                        print('--------------------------------------------------')
                        espera_comando_user()
                        limpar_tela()
                        continue

            except ValueError:
                limpar_tela()
                print('Só é permitido números!')
                print('--------------------------------------------------')
                espera_comando_user()
                limpar_tela()  

    def definir_nome_titular():
        while True:
            #A função "split" separa os nomes do titular e os armazena em uma lista:
            nome_titular = input('Nome do titular: ').split()
            #Formata os nomes informados pelo usuário:
            nome_titular_formatado = ' '.join(nome_titular.capitalize() for nome_titular in nome_titular)
            #Elimina os espaços em branco (facilita a verificação):
            elimina_espacos = nome_titular_formatado.replace(' ', '')
            
            #verifica se o nome do titular só contém letras:
            if not elimina_espacos.isalpha():
                limpar_tela()
                print('Só é permitido letras!')
                print('--------------------------------------------------')
                espera_comando_user()
                limpar_tela()
                continue
            else:
                #Verifica a quantidade de nomes do titular:
                if len(nome_titular) >= 2:
                    limpar_tela()
                    return nome_titular_formatado
                else:
                    limpar_tela()
                    print('É necessário pelo menos dois nomes!')
                    print('--------------------------------------------------')
                    espera_comando_user()
                    limpar_tela()
                    continue
            
    def definir_cpf():
        while True:
            try:
                cpf = input('CPF (11 dígitos, com ponto e traço): ')
                #Elimina os pontos e traços do cpf (facilita a verificação):
                elimina_carac_especiais = cpf.replace('.','').replace('-', '')
                
                if not elimina_carac_especiais.isdigit():
                    limpar_tela()
                    print('Só é permitido números!') 
                    print('--------------------------------------------------')
                    espera_comando_user()
                    limpar_tela()
                    continue
                else:    
                    if len(elimina_carac_especiais) == 11:
                        limpar_tela()
                        return cpf
                    else:
                        limpar_tela()
                        print('Cpf inválido, é necessário 11 dígitos!')
                        print('--------------------------------------------------')
                        espera_comando_user()
                        limpar_tela()
                        continue

            except ValueError:
                limpar_tela()
                print('Só é permitido números!')
                print('--------------------------------------------------')
                espera_comando_user()
                limpar_tela()

    def definir_apelido_cartao(dados_cartao):
        while True:
            apelido_cartao = input('Apelido do cartão: ').capitalize()
            
            if apelido_cartao in dados_cartao:
                limpar_tela()
                print('Apelido já cadastrado!')
                espera_comando_user()
                limpar_tela()
                continue
            else:
                limpar_tela()
                return apelido_cartao
                      
    #Chamando as funções:       
    agencia = definir_agencia()
    tipo_cartao = definir_tipo_cartao()
    num_cartao = definir_num_cartao()
    validade_cartao = definir_validade_cartao()
    cvv = definir_cvv()
    nome_titular = definir_nome_titular()
    cpf = definir_cpf()
    apelido_cartao = definir_apelido_cartao(dados_cartao)
    
    #Insere as informações do cartão em um dicionário:
    dados_cartao.update({
        apelido_cartao: {'agencia': agencia, 'tipo_cartao': tipo_cartao, 'numero_cartao': num_cartao,
                         'validade_cartao': validade_cartao, 'cvv': cvv, 'nome_titular': nome_titular,
                         'cpf': cpf}
    })
    
    print('Cartão cadastrado com sucesso!')
    espera_comando_user()
    limpar_tela()
    return dados_cartao


def ver_dados_cartao(dados_cartao):
    #Verifica se existe algum cartão em "dados_cartao":
    if dados_cartao:
        while True:
            menu_dados_cartao()
            acesso_infos_cartao = input('Informe o apelido do cartão: ').capitalize()
            
            #verifica se o cartão existe em "dados_cartao":
            if acesso_infos_cartao not in dados_cartao:
                cartao_nao_encontrado()
                continue
            else:
                #Exibe as informações do cartão informado pelo usuário:
                limpar_tela()
                print('--------------------------------------------------')
                print(f'Agencia: {dados_cartao[acesso_infos_cartao]['agencia']}\n'
                    f'Tipo de cartão: {dados_cartao[acesso_infos_cartao]['tipo_cartao']}\n'
                    f'Número do cartão: {dados_cartao[acesso_infos_cartao]['numero_cartao']}\n'
                    f'Validade do cartão: {dados_cartao[acesso_infos_cartao]['validade_cartao']}\n'
                    f'CVV: {dados_cartao[acesso_infos_cartao]['cvv']}\n'
                    f'Nome do titular: {dados_cartao[acesso_infos_cartao]['nome_titular']}\n'
                    f'CPF: {dados_cartao[acesso_infos_cartao]['cpf']}\n'
                    f'Apelido do cartão: {acesso_infos_cartao}')
                print('--------------------------------------------------')
                espera_comando_user()
                limpar_tela()
                return dados_cartao
            
    #Caso não haja cartões cadastrados:
    else:
        dados_cartao_vazia()


def excluir_cartao(dados_cartao):
    if dados_cartao:
        while True:
            selecionar_cartao = input('Informe o apelido do cartão que deseja excluir: ').capitalize()
            #Caso o cartão selecionado não exista em "dados_cartao":
            if selecionar_cartao not in dados_cartao:
                cartao_nao_encontrado()
                continue
            else:       
                confirmacao = input('Você tem certeza? (sim/nao/não) ').lower()
                match confirmacao:
                    #Exclui o cartão:
                    case 'sim':
                        del dados_cartao[selecionar_cartao]
                        limpar_tela()
                        print('Cartão excluído com sucesso!')
                        espera_comando_user()
                        limpar_tela()
                        break
                    #Cancela a operação de exclusão:
                    case 'nao' | 'não':
                        limpar_tela()
                        print('Operação encerrada, exclusão cancelada!')
                        espera_comando_user()
                        limpar_tela()
                        break
                    #Caso a resposta seja inválida:
                    case _:
                        limpar_tela()
                        print('Comando inválido!')
                        espera_comando_user()
                        limpar_tela()
                        continue
    else:
        dados_cartao_vazia()
        
    return dados_cartao


def fechar_programa():
    for contagem in range(5, 0, -1):
        print(f'Encerrando em {contagem}...')
        sleep(1)
    limpar_tela()
    print('Até logo!')

                            
dados_cartao = {}

while True:
    menu_principal()
    opcao = obter_opcao()
    limpar_tela()
    
    match opcao:
        case 1:
            dados_cartao = cadastrar_cartao(dados_cartao) 
        case 2:
            dados_cartao = ver_dados_cartao(dados_cartao)
        case 3:
            dados_cartao = excluir_cartao(dados_cartao)
        case 4:
            fechar_programa()
            break