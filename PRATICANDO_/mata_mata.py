from os import system, name
from random import randint, sample


def clear():
    if name == 'nt': #Windows
        system('cls')
    else: #Linux, MacOS, etc. 
        system('clear')


def pressione_enter():
    input("Pressione ENTER para continuar...")
    
    
def mata_mata():
    # Lista de times: 16 times
    oitavas = [
        'Flamengo', 'Vasco', 'Botafogo', 'Fluminense', 'São Paulo', 'Palmeiras', 'Corinthians', 'Santos',
        'Internacional', 'Grêmio', 'Cuiabá', 'Cruzeiro', 'Bahia', 'Vitória', 'Sport', 'Mirassol'
    ]
    
    quartas = []
    semifinais = []
    final_torneio = []
    campeao = []
    
    #Função que representa o palpite do usuário:
    def palpite_user():
        print("Cheque a função 'mata_mata' para ver a lista de times disponíveis.")
        pressione_enter()
        clear()
            
        while True:            
            #Palpite do usuário:
            palpite = input("Digite o seu palpite para o campeão do torneio: ").capitalize()
            
            #Verifica se o palpite está na lista de times:
            if palpite not in oitavas:
                clear()
                print("Time inválido. Digite um time que esteja na lista.")
                pressione_enter()
                clear()
                continue
            else:
                clear()
                print("Boa sorte! O torneio vai começar...")
                pressione_enter()
                clear()
                return palpite
               
    #Funções que representam as fases do mata-mata:
    def oitavas_final(oitavas, quartas):
        '''
            Oitavas de final (8 jogos). O loop while é executado até que a lista de oitavas
            fique vazia. A cada iteração, dois times são sorteados para jogar. O placar é
            sorteado e exibido na tela.
        '''
        print("============== OITAVAS ==============")
        while len(oitavas) > 1:
            #Sorteia dois times e, logo em seguida, o placar:
            time1, time2 = sample(oitavas, 2)
            placar_time1, placar_time2 = randint(0, 7), randint(0, 7)
            #Exibe o resultado:      
            print(f"{time1} {placar_time1} x {placar_time2} {time2}")
            
            #Caso seja empate:
            if placar_time1 == placar_time2:
                #Verifica a posição dos times na lista:
                posicao_time1, posicao_time2 = oitavas.index(time1), oitavas.index(time2)
                #Sorteia um dos times para passar de fase:
                time_nao_passa = sample([time1, time2], 1)
                
                #Remove o time que não passou:
                if time_nao_passa[0] == time1:
                    oitavas.pop(posicao_time1)
                    '''
                    Adiciona o time que passou na lista "quartas" e o remove
                    da lista "oitavas":
                    '''
                    quartas.append(time2)
                    oitavas.remove(time2)
                else:
                    oitavas.pop(posicao_time2)
                    quartas.append(time1)
                    oitavas.remove(time1)
                print("O time que não passou foi:", time_nao_passa[0])
            
            #Caso não seja empate (segue a mesma lógica do bloco anterior):       
            if placar_time1 > placar_time2:
                oitavas.remove(time2)            
                quartas.append(time1)
                oitavas.remove(time1)
            elif placar_time2 > placar_time1:
                oitavas.remove(time1)
                quartas.append(time2)
                oitavas.remove(time2)
            print("--------------------------------------")
        
        pressione_enter()
        clear()            
        return quartas
    
    def quartas_final(quartas, semifinais):
        '''
            Quartas de final (4 jogos). A lógica é a mesma das oitavas de final.
        '''
        print("============== QUARTAS ==============")
        while len(quartas) > 1:
            time1, time2 = sample(quartas, 2)
            placar_time1, placar_time2 = randint(0, 7), randint(0, 7)
            print(f"{time1} {placar_time1} x {placar_time2} {time2}")
            
            if placar_time1 == placar_time2:
                posicao_time1, posicao_time2 = quartas.index(time1), quartas.index(time2)
                time_nao_passa = sample([time1, time2], 1)
                
                if time_nao_passa[0] == time1:
                    quartas.pop(posicao_time1)
                    semifinais.append(time2)
                    quartas.remove(time2)
                else:
                    quartas.pop(posicao_time2)
                    semifinais.append(time1)
                    quartas.remove(time1)
                print("O time que não passou foi:", time_nao_passa[0])
            
            if placar_time1 > placar_time2:
                quartas.remove(time2)            
                semifinais.append(time1)
                quartas.remove(time1)
            elif placar_time2 > placar_time1:
                quartas.remove(time1)
                semifinais.append(time2)
                quartas.remove(time2)
            print("--------------------------------------")
        pressione_enter()
        clear()    
        return semifinais   

    def semi_final(semifinais, final):
        '''
            Semifinais (2 jogos). A lógica é a mesma das oitavas e quartas de final.
        '''
        print("============== SEMIFINAIS ==============")
        while len(semifinais) > 1:
            time1, time2 = sample(semifinais, 2)
            placar_time1, placar_time2 = randint(0, 7), randint(0, 7)
            print(f"{time1} {placar_time1} x {placar_time2} {time2}")
            
            if placar_time1 == placar_time2:
                posicao_time1, posicao_time2 = semifinais.index(time1), semifinais.index(time2)
                time_nao_passa = sample([time1, time2], 1)
                
                if time_nao_passa[0] == time1:
                    semifinais.pop(posicao_time1)
                    final.append(time2)
                    semifinais.remove(time2)
                else:
                    semifinais.pop(posicao_time2)
                    final.append(time1)
                    semifinais.remove(time1)
                print("O time que não passou foi:", time_nao_passa[0])
            
            if placar_time1 > placar_time2:
                semifinais.remove(time2)
                final.append(time1)
                semifinais.remove(time1)           
            elif placar_time2 > placar_time1:
                semifinais.remove(time1)
                final.append(time2)
                semifinais.remove(time2)
            print("--------------------------------------")
        
        pressione_enter()
        clear()
        return final
    
    def campeao_final(final, campeao):
        '''
            Final (1 jogo). A lógica é a mesma das oitavas, quartas e semifinais.
        '''
        print("============== FINAL ==============")
        while len(final) > 1:
            time1, time2 = sample(final, 2)
            placar_time1, placar_time2 = randint(0, 7), randint(0, 7)
            print(f"{time1} {placar_time1} x {placar_time2} {time2}")
            
            if placar_time1 == placar_time2:
                posicao_time1, posicao_time2 = final.index(time1), final.index(time2)
                time_nao_passa = sample([time1, time2], 1)
                
                if time_nao_passa[0] == time1:
                    final.pop(posicao_time1)
                    campeao.append(time2)
                    final.remove(time2)
                else:
                    final.pop(posicao_time2)
                    campeao.append(time1)
                    final.remove(time1)
                print("O time que não passou foi:", time_nao_passa[0])
            
            if placar_time1 > placar_time2:
                final.remove(time2)
                campeao.append(time1)
                final.remove(time1)           
            elif placar_time2 > placar_time1:
                final.remove(time1)
                campeao.append(time2)
                final.remove(time2)
            print("--------------------------------------")
        
        pressione_enter()
        clear()
        return campeao
               
    #Execução das funções:
    palpite = palpite_user()
    quartas = oitavas_final(oitavas, quartas)
    semifinais = quartas_final(quartas, semifinais)
    final_torneio = semi_final(semifinais, final_torneio)
    campeao = campeao_final(final_torneio, campeao)
    
    #Exibição do campeão:
    print("================= CAMPEÃO =================")
    print(f"O campeão do torneio foi: {campeao[0]}")
    print("===========================================")
    
    #Exibição do palpite do usuário:
    print(f"Seu palpite foi: {palpite}")
    if palpite == campeao[0]:
        print("Parabéns, você acertou seu palpite!")
    else:
        print("Que pena, você errou seu palpite!")

#Chamada da função principal:    
mata_mata()