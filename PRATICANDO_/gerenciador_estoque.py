from os import name, system
from time import sleep


def limpar_tela():
    '''
    Executa a função de limpar a tela do terminal
    de acordo com o sistema operacional do usuário.
    '''
    if name == "nt":  #Windows
        system("cls")
    else:  #Linux, macOS, etc.
        system("clear")


def erro_estoque_vazio():
    '''
    Exibe uma mensagem de erro caso o estoque esteja vazio.
    '''
    print("ERRO: Estoque vazio.")
    pausar()
    limpar_tela()
    

def menu():
    print("MENU:")
    print("------------------------------------------------------")
    print("[1] Adicionar produto")
    print("[2] Remover produto")
    print("[3] Listar produtos")
    print("[4] Consultar produto")
    print("[5] Sair")
    print("------------------------------------------------------")


def pausar():
    '''
    Pausa a execução do programa até que o usuário pressione
    a tecla Enter.
    '''
    input("Pressione Enter para continuar...")


def obter_opcao():
    while True:
        try:
            menu()
            opcao = int(input("Digite a opção desejada: "))
            #Verifica se a opção digitada é válida:
            if opcao < 1 or opcao > 5:
                #Caso a opção digitada não seja válida, levanta um erro:
                raise ValueError("Digite uma opção válida.")
            else:
                break
        #Caso um erro ocorra, exibe a mensagem de erro e continua o loop:
        except ValueError as e:
            limpar_tela()
            print(f"ERRO: {e}")
            pausar()
            continue
        #Executa as funções mesmo se ocorrer um erro:
        finally:
            limpar_tela()
    return opcao


def adicionar_produto(estoque):
    #Inicializa um loop infinito:
    while True:
        try:
            produto = input("Digite o nome do produto: ").capitalize()
            #Verifica se o produto já está cadastrado:
            if produto in estoque:
                #Caso o produto já esteja cadastrado, levanta um erro:
                raise ValueError("Produto já cadastrado.")
        #Caso um erro ocorra, exibe a mensagem de erro e continua o loop:
        except ValueError as e:
            print(f"ERRO: {e}")
            pausar()
            continue
        finally:
            limpar_tela()
        break

    #As proximas etapas seguem o mesmo padrão do código acima:
    while True:
        try:
            quantidade = int(input("Digite a quantidade do produto: "))
            if quantidade <= 0:
                raise ValueError("Digite um valor válido.")
        except ValueError as e:
            print(f"ERRO: {e}")
            pausar()
            continue
        finally:
            limpar_tela()
        break

    while True:
        try:
            preco_custo = float(input("Digite o preço de custo do produto: "))
            if preco_custo <= 0:
                raise ValueError("Digite um valor válido.")
        except ValueError as e:
            print(f"ERRO: {e}")
            pausar()
            continue
        finally:
            limpar_tela()
        break
    
    while True:
        try:
            preco_venda = float(input("Digite o preço de venda do produto: "))
            if preco_venda <= 0:
                raise ValueError("Digite um valor válido.")
        except ValueError as e:
            print(f"ERRO: {e}")
            pausar()
            continue
        finally:
            limpar_tela()
        break
    
    #Calcula o lucro do produto:
    lucro = preco_venda - preco_custo

    #Adiciona o produto ao estoque e exibe uma mensagem de sucesso:
    estoque.update({produto: {"quantidade": quantidade, "preço custo": preco_custo, "preço venda": preco_venda, "lucro": lucro}})
    print("Produto cadastrado com sucesso!")
    pausar()
    limpar_tela()
    return estoque


def remover_produto(estoque):
    #Verifica se há produtos cadastrados:
    if estoque:
        while True:
            try:
                excluir_produto = input("Digite o nome do produto que deseja remover: ").capitalize()
                if excluir_produto not in estoque:
                    raise KeyError("Produto não cadastrado.")
                else:
                    #Remove o produto do estoque:
                    del estoque[excluir_produto]
                    break
            except KeyError as e:
                print(f"ERRO: {e}")
                pausar()
                continue        
            finally:
                limpar_tela()

        print("Produto removido com sucesso!")
        pausar()
        limpar_tela()
        return estoque
    #Caso não haja produtos cadastrados, exibe uma mensagem de erro:
    else:
        erro_estoque_vazio()
        return estoque


def listar_produtos(estoque):
    if estoque:
        print("LISTA DE PRODUTOS:")
        print("------------------------------------------------------")
        '''
        Percorre o estoque e exibe os produtos cadastrados e
        suas respectivas informações:
        '''
        for produto, info in estoque.items():
            print(f"Produto: {produto}\n"
                f"Quantidade: {info['quantidade']}\n"
                f"Preço de Custo: R${info['preço custo']:.2f}\n"
                f"Preço de Venda: R${info['preço venda']:.2f}\n"
                f"Lucro: R${info['lucro']:.2f}")
            print("------------------------------------------------------")
        pausar()
        limpar_tela()
    else:
        erro_estoque_vazio()


def consultar_produto(estoque):
    if estoque:
        while True:
            try:
                produto = input("Digite o nome do produto que deseja consultar: ").capitalize()
                if produto not in estoque:
                    raise KeyError("Produto não cadastrado.")
                else:
                    #Exibe as informações do produto:
                    limpar_tela()
                    print("INFORMAÇÕES DO PRODUTO:")
                    print("------------------------------------------------------")
                    print(f"Produto: {produto}\n"
                        f"Quantidade: {estoque[produto]['quantidade']}\n"
                        f"Preço de Custo: R${estoque[produto]['preço custo']}\n"
                        f"Preço de Venda: R${estoque[produto]['preço venda']}\n"
                        f"Lucro: R${estoque[produto]['lucro']}")
                    print("------------------------------------------------------")
                    pausar()
                    break
            except KeyError as e:
                print(f"ERRO: {e}")
                pausar()
                continue
            finally:
                limpar_tela()
    else:
        erro_estoque_vazio()


def sair():
    for i in range(5, 0, -1):
        print(f"Saindo em {i}...")
        sleep(1)
        limpar_tela()
    print("Até logo!")

   
estoque = {}
while True:
    opcao = obter_opcao()

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
            sair()
            break