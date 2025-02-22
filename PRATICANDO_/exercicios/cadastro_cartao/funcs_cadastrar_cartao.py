from exercicios.utils import message, msg_exceptions, clear


def info_agencia():
    '''
    Recebe a agência do cartão e a retorna.
    
    :return: agencia
    '''
    while True:
        #Menu das agências disponíveis:
        message("MENU DE AGÊNCIAS", ['Visa', 'MasterCard', 'Hipercard', 'Alelo'])
        try:
            agencia = int(input('Agência: '))
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
                clear()
                return agencia
            #Caso a agência não esteja entre as opções:                   
            else:
                msg_exceptions('A agência sugerida é inválida!') 
                continue                
        except ValueError:
            msg_exceptions('A agência sugerida é inválida!')
            continue
        
                                    
def info_tipo_cartao():
    '''
    Recebe o tipo do cartão e o retorna.
    
    :return: tipo_cartao
    '''
    while True:
        message("MENU DE TIPOS DE CARTÕES", ['Crédito', 'Débito', 'Crédito e Débito'])
        
        #Verifica se o tipo do cartão é um número inteiro:
        try:
            tipo_cartao = int(input('Tipo de cartão: '))
            if 1 <= tipo_cartao <= 3:                   
                match tipo_cartao:
                    case 1:
                        tipo_cartao = 'Crédito'
                    case 2:
                        tipo_cartao = 'Débito'
                    case 3:
                        tipo_cartao = 'Crédito e Débito' 
                clear()
                return tipo_cartao                                                                                                                       
            else:
                msg_exceptions('O tipo de cartão sugerido é inválido!')
                continue        
        #Caso o tipo do cartão seja diferente de um número inteiro:                
        except ValueError:
            msg_exceptions('O tipo de cartão sugerido é inválido!')
            continue
        
                            
def info_num_cartao():
    '''
    Recebe o número do cartão, o formata e o retorna.
    
    :return: numero_cartao
    '''
    while True:
        try:
            message("Não é necessário colocar espaços entre os números!")
            numero_cartao = input('Número do cartão (16 dígitos): ')
            #Caso o usuário coloque espaços em branco:
            elimina_espacos = numero_cartao.replace(' ', '')
            
            #Verifica se o número do cartão só contém dígitos:
            if not elimina_espacos.isdigit():
                msg_exceptions('Só é permitido números!!')                
                continue
            else:
                #Verifica se o número do cartão tem 16 dígitos:
                if len(elimina_espacos) == 16:
                    #Formata o número do cartão colocando um "-" a cada 4 números:
                    numero_cartao = "-".join(numero_cartao[i:i+4] for i in range(0, len(numero_cartao), 4))
                    clear()
                    return numero_cartao
                else:
                    msg_exceptions('O número precisa ter 16 dígitos!')
                    continue                   
        except ValueError:
            msg_exceptions('Só é permitido números!!')                
            continue

       
def info_validade_cartao():
    '''
    Recebe a validade do cartão, a formata e a retorna.
    
    :return: validade_cartao
    '''
    while True:
        try:
            mes = int(input('Mês de validade (1-12): '))           
            ano = int(input('Ano de validade (1 ou 2 dígitos): '))
            #Formata as datas de validade do cartão:
            validade_cartao = f'{mes:02}/{ano:02}'
            clear()
            return validade_cartao                             
        except ValueError:
            msg_exceptions('Só é permitido números!')
            continue


def info_cvv():
    '''
    Recebe o cvv do cartão e o retorna.
    
    :return: cvv
    '''
    while True:
        try:
            cvv = input('CVV (3 dígitos): ')
            elimina_espacos = cvv.replace(' ', '')
            
            #Verifica se o cvv só contém números:
            if not elimina_espacos.isdigit():
                msg_exceptions('Só é permitido números!')
                continue                       
            else:
                #Verifica se o cvv tem 3 dígitos:
                if len(elimina_espacos) == 3:
                    clear()
                    return cvv 
                else:
                    msg_exceptions('É obrigatório ter 3 digítos!')
                    continue
        except ValueError:
            msg_exceptions('Só é permitido números!')
            continue  
        
        
def info_nome_titular():
    '''
    Recebe o nome do titular do cartão, o formata e o retorna.
    
    :return: nome_titular
    '''
    while True:
        #A função "split" separa os nomes do titular e os armazena em uma lista:
        nome_titular = input('Nome do titular (coloque espaço a cada nome): ').split()
        #Formata os nomes informados pelo usuário:
        nome_titular_formatado = ' '.join(nome.capitalize() for nome in nome_titular)
        #Elimina os espaços em branco (facilita a verificação):
        elimina_espacos = nome_titular_formatado.replace(' ', '')
        
        #verifica se o nome do titular só contém letras:
        if not elimina_espacos.isalpha():
            msg_exceptions('Só é permitido letras!')
            continue
        else:
            #Verifica a quantidade de nomes do titular:
            if len(nome_titular) >= 2:
                clear()
                return nome_titular_formatado
            else:
                msg_exceptions('É necessário pelo menos dois nomes!')
                continue
            
        
def info_cpf():
    '''
    Recebe o cpf do titular do cartão, o formata e o retorna.
    
    :return: cpf
    '''
    while True:
        try:
            cpf = input('CPF (11 dígitos sem pontos e traços): ')
            #Verifica se o usuário já colocou "." e '-' nos lugares corretos:
            if '.' in cpf[3] and '.' in cpf[7] and '-' in cpf[11]:
                clear()
                return cpf
            #Caso ele não tenha os colocado nos lugares corretos:
            else:
                #Elimina os pontos, traços e espaços vazios, caso o usuário os coloquem:
                elimina_carac_especiais = cpf.replace('.','').replace('-', '').replace(' ', '')
                
                if not elimina_carac_especiais.isdigit():
                    msg_exceptions('Só é permitido números!') 
                    continue
                else:    
                    if len(elimina_carac_especiais) == 11:
                        #Adiciona pontos no cpf:
                        cpf_com_pontos = '.'.join(elimina_carac_especiais[i:i+3] for i in range(0, len(elimina_carac_especiais), 3))
                        #Separa cada elemento do cpf_com_pontos e os armazena em uma lista:
                        elementos_cpf = [elemento for elemento in cpf_com_pontos]
                        #Substitue o terceiro ponto por um traço:
                        elementos_cpf[11] = '-'
                        #Junta os elementos da lista em uma string:
                        cpf = ''.join(elementos_cpf)
                        clear()
                        return cpf
                    else:
                        msg_exceptions('Cpf inválido, é necessário 11 dígitos!')
                        continue
        except ValueError:
            msg_exceptions('Só é permitido números!') 
            continue
        
        
def info_apelido_cartao(dados_cartao):
    '''
    Recebe o apelido do cartão e o retorna.
    
    :return: apelido_cartao
    '''
    while True:
        apelido_cartao = input('Apelido do cartão: ').capitalize()
        
        if apelido_cartao in dados_cartao:
            msg_exceptions('Apelido já cadastrado!')
            continue
        else:
            clear()
            return apelido_cartao