from exercicios.tarefas.funcs_tarefas import *
from exercicios.utils import close_program

#Armazena as tarefas:
tasks = list()

#Função principal:
def main(tasks):
    while True:
        message("MENU PRINCIPAL DAS TASKS:", [
            "Adc. tarefa", "Listar tarefa(s)", "Excluir tarefa", 
            "Visualizar tarefa", "Concluir tarefa", "Sair"
        ])
        opcao = option(6)
        clear()
        
        match opcao:
            case 1:
                tasks = add_task(tasks)
            case 2:
                all_tasks(tasks)
            case 3:
                tasks = remove_task(tasks)
            case 4:
                view_task(tasks)
            case 5:
                tasks = complete_task(tasks)
            case 6:
                close_program("Tchau!")
                break
       
#Excecução do programa:
if __name__ == '__main__':
    main(tasks)