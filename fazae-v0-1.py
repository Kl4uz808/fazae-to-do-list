#Sistema de gerenciamento de tarefas

# Cada tarefa possui ID, descrição, tempo limite (h), situação
# Toda NOVA tarefa possui situação ativa

class Tarefa:
    id = None
    desc = None
    tempo = None
    status = "ativa"


# 1) Adicionar Tarefas

def addTarefa(lista_tarefas):
    tarefa = Tarefa()
    tarefa.id = input("\nIdentificador da tarefa: ")
    tarefa.desc = input("Descrição da tarefa: ")
    tarefa.tempo = int(input("Tempo para realizar tarefa (em horas): "))

    # SE id for existente = error msg - volta menu

# 1.1) verificar ID

def verificaId(lista_tarefas, id):
    return 0

    # recebe id informado pelo usuario
    # busca e compara todos os ID's na lista
    #retorna valido / nao valido

################################################################################

# 2) Visualizar tarefas
      # Todas as tarefas / Ativas / Concluídas

def visualizaTarefa(lista_tarefas):
    print("Digite o modo de visualização desejado: ")
    while 1:
        print("\t1 - Todas as tarefas")
        print("\t2 - Tarefas ativas")
        print("\t3 - Tarefas concluídas")
        opcao = int(input())
        break

# Descobrir como retornar as informações e selecionar as tarefas desejadas..


# !Bônus - prioridade visualização (Ativas-Limite tempo crescente-Concluídas)..

################################################################################
# 3) Atualizar Tarefas

def atualizaTarefa(lista_tarefas):
      return 0

    #Atualizar dados existentes das tarefas, exceto ID...

################################################################################

#4) Concluir Tarefas

def concluiTarefa(lista_tarefas):
    return 0

    # Solicitar ID tarefa desejada..
    # Mudar status tarefa correspondente..

    # OU visualiza TODAS tarefas ativas - Digita id desejado - muda status...

################################################################################

#5) Excluir Tarefas

def excluiTarefa(lista_tarefas):
    return 0

    #Visualiza TODAS tarefas ativas - digita id desejado - exclui da lista

################################################################################
#6) Menu de opções

def menuPrincipal():
    print("\tSistema de gerenciamento de tarefas - FazAí")

    lista_tarefas = []

    while 1:
        print("\nDigite qual opção você deseja:  \n")
        print("\t1 - Adicionar Tarefa")
        print("\t2 - Visualizar Tarefa")
        print("\t3 - Atualizar Tarefa")
        print("\t4 - Concluir Tarefa")
        print("\t5 - Excluir Tarefa")
        print("\t6 - Encerrar programa")
        opcao = int(input())

        if opcao == 1:
            addTarefa(lista_tarefas)
            break
        elif opcao == 2:
            visualizaTarefa(lista_tarefas)
            break
        elif opcao == 3:
            atualizaTarefa(lista_tarefas)
            break
        elif opcao == 4:
            concluiTarefa(lista_tarefas)
            break
        elif opcao == 5:
            excluiTarefa(lista_tarefas)
            break
        elif opcao == 6:
            break
        else:
            print("\nOpção inválida")
menuPrincipal()
