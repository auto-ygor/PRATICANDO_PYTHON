from random import randint
from os import system, name
from time import sleep


def pausar():
    sleep(2)


def menu():
    print("----------------- ADIVINHE A SENHA -------------------")
    print("Obs: O tamanho da senha deve ser de 4 a 8 dígitos.")
    print("------------------------------------------------------")
    print("Forma de jogar: Tente adivinhar o primeiro dígito.\n"
          "Se acertar, tente o segundo e assim por diante.")
    print("------------------------------------------------------")
    input("Pressione ENTER para continuar...")
    limpar_tela()


def limpar_tela():
    '''
    Executa a função de limpar a tela do terminal
    de acordo com o sistema operacional do usuário.
    '''
    if name == 'nt': #Windows
        system('cls')
    else: #Linux, MacOS, etc
        system('clear')
    

def tamanho_senha(tam):
    while True:
        try:
            tam = int(input("Digite o tamanho da senha: "))
            
            #Verifica se o tamanho da senha está entre 4 e 8 dígitos:
            if tam < 4 or tam > 8:
                limpar_tela()
                print("A senha deve ter no mínimo 4 dígitos\n"
                      "e no máximo 8 dígitos.")
                pausar()
                limpar_tela()
                continue
            else:
                limpar_tela()
                break
        
        #Caso o usuário digite algo diferente de um número:    
        except ValueError:
            limpar_tela()
            print("Digite algo válido.")
            pausar()
            limpar_tela()
            continue
    return tam            
    
              
def jogo_da_senha():
    menu()
    tamanho = tamanho_senha(0)
    
    #Cria duas listas vazias:
    senha = []
    senha_criptografada = []
    
    #Adiciona números aleatórios na lista "senha" e '*' na lista "senha_criptografada":
    for i in range(tamanho):
        senha.append(randint(0, 9))
        senha_criptografada.append('*')
       
    contador = 0
    quant_tentativas = 5
    
    while contador != tamanho:
        print(f"A senha é: {' | '.join(senha_criptografada)}")
        print("-----------------------------------------------------------")
        print(f"Você tem {quant_tentativas} tentativas.")
        print("-----------------------------------------------------------")
        
        '''
        Se o número de tentativas for igual a 0, o jogo é finalizado e a senha é exibida.
        '''
        if quant_tentativas == 0:
            limpar_tela()
            print("Você perdeu todas as tentativas.")
            print(f"A senha era: {' | '.join(map(str, senha))}")
            break
        
        try:
            tentativa_user = int(input(f"Adivinhe o {contador + 1}º dígito da senha: "))
            print("-----------------------------------------------------------")           
            if tentativa_user < 0 or tentativa_user > 9:
                print("Digite um número entre 0 e 9.")
                pausar()
                limpar_tela()
                continue           
            else:
                '''
                Se o número digitado for igual ao número da senha, o '*' é substituído pelo número
                e o contador é incrementado. A variável "quant_tentativas" é reiniciada para 5.
                '''                
                if tentativa_user == senha[contador]:
                    senha_criptografada[contador] = str(tentativa_user)
                    contador+= 1
                    quant_tentativas = 5
                    print("Você acertou o dígito!")
                    pausar()
                    limpar_tela()
                #Se o número digitado for diferente do número da senha:
                elif tentativa_user > senha[contador]:
                    quant_tentativas -= 1        
                    print("O número é menor.")
                    pausar()
                    limpar_tela()
                else:
                    quant_tentativas -= 1
                    print("O número é maior.")
                    pausar()
                    limpar_tela()
                             
        except ValueError:
            limpar_tela()
            print("Digite algo válido.")
            pausar()
            limpar_tela()
            continue
    
    '''
    Quando o contador se igualar ao tamanho da senha, o jogo é finalizado e a mensagem
    de conclusão é exibida. Esta mensagem só será exibida se o usuário acertar a senha.
    '''
    if contador == tamanho:       
        limpar_tela()
        print("Parabéns, Você acertou a senha!!")
        print(f"A senha era: {' | '.join(map(str, senha))}")

#Inicializa o jogo:      
jogo_da_senha()