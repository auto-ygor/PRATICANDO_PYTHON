from exercicios.utils import message, msg_exceptions, clear, pause_clear


def tamanho_senha():
    '''
    Recebe o tamanho da senha informada pelo usuário.
    
    :return: tamanho da senha
    '''
    while True:
        try:
            tam = int(input("Digite o tamanho da senha: "))
            
            #Verifica se o tamanho da senha está entre 4 e 8 dígitos:
            if tam < 4 or tam > 8:
                msg_exceptions("A senha deve ter no mínimo 4 dígitos e no máximo 8 dígitos.")
                continue
            else:
                clear()
                return tam
        
        #Caso o usuário digite algo diferente de um número:    
        except ValueError:
            msg_exceptions("Digite algo válido.")
            continue        
    
              
def jogo_da_senha():
    '''
    Função principal do jogo da senha.
    
    :return: não tem retorno
    '''
    from random import randint   
    #Recebe o tamanho da senha:
    tamanho = tamanho_senha()
    
    #Cria duas listas vazias:
    senha = list()
    senha_criptografada = list()
    
    #Adiciona números aleatórios na lista "senha" e '*' na lista "senha_criptografada":
    for i in range(tamanho):
        senha.append(randint(0, 9))
        senha_criptografada.append('*')
       
    contador = 0
    quant_tentativas = 5
    
    while contador != tamanho:
        print(f"A senha é: {' | '.join(senha_criptografada)}")
        message(f"Você tem {quant_tentativas} tentativas.")
               
        #Se o número de tentativas for igual a 0, o jogo é finalizado e a senha é exibida.       
        if quant_tentativas == 0:
            clear()
            message("Você perdeu todas as tentativas.")
            print(f"A senha era: {' | '.join(map(str, senha))}")
            break
        
        try:
            tentativa_user = int(input(f"Adivinhe o {contador + 1}º dígito da senha: "))     
            if tentativa_user < 0 or tentativa_user > 9:
                message("Digite um número entre 0 e 9.")
                pause_clear()
                continue           
            else:               
                #Se o número digitado for igual ao número da senha, o '*' é substituído pelo número
                #e o contador é incrementado. A variável "quant_tentativas" é reiniciada para 5.                              
                if tentativa_user == senha[contador]:
                    senha_criptografada[contador] = str(tentativa_user)
                    contador+= 1
                    quant_tentativas = 5
                    message("Você acertou o dígito!")
                    pause_clear()                    
                #Se o número digitado for diferente do número da senha:
                elif tentativa_user > senha[contador]:
                    quant_tentativas -= 1        
                    message("O número é menor.")
                    pause_clear()
                else:
                    quant_tentativas -= 1
                    message("O número é maior.")
                    pause_clear()
                                              
        except ValueError:
            msg_exceptions("Digite algo válido.")
            continue
        
    #Quando o contador se igualar ao tamanho da senha, o jogo é finalizado e a mensagem
    #de conclusão é exibida. Esta mensagem só será exibida se o usuário acertar a senha.    
    if contador == tamanho:       
        clear()
        message("Parabéns, Você acertou a senha!!")
        print(f"A senha era: {' | '.join(map(str, senha))}")