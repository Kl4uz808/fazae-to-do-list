#Sistema de gerenciamento de tarefas

class Tarefa:
    def __init__(self, id, desc, tempo):
        self.id = id
        self.desc = desc
        self.tempo = tempo
        self.status = "ativa"


 # Verificar Id existente
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
        tempo = int(input("Tempo para realizar tarefa (em horas): "))
        nova_tarefa = Tarefa(id, desc, tempo)
        lista_tarefas.append(nova_tarefa)

################################################################################

# 2) Visualizar tarefas

# Exibe todas as tarefas
def verTudo(lista_tarefas):
    if not lista_tarefas:
        print("Não há tarefas na lista.\n")
    for tarefa in lista_tarefas:
        print(f"Descrição: {tarefa.desc}, Tempo: {tarefa.tempo} horas, Status: {tarefa.status}, ID: {tarefa.id}\n")

#Exibe apenas tarefas com status ativa
def verAtivas(lista_tarefas):
    for tarefa in lista_tarefas:
        if tarefa.status == 'ativa':
            print(f"Descrição: {tarefa.desc}, Tempo: {tarefa.tempo} horas, ID: {tarefa.id}\n")
        #Não há tarefas ativas/qualquer na lista?

#Exibe apenas tarefas com status concluída
def verConcluida(lista_tarefas):
    for tarefa in lista_tarefas:
        if tarefa.status == 'concluída':
            print(f"Descrição: {tarefa.desc}, Tempo: {tarefa.tempo} horas, ID: {tarefa.id}\n")
        #Não há tarefas concluídas/qualquer na lista?

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

# !Bônus - prioridade visualização (Ativas -Limite tempo crescente- concluídas)..

################################################################################
# 3) Atualizar Tarefas

def atualizaTarefa(lista_tarefas):
      return 0

    #Atualizar dados existentes das tarefas, exceto ID...

################################################################################

#4) concluir Tarefas

def concluiTarefa(lista_tarefas):
    print("\tTarefas que podem ser concluídas: \n")
    verAtivas(lista_tarefas)
    conclui_id = input("Digite o ID da tarefa que deseja concluir: \n")
    for tarefa in lista_tarefas:
        if conclui_id == tarefa.id:
                tarefa.status = 'concluída'
                print("Bom trabalho! Tarefa Concluída.")

################################################################################

#5) Excluir Tarefas

def excluiTarefa(lista_tarefas):
    print("\tLista de tarefas: \n")
    verTudo(lista_tarefas)
    endtarefa = input("Digite o ID da tarefa que deseja excluir: \n")
    for tarefa in lista_tarefas:
        if endtarefa == tarefa.id:
            lista_tarefas.remove(tarefa)
            print("\nTarefa excluída com sucesso.")

################################################################################


#6) Menu de opções

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
        opcao = int(input())

        if opcao == 1:
            addTarefa(lista_tarefas)
        elif opcao == 2:
            visualizaTarefa(lista_tarefas)
        elif opcao == 3:
            atualizaTarefa(lista_tarefas)
            break
        elif opcao == 4:
            concluiTarefa(lista_tarefas)
        elif opcao == 5:
            excluiTarefa(lista_tarefas)
        elif opcao == 6:
            break
        else:
            print("\nOpção inválida")
            
menuPrincipal()