from exercicios.utils import message, clear, pause_clear, msg_exceptions


def adicionar_produto(estoque):
    '''
    Função que adiciona um produto ao estoque.
    
    :param estoque: Dicionário que armazena os produtos do estoque.
    :return: estoque
    '''
    def add_produto(estoque):
        '''
        Adiciona o nome de um produto ao estoque.
        
        :param estoque: Dicionário que armazena os produtos do estoque.
        :return: produto
        '''
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
                msg_exceptions(msg=f"ERRO: {e}")
                continue
            clear()
            return produto

    def add_quantidade():
        '''
        Adiciona a quantidade de um produto ao estoque.
        
        :param quantidade: Quantidade do produto.
        :return: quantidade
        '''     
        #As proximas etapas seguem o mesmo padrão do código acima:
        while True:
            try:
                quantidade = int(input("Digite a quantidade do produto: "))
                if quantidade <= 0:
                    raise ValueError("Digite um valor válido.")
            except ValueError as e:
                msg_exceptions(msg=f"ERRO: {e}")
                continue
            clear()
            return quantidade
        
    def add_preco_custo():
        '''
        Adiciona o preço de custo de um produto ao estoque.
        
        :return: preco_custo
        '''
        while True:
            try:
                preco_custo = float(input("Digite o preço de custo do produto: "))
                if preco_custo <= 0:
                    raise ValueError("Digite um valor válido.")
            except ValueError as e:
                msg_exceptions(f"ERRO: {e}")
                continue
            clear()
            return preco_custo
    
    def add_preco_venda():
        '''
        Adiciona o preço de venda de um produto ao estoque.
        
        :return: preco_venda
        '''      
        while True:
            try:
                preco_venda = float(input("Digite o preço de venda do produto: "))
                if preco_venda <= 0:
                    raise ValueError("Digite um valor válido.")
            except ValueError as e:
                msg_exceptions(f"ERRO: {e}")
                continue
            clear()
            return preco_venda
    
    #Funções que fornecem as informações do produto:
    produto = add_produto(estoque)
    quantidade = add_quantidade()
    preco_custo = add_preco_custo()
    preco_venda = add_preco_venda()

    #Calcula o lucro do produto:
    lucro = preco_venda - preco_custo

    #Adiciona o produto ao estoque e exibe uma mensagem de sucesso:
    estoque.update({produto: {"quantidade": quantidade, "preço custo": preco_custo, "preço venda": preco_venda, "lucro": lucro}})
    message("Produto cadastrado com sucesso!")
    pause_clear()
    return estoque


def remover_produto(estoque):
    '''
    Função que remove um produto do estoque.
    
    :param estoque: Dicionário que armazena os produtos do estoque.
    :return: estoque
    '''
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
                msg_exceptions(f"ERRO: {e}")
                continue        
        clear()
        message("Produto removido com sucesso!")
        pause_clear()
        return estoque
    #Caso não haja produtos cadastrados, exibe uma mensagem de erro:
    else:
        msg_exceptions("Não há produtos cadastrados no estoque.")
        return estoque


def listar_produtos(estoque):
    '''
    Função que lista os produtos do estoque.
    
    :param estoque: Dicionário que armazena os produtos do estoque.
    :return: não tem retorno
    '''
    if estoque:
        print("LISTA DE PRODUTOS:")
        print("------------------------------------------------------")
        '''
        Percorre o estoque e exibe os produtos cadastrados e
        suas respectivas informações:
        '''
        for produto in estoque:
            print(f"Produto = {produto}\n"
                  f"Quantidade = {estoque[produto]['quantidade']}\n"
                  f"Preço de custo = R${estoque[produto]['preço custo']:.2f}\n"
                  f"Preço de venda = R${estoque[produto]['preço venda']:.2f}\n"
                  f"Lucro = R${estoque[produto]['lucro']:.2f}")           
        print("------------------------------------------------------")
        pause_clear()
    else:
        msg_exceptions("Não há produtos cadastrados no estoque.")


def consultar_produto(estoque):
    '''
    Função que consulta um produto específico do estoque.
    
    :param estoque: Dicionário que armazena os produtos do estoque.
    :return: não tem retorno
    '''
    if estoque:
        while True:
            try:
                nome_produto = input("Digite o nome do produto que deseja consultar: ").capitalize()
                if nome_produto not in estoque:
                    raise KeyError("Produto não cadastrado.")
                else:
                    #Exibe as informações do produto:
                    clear()
                    print("INFORMAÇÕES DO PRODUTO:")
                    print("------------------------------------------------------")
                    for nome_produto in estoque:
                        print(f"Produto = {nome_produto}")
                        print(f"Quantidade = {estoque[nome_produto]['quantidade']}\n"
                              f"Preço de custo = R${estoque[nome_produto]['preço custo']:.2f}\n"
                              f"Preço de venda = R${estoque[nome_produto]['preço venda']:.2f}\n"
                              f"Lucro = R${estoque[nome_produto]['lucro']:.2f}")                         
                    print("------------------------------------------------------")
                    pause_clear()
                    break
            except KeyError as e:
                msg_exceptions(f"ERRO: {e}")
                continue
    else:
        msg_exceptions("Não há produtos cadastrados no estoque.")