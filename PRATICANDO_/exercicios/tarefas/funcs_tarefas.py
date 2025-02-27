from exercicios.utils import message, clear, option, msg_exceptions, pause_clear


def add_task(tasks):
    '''
    Adiciona as informações das tasks.
    
    :param tasks: lista com as tasks.
    :return: tasks
    '''
    #Informações da task:
    infos_task = dict()
    
    #Funções responsáveis por captarem as informações da task:
    def task_title(tasks):
        '''
        Captura o título da task.
        
        :param tasks: lista com as tasks.
        :return: title
        '''
        while True:
            message("TÍTULO DA TASK:")
            title = input("R: ").capitalize()
            #Verifica a quantidade de elementos na lista:
            if len(tasks) > 0:
                for i in range(0, len(tasks)):
                    #verifica se o título informado já existe em "tasks":
                    if tasks[i]['Título'] == title:
                        msg_exceptions("Já existe uma tarefa com este mesmo nome!")
                        break
                    continue
                #Caso o título informado não esteja em "tasks":
                else:
                    clear()
                    return title
            #Caso o elemento informado seja o primeiro a ser inserido em "tasks":
            else:
                clear()
                return title
    
    def task_description():
        '''
        Captura a descrição da task.
        
        :return: description
        '''
        while True:
            message("DESCRIÇÃO DA TASK:", ['Sem descrição', 'Com descrição'])
            opcao = option(2)
            
            #Checa a opção informada pelo usuário:
            match opcao:
                #Caso a opção 1 seja escolhida:
                case 1:
                    description = "Sem descrição"
                #Caso seja a 2:
                case 2:
                    clear()
                    #Recebe a descrição da task:
                    message("DESCRIÇÃO DA TASK:")
                    description = input("R: ").capitalize()
                case _:
                    continue
            clear()
            return description
        
    #Chamada das funções anteriores:
    title = task_title(tasks)
    description = task_description()
    
    #Exibe uma mensagem informando que a task foi cadastrada:
    message(f"Task '{title}' cadastrada com sucesso!")
    pause_clear()
    #Inserem as informações da task em seus respectivos locais:
    infos_task.update({'Título': title, 'Descrição': description, 'Status': 'Pendente'})
    tasks.append(infos_task)
    return tasks


def all_tasks(tasks):
    '''
    Mostra todas as tasks cadastradas ou mostra todas
    as tasks com o status informado pelo usuário:
    
    :param tasks: lista com as tasks.
    :return: None
    '''
    #Verifica se há elementos na lista "tasks":
    if len(tasks) > 0:    
        message("TODAS AS TASKS CADASTRADAS: ")
        #Mostra todas as tasks cadastradas:
        for i in range(0, len(tasks)):
            for k, v in tasks[i].items():
                print(f"{k} -> {v}")
            print("====================================")
        pause_clear()            
    #Caso não haja tasks cadastradas:
    else:
        msg_exceptions("Nenhuma task cadastrada!")
        

def remove_task(tasks):
    '''
    Remove a task informada pelo usuário.
    
    :param tasks: lista com as tasks.
    :return: tasks
    '''
    if len(tasks) > 0:
        #Recebe o título da task a ser removida:
        message("Informe o título da task a ser removida!")
        task_remove = input("R: ").capitalize()
        
        for i in range(0, len(tasks)):
            #Checa se a task existe em "tasks":
            if tasks[i]['Título'] == task_remove:
                #Checa se o status está pendente:
                if tasks[i]['Status'] == "Pendente":
                    clear()
                    #Pergunta se o usuário deseja remover a task, mesmo ela estando pendente:
                    message("Esta task está pendente, deseja remover?", ['Sim','Não'])
                    opcao = option(2)
                    
                    match opcao:
                        case 1:
                            #Remove a task:
                            tasks.remove(tasks[i])
                            clear()
                            message(f"Task '{task_remove}' removida com sucesso!")
                            pause_clear()
                            break
                        case 2:
                            #Cancela a exclusão:
                            msg_exceptions("Operação cancelada!")
                            break
                        case _:
                            break
                #Caso a task informada esteja concluída, ela é removida diretamente:
                else:
                    tasks.remove(tasks[i])
                    clear()
                    message(f"Task '{task_remove}' removida com sucesso!")
                    pause_clear()
                    break
            #Caso a task não exista em "tasks":
            else:
                msg_exceptions("Task não encontrada!")
    else:
        msg_exceptions("Nenhuma task cadastrada!")
    return tasks


def view_task(tasks):
    '''
    Visualiza uma task informada pelo usuário.
    
    :param tasks: lista com as tasks.
    :return: None
    '''
    if len(tasks) > 0:
        message("Informe o título da task a ser visualizada!")
        task_view = input("R: ").capitalize()
        
        for i in range(0, len(tasks)):
            #verifica se a task existe:
            if tasks[i]['Título'] == task_view:
                clear()
                #Exibe as informações da task:
                message("INFORMAÇÕES DA TASK:")
                for k, v in tasks[i].items():
                    print(f"{k} -> {v}")
                print("===================================")
                pause_clear()
                break               
            #Caso a task não exista:
            else:
                msg_exceptions("Task não encontrada!")
    else:
        msg_exceptions("Nenhuma task cadastrada!")


def complete_task(tasks):
    '''
    Marca uma task como concluída.
    
    :param tasks: lista com as tasks.
    :return: tasks
    '''
    if len(tasks) > 0:
        message("Informe o título da task a ser concluída!")
        task_complete = input("R: ").capitalize()
        
        for i in range(0, len(tasks)):
            #verifica se a task existe:
            if tasks[i]['Título'] == task_complete:
                clear()
                #Exibe as informações da task:
                message("MARCAR COMO CONLCUÍDA?", ['Sim', 'Não'])
                opcao = option(2)
                
                match opcao:
                    case 1:
                        #Marca a task como concluída
                        tasks[i]['Status'] = "Concluída"
                        clear()
                        message(f"Task '{task_complete}' concluída com sucesso!")
                        pause_clear()
                        break
                    case 2:
                        msg_exceptions("Operação cancelada!")
                        break
                    case _:
                        break
            #Caso a task não exista:
            else:
                msg_exceptions("Task não encontrada!")
    else:
        msg_exceptions("Nenhuma task cadastrada!")
    return tasks