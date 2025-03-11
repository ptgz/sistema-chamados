import os

chamados = []
contadorId = 1

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def topbar(text):
    print(f"-+-+- {text} -+-+-")

def cadastrarChamado(descricao, prioridade):
    global contadorId
    chamado = {
        'id': contadorId,
        'descricao': descricao,
        'prioridade': prioridade,
        'status': 'Aberto',
    }
    chamados.append(chamado)
    contadorId += 1
    print(f'Chamado {chamado["id"]} inserido!')


def buscarChamado(termo):
    resultado = []
    for i in chamados:
        if termo == str(i['id']) or termo.lower() in i['descricao'].lower():
            resultado.append(i)
    if resultado:
        for c in resultado:
            print(
                f'ID: {c["id"]}, Descrição: {c["descricao"]}, Prioridade: {c["prioridade"]}, Status: {c["status"]}')
    else:
        print('Nenhum chamado encontrado...')


def removerChamado(idChamado):
    for i in chamados:
        if i['id'] == idChamado:
            print(f'Chamado encontrado: \n{i}\n\nConfirma a remoção?\nDigite "S" para confirmar: ')
            chamados.remove(i)
            print(f'Chamado {idChamado} removido!')
            return
    print(f'chamado {idChamado} não encontrado')


def listarChamados():
    if not chamados:
        print('Nenhum chamado cadastrado.')
    else:
        for c in sorted(chamados, key=lambda x: x['prioridade']):
            print(
                f'ID: {c["id"]}, Descrição: {c["descricao"]}, Prioridade: {["Alta", "Média", "Baixa"][c["prioridade"]-1]}, Status: {c["status"]}')


def exibirEstatisticas():
    abertos = 0
    for i in chamados:
        if i['status'] == 'Aberto':
            abertos += 1
    finalizados = len(chamados) - abertos
    print(
        f'Total: {len(chamados)}, Chamados abertos: {abertos}, Chamados finalizados: {finalizados}')


def reverterLista():
    chamados.reverse()
    print('Lista revertida!')


def limparLista():
    chamados.clear()
    print("Lista limpa!")


def finalizarChamado(idFinalizar):
    for i in chamados:
        if i['id'] == idFinalizar:
            i['status'] = 'finalizado'
            cls()
            topbar('Finalizar Chamados')
            print(f'Chamado {idFinalizar} finalizado!')
            input('Pressione qualquer tecla para continuar...')
            return
    cls()
    topbar('Finalizar Chamados')
    print(f'Chamado {idFinalizar} não encontrado')
    input('Pressione qualquer tecla para continuar...')

while True:
    cls()
    print("-+-+- Sistema de Chamados -+-+-")
    print("1. Cadastrar Chamado")
    print("2. Buscar Chamado")
    print("3. Remover Chamado")
    print("4. Listar Chamados")
    print("5. Exibir Estatísticas")
    print("6. Inverter Lista de Chamados")
    print("7. Limpar Chamados")
    print("8. Finalizar Chamado")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cls()
        topbar('Cadastro de Chamado')
        descricao = input('Descrição: ')
        prioridade = int(input('Prioridade 1-3 (1 é maior e 3 menor): '))
        if prioridade not in [1, 2, 3]:
            print("Por favor, siga os padrões de resposta.")
            input('Pressione qualquer tecla para continuar...')
            continue
        cls()
        topbar('Cadastro de Chamado')
        print(f'Confirma estes dados?\nDescrição: {descricao}\nPrioridade: {["Alta", "Média", "Baixa"][prioridade-1]} ({prioridade})')
        _b = input('Pressione qualquer tecla para confirmar, ou 0 para cancelar...')
        if _b == '0':
            continue
        cadastrarChamado(descricao, prioridade)
        cls()
        topbar('Cadastro de Chamado')
        print('Chamado cadastrado com sucesso!')
        input('Pressione qualquer tecla para continuar...')
    elif opcao == '2':
        cls()
        topbar('Buscar Chamado')
        termo = input('Digite ID ou descrição: ')
        cls()
        topbar('Buscar Chamado')
        buscarChamado(termo)
        input('Pressione qualquer tecla para continuar...')
        
    elif opcao == '3':
        cls()
        topbar('Buscar Chamado')
        idChamado = int(input('Digite o ID do chamado para remover: '))
        removerChamado(idChamado)
        cls()
        topbar('Remover Chamado')
        input('Pressione qualquer tecla para continuar...')
    elif opcao == '4':
        cls()
        topbar('Lista de Chamados')
        listarChamados()
        input('Pressione qualquer tecla para continuar...')
    elif opcao == '5':
        cls()
        topbar('Estatísticas')
        exibirEstatisticas()
        input('Pressione qualquer tecla para continuar...')
    elif opcao == '6':
        cls()
        topbar('Inverter Lista de Chamados')
        reverterLista()
        input('Pressione qualquer tecla para continuar...')
    elif opcao == '7':
        cls()
        topbar('Limpar Chamados')
        desicao = input("Gostaria de limpar a lista de chamados? (S/N): ")
        if desicao.lower() == 's':
            limparLista()
            cls()
            topbar('Limpar Chamados')
            print('Lista de chamados limpa!')
            input('Pressione qualquer tecla para continuar...')
        elif desicao.lower() == 'n':
            cls()
            topbar('Limpar Chamados')
            print('Ação cancelada!')
            input('Pressione qualquer tecla para continuar...')
            continue
    elif opcao == '8':
        cls()
        topbar('Finalizar Chamados')
        idFinalizar = int(input("Digite o ID do chamado para finalizar: "))
        finalizarChamado(idFinalizar)
    elif opcao == '0':
        print('Saindo...')
        break
    else:
        cls()
        topbar('Opção inválida')
        print('Por favor digite uma das opções válidas no menu.\n')
        input('Pressione qualquer tecla para continuar...')
