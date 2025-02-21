from os import system, name
from time import sleep


def clear():
    '''
    Executa a função de limpar a tela do terminal
    de acordo com o sistema operacional do usuário.
    Se o sistema for Windows, executa a função contida
    no if. Caso contrário, executa a função contida
    no else.
    '''
    if name == 'nt': 
        system('cls')
    else:
        system('clear')
        

def message(msg, options=[], symbol='='):
    '''
    Mostra uma mensagem formantando-a com símbolos.
    Caso o usuário insira opções, elas serão mostradas
    no final da mensagem. Também é possível informar o
    símbolo.
    
    :param msg: Recebe a mensagem (obrigatória)
    :param options: Recebe as opções (opcional)
    :param symbol: Recebe o símbolo (opcional)
    :return: Não retorna nada
    '''
    
    # Captura o tamanho da mensagem e adiciona 10:
    size_msg = len(msg) + 8
    # Printa a mensagem formatada conforme o tamanho dela:
    print(f"{symbol}" * size_msg)
    print(f"{msg}")
    print(f"{symbol}" * size_msg)

    # Caso opções sejam informadas:
    if len(options) > 0:
        # Printa os elementos que estão em options:
        for i in range(0, len(options)):
            print(f"[{i+1}] {options[i].capitalize()}")
        print(f"{symbol}" * size_msg)


def pause():
    '''
    Pausa a execução do programa até que o usuário
    pressione qualquer tecla.
    '''
    system("pause")   


def pause_clear():
    '''
    Junta as funções pause() e clear().
    '''
    pause()
    clear()


def option(quant_options):
    '''
    Retorna a opção escolhida pelo usuário de acordo
    com a quantidade de opções informadas.
    
    :param quant_options: Recebe a quantidade de opções (obrigatória)
    :return: Retorna a opção escolhida pelo usuário
    '''
    
    #Inicializa um loop infinito:
    while True:
        #Checa se a variável "opcao" é um número inteiro:
        try:
            opcao = int(input('Informe a opção: '))
            #Se a opção estiver no intervalo de opções informadas, ela é retornada:
            if 1 <= opcao <= quant_options:
                return opcao
            #Caso a opção seja inválida (continua o loop):
            else:
                clear()
                message("Opção inválida!")
                pause_clear() 
                continue
        #Caso a variável "opcao" não seja um número inteiro (continua o loop):                       
        except ValueError:
            clear()
            message("Opção inválida!")
            pause_clear()
            continue


def close_program(msg="Até logo!"):
    '''
    Fecha o programa com uma contagem regressiva.
    
    :param msg: Recebe a mensagem (opcional)
    :return: Não retorna nada
    '''
    for i in range(5, 0, -1):
        print(f"Encerrando em {i}...")
        sleep(1)
        clear()
    print(msg)


def msg_exceptions(msg="Opção invalida!"):
    '''
    Exibe uma mensagem caso ocorra uma exceção.
    
    :param msg: Recebe a mensagem (opcional)
    :return: Não retorna nada
    '''
    clear()
    message(msg)
    pause_clear()
