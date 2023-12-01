    #Sistema de gerenciamento de tarefas

class Tarefa:
    def __init__(self, id, desc, tempo):
        self.id = id
        self.desc = desc
        self.tempo = tempo
        self.status = "ativa"


# Verifica se há ID existente para adicionar tarefas
def verificaId(id, lista_tarefas):
    for tarefa in lista_tarefas:      
        if tarefa.id == id:
            print("Erro! Motivo: ID já existe.")
            return 1
    return 0

# Adiciona novas tarefas
def addTarefa(lista_tarefas):
    id = input("\nIdentificador da tarefa: ")
    if not verificaId(id, lista_tarefas):
        desc = input("Descrição da tarefa: ")
        try:
            tempo = float(input("Tempo para realizar tarefa (em horas): "))
            if tempo <= 0:
                raise ValueError
        except ValueError:
            print("\nErro. Motivo: digite um número válido para definir o tempo.")
        else:
            nova_tarefa = Tarefa(id, desc, tempo)
            lista_tarefas.append(nova_tarefa)
            print("\nTarefa adicionada com sucesso!")

################################################################################

# Visualizar tarefas

# a)Exibe todas as tarefas
def verTudo(lista_tarefas):
    if not lista_tarefas:
        print("Não há tarefas na lista.\n")
    for tarefa in lista_tarefas:
        print(f"Descrição: {tarefa.desc}, Tempo: {tarefa.tempo} horas, Status: {tarefa.status}, ID: {tarefa.id}\n")

# b)Exibe apenas tarefas com status ativa
def verAtivas(lista_tarefas):
    for tarefa in lista_tarefas:
        if tarefa.status == 'ativa':
            print(f"Descrição: {tarefa.desc}, Tempo: {tarefa.tempo} horas, ID: {tarefa.id}\n")
        #Não há tarefas ativas/qualquer na lista?

# c)Exibe apenas tarefas com status concluída
def verConcluida(lista_tarefas):
    for tarefa in lista_tarefas:
        if tarefa.status == 'concluída':
            print(f"Descrição: {tarefa.desc}, Tempo: {tarefa.tempo} horas, ID: {tarefa.id}\n")
        #Não há tarefas concluídas/qualquer na lista?

# menu de visualização de tarefas
#CORRIGIR SITUACAO LISTA VAZIA
def visualizaTarefa(lista_tarefas):
    print("Digite o modo de visualização desejado: \n")
    while 1:
        print("\t1 - Todas as tarefas")
        print("\t2 - Tarefas ativas")
        print("\t3 - Tarefas concluídas")
        print("\t4 - Voltar")
        opcao = int(input(" \n"))
        if opcao == 1: 
            verTudo(lista_tarefas)
        elif opcao == 2:
            verAtivas(lista_tarefas)
        elif opcao == 3:
            verConcluida(lista_tarefas)
        elif opcao == 4:
            break

# !Bônus - prioridade visualização (Ativas /Limite tempo crescente/ concluídas)..

################################################################################
# Atualizar Tarefas
#CORRIGIR SITUACAO LISTA VAZIA
#CORRIGIR ID DIGITADO ERRADO
def atualizaTarefa(lista_tarefas):
    print("\tDigite o ID da tarefa que deseja atualizar: \n")
    verTudo(lista_tarefas)
    attid = input()
    for tarefa in lista_tarefas:
        if attid == tarefa.id:
            print("Tarefa selecionada: \n")
            print(f"Descrição: {tarefa.desc}, Tempo: {tarefa.tempo} horas, Status: {tarefa.status}.\n")
            print("Digite a opção que deseja atualizar: ")
            print("\t1 - Descrição")
            print("\t2 - Tempo")
            print("\t3 - Status")
            opt = int(input())
            if opt == 1:
                nova_desc = input("Digite a nova descrição: ")
                tarefa.desc = nova_desc
            elif opt == 2:
                novo_tempo = float(input("Digite o novo tempo: "))
                tarefa.tempo = novo_tempo
            elif opt == 3:
                novo_status = int(input("Digite uma opção para o novo status (1 - Ativa, 2 - Concluída): "))
                if novo_status == 1:
                    tarefa.status = 'ativa'
                elif novo_status == 2:
                    tarefa.status = 'concluída'
            else:
                print("Erro. Motivo: operação inválida.")                
################################################################################

# concluir Tarefas
#CORRIGIR SITUACAO LISTA VAZIA
#CORRIGIR ID DIGITADO ERRADO
def concluiTarefa(lista_tarefas):
    print("\tTarefas que podem ser concluídas: \n")
    verAtivas(lista_tarefas)
    conclui_id = input("Digite o ID da tarefa que deseja concluir: \n")
    for tarefa in lista_tarefas:
        if conclui_id == tarefa.id:
                tarefa.status = 'concluída'
                print("Bom trabalho! Tarefa Concluída.")

################################################################################

# Excluir Tarefas
#CORRIGIR SITUACAO LISTA VAZIA
#CORRIGIR ID DIGITADO ERRADO
def excluiTarefa(lista_tarefas):
    print("\tLista de tarefas: \n")
    verTudo(lista_tarefas)
    endid = input("Digite o ID da tarefa que deseja excluir: \n")
    for tarefa in lista_tarefas:
        if endid == tarefa.id:
            lista_tarefas.remove(tarefa)
            print("\nTarefa excluída com sucesso.")

################################################################################

# Menu de opções

def menuPrincipal():
    print("\tSistema de gerenciamento de tarefas - Faz Ae")

    lista_tarefas = []

    while 1:
        print("\nDigite qual opção você deseja:  \n")
        print("\t1 - Adicionar Tarefa")
        print("\t2 - Visualizar Tarefa")
        print("\t3 - Atualizar Tarefa")
        print("\t4 - Concluir Tarefa")
        print("\t5 - Excluir Tarefa")
        print("\t6 - Encerrar programa")
        try:
            opcao = int(input())
            if opcao == 1:
                addTarefa(lista_tarefas)
            elif opcao == 2:
                visualizaTarefa(lista_tarefas)
            elif opcao == 3:
                atualizaTarefa(lista_tarefas)
            elif opcao == 4:
                concluiTarefa(lista_tarefas)
            elif opcao == 5:
                excluiTarefa(lista_tarefas)
            elif opcao == 6:
                break
            else:
                raise ValueError
        except ValueError:
            print("\nErro. Motivo: Opção inválida")

menuPrincipal()